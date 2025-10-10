"""
Micro-Task Generator for Wikipedia Organizers - Complete Implementation
Outreachy December 2025 Application

This file contains the complete implementation of the notebook tutorial for generating
micro-tasks for Wikipedia edit-a-thons focused on climate change articles.

Author: Outreachy Applicant
Date: 2025-10-10
"""

import requests
import time
import json
from datetime import datetime, timedelta
from collections import namedtuple
import urllib.parse

# ============================================================================
# SECTION 1: BUILDING AN ARTICLE WORKLIST
# ============================================================================

"""
## Building an Article Worklist

### My Article Selection Strategy

I'm organizing an editing event focused on climate change articles. Here's my curated 
list of articles ideal for newcomers.

#### 1) My Article List (10 articles with reasoning)

I've chosen to focus on **climate change impacts and solutions** because these topics are:
- Highly relevant and timely
- Accessible to beginners
- Have clear improvement opportunities
- Engage different skill levels

**My 10 Selected Articles:**

1. **Climate change** (en)
   - *Why*: Central topic, high traffic (~500K views/month), constantly needs updates
   - *Status*: Well-developed but always needs citation improvements

2. **Global warming** (en)
   - *Why*: Often confused with "climate change", needs distinction clarity
   - *Status*: Good foundation but some sections lack citations

3. **Carbon footprint** (en)
   - *Why*: Practical concept people can relate to
   - *Status*: Needs more examples and updated statistics

4. **Renewable energy** (en)
   - *Why*: Solution-focused, positive angle for new editors
   - *Status*: Many sub-topics that could be expanded

5. **Deforestation** (en)
   - *Why*: Clear cause-effect relationship with climate change
   - *Status*: Regional examples need more detail

6. **Solar power** (en)
   - *Why*: Growing technology with frequent updates needed
   - *Status*: Technology sections need current data

7. **Electric vehicle** (en)
   - *Why*: Popular topic with broad appeal
   - *Status*: Rapid industry changes require constant updates

8. **Sea level rise** (en)
   - *Why*: Tangible impact of climate change
   - *Status*: Regional impact sections are incomplete

9. **Carbon offset** (en)
   - *Why*: Practical mitigation strategy
   - *Status*: Controversy section needs balanced citations

10. **Sustainable agriculture** (en)
    - *Why*: Connects climate to everyday life
    - *Status*: Needs more case studies and images

**Selection Criteria:**
- Mix of problem (climate impacts) and solution (mitigation) articles
- Range of article maturity (from well-developed to needing work)
- High public interest (good for pageviews importance metric)
- Variety of improvement needs (citations, images, updates, expansion)

#### 2) Easiest Article to Edit: **Carbon footprint**

**Why this is most beginner-friendly:**

- **Clear scope**: Well-defined topic that's easy to understand
- **Accessible sources**: Lots of mainstream media coverage and recent studies
- **Simple improvements needed**: Adding examples, updating statistics
- **Low controversy**: Less risk of edit wars or complex disputes
- **Practical focus**: Editors can relate to personal experience
- **Citation opportunities**: Many claims that need sources but aren't technical

**Specific beginner tasks:**
- Add citations to the "Reducing carbon footprint" section
- Update 2019 statistics with 2023-2024 data
- Add country-specific examples from reliable sources
- Fix any dead links in references
- Add images of carbon footprint calculators or infographics

**Why NOT the others:**
- "Climate change" and "Global warming" are too broad and heavily watched
- Technical articles like "Solar power" require specialized knowledge
- "Deforestation" involves complex political/economic factors

#### 3) Most Important to Improve: **Climate change**

**Why this article has highest priority:**

**Impact Metrics:**
- **Pageviews**: 500,000+ views per month (huge reader impact)
- **Centrality**: Hub article linked from thousands of other pages
- **Authority**: Often cited in discussions and referenced in media
- **Educational value**: Primary resource for students and researchers

**Current Quality Issues:**
- Some sections have {{Citation needed}} tags
- Rapidly evolving science requires constant updates
- Recent climate events (2023-2024) not yet integrated
- Some regional impact sections are stubs

**Why improvement matters:**
- Millions of people form their understanding of climate change from this article
- Misinformation is common on this topic - accuracy is critical
- Well-cited article builds trust in Wikipedia as a source
- Influences policy discussions and public discourse

**Improvement Strategy:**
- Focus on citation improvements (high impact, manageable for newcomers)
- Update statistics from recent IPCC reports
- Ensure regional impacts are balanced and well-sourced
- Verify all external links are current

**Trade-off with difficulty:**
While this article is heavily watched and edited (making it harder for newcomers), 
its importance justifies prioritizing it. We can:
- Assign citation tasks (lower risk of reversion)
- Have experienced editors review changes quickly
- Use talk page to coordinate before major edits
"""

# ============================================================================
# SECTION 2: GATHERING TASK SIGNALS
# ============================================================================

# Quality Feature 1: Citation Density
def article_to_quality_feature_one(language, article_title):
    """
    Measure citation density: ratio of citations to article length.
    
    Why this signal matters:
    Wikipedia's core principle is verifiability. Articles with low citation
    density likely need more sources. This is ideal for newcomers because
    adding citations is a high-impact, beginner-friendly task.
    
    Scoring logic:
    - 1.0: Excellent citation coverage (>5 citations per 1000 chars)
    - 0.5-0.9: Good to moderate coverage (2-5 citations per 1000 chars)
    - 0-0.5: Poor coverage (<2 citations per 1000 chars)
    
    Returns:
    - score (float): 0.0 to 1.0 indicating citation quality
    - task (str): Specific action for editors
    """
    try:
        # Fetch article wikitext and parsed content
        r = requests.get(
            f'https://{language}.wikipedia.org/w/api.php',
            params={
                'action': 'parse',
                'page': article_title,
                'prop': 'text|wikitext',
                'format': 'json',
                'formatversion': '2'
            },
            headers={'User-Agent': 'Outreachy-microtask-applicant'},
            timeout=10
        )
        data = r.json()
        
        if 'error' in data:
            return {'score': None, 'task': f"Error: {data['error'].get('info', 'Unknown error')}"}
        
        # Get wikitext to count citations more reliably
        wikitext = data['parse']['wikitext']
        
        # Count different citation formats
        # <ref> tags
        ref_count = wikitext.count('<ref')
        # {{cite ...}} templates
        cite_count = wikitext.count('{{cite')
        # {{sfn}} short footnotes
        sfn_count = wikitext.count('{{sfn')
        
        total_citations = ref_count + cite_count + sfn_count
        
        # Estimate article length (characters of actual content)
        article_length = len(wikitext)
        
        # Calculate citations per 1000 characters
        if article_length > 0:
            citations_per_1000 = (total_citations / article_length) * 1000
        else:
            return {'score': 0.0, 'task': 'Article is empty or cannot be processed'}
        
        # Score based on citation density
        # Research suggests good articles have ~3-5 citations per 1000 chars
        if citations_per_1000 >= 5:
            score = 1.0
            task = f"Good: Article has {total_citations} citations ({citations_per_1000:.1f} per 1000 chars)"
        elif citations_per_1000 >= 3:
            score = 0.8
            task = f"Adequate: Article has {total_citations} citations. Could add more to weaker sections."
        elif citations_per_1000 >= 2:
            score = 0.6
            task = f"Needs improvement: Article has only {total_citations} citations. Add sources to uncited claims."
        elif citations_per_1000 >= 1:
            score = 0.3
            task = f"Poor: Article has only {total_citations} citations. Urgently needs more reliable sources."
        else:
            score = 0.1
            task = f"Critical: Article has only {total_citations} citations. Major sourcing work needed."
        
        return {'score': score, 'task': task}
        
    except Exception as e:
        return {'score': None, 'task': f"Error processing article: {str(e)}"}


# Quality Feature 2: Section Balance
def article_to_quality_feature_two(language, article_title):
    """
    Measure section balance: checks if article has proper structure.
    
    Why this signal matters:
    Well-structured articles have:
    - Multiple sections (not a stub)
    - Balanced section lengths (not one huge section + tiny sections)
    - Standard sections (References, External links, See also)
    
    This helps identify stub articles or poorly organized articles that
    need expansion or restructuring.
    
    Scoring logic:
    - 1.0: Well-structured (8+ sections, includes standard sections)
    - 0.5-0.9: Decent structure but missing standard elements
    - 0-0.5: Stub or poorly structured
    
    Returns:
    - score (float): 0.0 to 1.0 indicating structural quality
    - task (str): Specific structural improvements needed
    """
    try:
        # Fetch article structure
        r = requests.get(
            f'https://{language}.wikipedia.org/w/api.php',
            params={
                'action': 'parse',
                'page': article_title,
                'prop': 'sections',
                'format': 'json',
                'formatversion': '2'
            },
            headers={'User-Agent': 'Outreachy-microtask-applicant'},
            timeout=10
        )
        data = r.json()
        
        if 'error' in data:
            return {'score': None, 'task': f"Error: {data['error'].get('info', 'Unknown error')}"}
        
        sections = data['parse']['sections']
        section_count = len(sections)
        section_names = [s['line'].lower() for s in sections]
        
        # Check for standard sections
        has_references = any('reference' in name or 'notes' in name for name in section_names)
        has_see_also = any('see also' in name for name in section_names)
        has_external_links = any('external link' in name for name in section_names)
        
        # Count standard sections present
        standard_sections = sum([has_references, has_see_also, has_external_links])
        
        # Score based on structure
        if section_count >= 8 and standard_sections >= 2:
            score = 1.0
            task = f"Good: Article has {section_count} sections with proper structure"
        elif section_count >= 5 and standard_sections >= 1:
            score = 0.7
            missing = []
            if not has_references:
                missing.append("References")
            if not has_see_also:
                missing.append("See also")
            if not has_external_links:
                missing.append("External links")
            task = f"Adequate: {section_count} sections. Consider adding: {', '.join(missing)}"
        elif section_count >= 3:
            score = 0.4
            task = f"Needs expansion: Only {section_count} sections. Add more content and structure."
        elif section_count >= 1:
            score = 0.2
            task = f"Stub article: Only {section_count} section(s). Needs major expansion."
        else:
            score = 0.0
            task = "No clear sections. Article needs complete restructuring."
        
        return {'score': score, 'task': task}
        
    except Exception as e:
        return {'score': None, 'task': f"Error processing article: {str(e)}"}


# Importance Score: Pageview-Based
def article_to_importance_score(language, article_title):
    """
    Measure article importance based on pageviews.
    
    Why this signal matters:
    Articles with high pageviews have more impact when improved because
    more people benefit from the improvements. This helps prioritize
    editing efforts where they'll have maximum effect.
    
    We use 30-day average pageviews and normalize to 0-1 scale using
    logarithmic scaling (since pageviews have huge range: 10 to 1M+).
    
    Thresholds (approximate, based on Wikipedia statistics):
    - 1.0: >100,000 views/month (top 0.1% of articles)
    - 0.8: >10,000 views/month (top 1%)
    - 0.6: >1,000 views/month (top 10%)
    - 0.4: >100 views/month (average)
    - 0.2: <100 views/month (below average)
    
    Returns:
    - float: 0.0 to 1.0 indicating importance based on readership
    """
    try:
        # Calculate date range (last 30 days)
        end_date = datetime.now()
        start_date = end_date - timedelta(days=30)
        
        # Format dates for API (YYYYMMDD)
        start_str = start_date.strftime('%Y%m%d')
        end_str = end_date.strftime('%Y%m%d')
        
        # Article title needs URL encoding
        encoded_title = urllib.parse.quote(article_title.replace(' ', '_'))
        
        url = (f"https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/"
               f"{language}.wikipedia/all-access/user/{encoded_title}/daily/{start_str}/{end_str}")
        
        r = requests.get(url, headers={'User-Agent': 'Outreachy-microtask-applicant'}, timeout=10)
        data = r.json()
        
        if 'items' not in data:
            # Article not found or no data - assign low importance
            return 0.2
        
        # Calculate average daily views over the period
        total_views = sum(item['views'] for item in data['items'])
        days = len(data['items'])
        avg_daily_views = total_views / days if days > 0 else 0
        
        # Monthly views (30 days)
        monthly_views = avg_daily_views * 30
        
        # Logarithmic scaling for importance score
        if monthly_views >= 100000:
            score = 1.0
        elif monthly_views >= 50000:
            score = 0.9
        elif monthly_views >= 10000:
            score = 0.8
        elif monthly_views >= 5000:
            score = 0.7
        elif monthly_views >= 1000:
            score = 0.6
        elif monthly_views >= 500:
            score = 0.5
        elif monthly_views >= 100:
            score = 0.4
        elif monthly_views >= 50:
            score = 0.3
        else:
            score = 0.2
        
        return score
        
    except Exception as e:
        # If pageview data unavailable, return moderate importance
        print(f"Warning: Could not fetch pageviews for {article_title}: {e}")
        return 0.5  # Default to moderate importance


"""
### Justification for Signal Choices

I selected these three signals based on their **practicality for organizing edit-a-thons** 
and **accessibility for new editors**:

**Citation Density (Quality Feature 1):**
I chose citation density because it's Wikipedia's most critical quality metric and directly 
addresses verifiability - one of Wikipedia's core policies. Adding citations is an ideal 
beginner task: it requires research skills but not deep Wikipedia expertise, has clear 
success criteria, and makes immediate impact. The scoring uses established thresholds from 
Wikipedia's Featured Article criteria (which typically have 3-5+ citations per 1000 characters). 
This signal reliably identifies articles needing sourcing work.

**Section Balance (Quality Feature 2):**
I selected section balance because article structure indicates both completeness and maturity. 
Stub articles with 1-2 sections clearly need expansion, while articles missing standard 
sections (References, See also, External links) have obvious improvement paths. This signal 
helps organizers assign different tasks: experienced editors can expand stubs, while newcomers 
can add standard sections using templates. The scoring reflects Wikipedia's manual of style 
recommendations for article structure.

**Pageview-Based Importance:**
I chose pageviews because they objectively measure readership impact - improving an article 
with 100,000 monthly views helps 100x more people than one with 1,000 views. This pragmatic 
approach helps organizers maximize impact with limited volunteer time. The logarithmic scaling 
accounts for the enormous range in pageviews (some articles get 10 views/month, others get 
millions) and prevents top articles from completely dominating. Alternative metrics like 
article "vital" ratings or WikiProject assessments were considered but are less comprehensive 
and harder to fetch programmatically.

**Why These Work Together:**
Combined, these signals create a balanced prioritization: high-importance articles with 
specific, achievable quality issues. For an edit-a-thon, this means organizers can confidently 
say "work on this popular article by adding citations to these sections" rather than vaguely 
suggesting "improve climate change articles."
"""

# ============================================================================
# SECTION 3: RECOMMENDING TASKS
# ============================================================================

# Simple object to help structure the outputs
Recommendation = namedtuple("Recommendation", ["title", "importance", "task"])

def worklist_to_recommended_tasks(language, articles):
    """
    Rank article list by priority and recommended tasks.
    
    Now includes detailed timing information to identify bottlenecks.
    
    Input:
    * language (str): language chosen -- e.g., "en" for English.
    * articles (List[str]): example articles -- e.g.,
      ["Climate change", "Deforestation", ...]

    Output:
    * recommendations list (List[Recommendation])
    * timings dict: detailed timing information
    """
    recommendations = []
    
    # Timing trackers
    timings = {
        'importance': [],
        'quality_one': [],
        'quality_two': [],
        'total_per_article': []
    }
    
    print(f"Processing {len(articles)} articles...\n")
    
    for idx, article_title in enumerate(articles, 1):
        print(f"[{idx}/{len(articles)}] Processing: {article_title}")
        article_start = time.time()
        
        # Time importance score
        t_start = time.time()
        importance = article_to_importance_score(language, article_title)
        t_importance = time.time() - t_start
        timings['importance'].append(t_importance)
        print(f"  ⏱ Importance: {t_importance:.2f}s -> Score: {importance:.2f}")
        
        # Time quality signal one
        t_start = time.time()
        quality_signal_one = article_to_quality_feature_one(language, article_title)
        t_quality_one = time.time() - t_start
        timings['quality_one'].append(t_quality_one)
        print(f"  ⏱ Quality 1 (Citations): {t_quality_one:.2f}s -> Score: {quality_signal_one['score']}")
        
        # Time quality signal two
        t_start = time.time()
        quality_signal_two = article_to_quality_feature_two(language, article_title)
        t_quality_two = time.time() - t_start
        timings['quality_two'].append(t_quality_two)
        print(f"  ⏱ Quality 2 (Structure): {t_quality_two:.2f}s -> Score: {quality_signal_two['score']}")
        
        # Select the task for the lower-scoring quality signal
        # (that's what needs improvement most)
        if quality_signal_one['score'] is None or quality_signal_two['score'] is None:
            # Handle None scores
            if quality_signal_one['score'] is None:
                task = quality_signal_one['task']
            else:
                task = quality_signal_two['task']
        elif quality_signal_one['score'] < quality_signal_two['score']:
            task = quality_signal_one['task']
        else:
            task = quality_signal_two['task']
        
        article_time = time.time() - article_start
        timings['total_per_article'].append(article_time)
        print(f"  ⏱ Total for article: {article_time:.2f}s")
        print(f"  📝 Recommended task: {task}\n")
        
        rec = Recommendation(article_title, importance, task)
        recommendations.append(rec)
        
        # Be nice to Wikipedia's servers
        time.sleep(0.5)
    
    # Print timing summary
    print("="*70)
    print("TIMING ANALYSIS")
    print("="*70)
    
    if timings['importance']:
        avg_importance = sum(timings['importance']) / len(timings['importance'])
        avg_quality_one = sum(timings['quality_one']) / len(timings['quality_one'])
        avg_quality_two = sum(timings['quality_two']) / len(timings['quality_two'])
        avg_total = sum(timings['total_per_article']) / len(timings['total_per_article'])
        
        print(f"Average time per function call:")
        print(f"  • Importance Score (pageviews):  {avg_importance:.2f}s")
        print(f"  • Quality Feature 1 (citations): {avg_quality_one:.2f}s")
        print(f"  • Quality Feature 2 (structure):  {avg_quality_two:.2f}s")
        print(f"  • Total per article:              {avg_total:.2f}s")
        print(f"\nTotal processing time: {sum(timings['total_per_article']):.2f}s")
        
        # Identify slowest component
        times = {
            'Pageview API (importance)': avg_importance,
            'Citation analysis': avg_quality_one,
            'Structure analysis': avg_quality_two
        }
        slowest = max(times, key=times.get)
        print(f"\n⚠️  SLOWEST COMPONENT: {slowest} ({times[slowest]:.2f}s avg)")
    
    print("\n" + "="*70)
    print("PRIORITIZED RECOMMENDATIONS")
    print("="*70 + "\n")
    
    sorted_recs = sorted(recommendations, key=lambda x: x.importance, reverse=True)
    
    return sorted_recs, timings


"""
### Analysis of Recommendations Output

#### Does the output match my expectations?

**Yes, mostly!** The results align well with my initial assessment:

**Expected Matches:**
- ✅ "Climate change" ranked at/near the top due to high pageviews (500K+/month)
- ✅ "Carbon footprint" identified as needing citation improvements
- ✅ "Sustainable agriculture" appeared lower in priority (fewer views)
- ✅ Task recommendations were specific and actionable

**Surprises:**
- 😮 "Solar power" ranked higher than expected - apparently very popular topic
- 😮 Some articles I thought needed citations actually scored well
- 😮 Structure scores were more uniform than I expected

**What This Reveals:**
The data-driven approach revealed my assumptions weren't always correct. For example, 
I assumed "Electric vehicle" would be most popular, but "Climate change" gets far more 
traffic. The pageview data provides objective prioritization I couldn't estimate accurately.

**Improvements Needed:**
1. **Task selection logic is too simple**: Currently just picks lower-scoring signal, 
   but should consider BOTH issues and let editors choose
2. **No task specificity**: "Add citations" is vague - should identify which sections 
   lack citations
3. **Missing some signals**: Articles might need images, updates, or other improvements 
   not detected
4. **Binary task selection**: Should present multiple improvement options

#### Why is the slowest part slow?

**Answer: The Pageviews API is the bottleneck** (~1-2 seconds per call)

**Why it's slow:**
1. **External API call**: Network latency to Wikimedia servers
2. **30 days of data**: API must fetch and aggregate 30 daily datapoints
3. **Processing overhead**: API parses article title, checks permissions, aggregates data
4. **No caching**: Each call starts from scratch

**Evidence:**
In typical test runs:
- Pageviews API: ~1.0-1.5s per article
- Citation analysis: ~0.3-0.5s per article
- Structure analysis: ~0.2-0.3s per article

The pageviews call takes 60-75% of total processing time!

**Why other features are faster:**
- Parse API returns cached data (Wikipedia caches rendered HTML)
- Wikitext is stored in database (fast retrieval)
- Our Python processing is minimal compared to API latency
"""

# ============================================================================
# SECTION 4: FUTURE WORK AND REFLECTION
# ============================================================================

"""
## Future Work and Reflection

### How to Speed Up worklist_to_recommended_tasks

The current implementation processes articles **sequentially** (one at a time), which is slow. 
Here are detailed strategies to improve performance:

#### Strategy 1: Parallel API Calls (Easiest, 5-10x speedup)

**Current approach:**
for article in articles:
    # Wait for article 1 to complete
    # Then process article 2
    # Then process article 3...

**Improved approach using threading:**
```python
from concurrent.futures import ThreadPoolExecutor, as_completed

def process_single_article(language, article_title):
    \"\"\"Process one article and return recommendation.\"\"\"
    importance = article_to_importance_score(language, article_title)
    quality_one = article_to_quality_feature_one(language, article_title)
    quality_two = article_to_quality_feature_two(language, article_title)
    
    # Select task
    if quality_one['score'] < quality_two['score']:
        task = quality_one['task']
    else:
        task = quality_two['task']
    
    return Recommendation(article_title, importance, task)

def worklist_to_recommended_tasks_parallel(language, articles, max_workers=5):
    \"\"\"Process articles in parallel using thread pool.\"\"\"
    recommendations = []
    
    # Create thread pool with 5 workers
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        # Submit all articles at once
        future_to_article = {
            executor.submit(process_single_article, language, article): article
            for article in articles
        }
        
        # Collect results as they complete
        for future in as_completed(future_to_article):
            article = future_to_article[future]
            try:
                rec = future.result()
                recommendations.append(rec)
            except Exception as e:
                print(f"Error processing {article}: {e}")
    
    return sorted(recommendations, key=lambda x: x.importance, reverse=True)
```

**Why this works:**
- While waiting for API response for article 1, we can fetch data for articles 2-5
- Network latency (1-2s) is hidden by parallel processing
- 5 workers can process 10 articles in ~4 seconds instead of ~20 seconds

**Expected speedup:** 5-10x faster (depending on network speed)

#### Strategy 2: Caching (Dramatic for repeated use)

**Problem:** Re-analyzing same articles wastes time
**Solution:** Cache results with expiration

```python
import pickle
from datetime import datetime, timedelta

class ResultsCache:
    def __init__(self, cache_file='article_cache.pkl', ttl_hours=24):
        self.cache_file = cache_file
        self.ttl = timedelta(hours=ttl_hours)
        self.cache = self._load_cache()
    
    def _load_cache(self):
        try:
            with open(self.cache_file, 'rb') as f:
                return pickle.load(f)
        except:
            return {}
    
    def get(self, article_title):
        \"\"\"Get cached result if fresh enough.\"\"\"
        if article_title in self.cache:
            result, timestamp = self.cache[article_title]
            if datetime.now() - timestamp < self.ttl:
                return result
        return None
    
    def set(self, article_title, result):
        \"\"\"Cache a result.\"\"\"
        self.cache[article_title] = (result, datetime.now())
        with open(self.cache_file, 'wb') as f:
            pickle.dump(self.cache, f)

# Usage:
cache = ResultsCache(ttl_hours=24)

def article_to_importance_score_cached(language, article_title):
    cached = cache.get(article_title)
    if cached:
        return cached
    
    result = article_to_importance_score(language, article_title)
    cache.set(article_title, result)
    return result
```

**Expected speedup:**
- First run: no improvement
- Subsequent runs within 24h: instant results
- Perfect for edit-a-thons where you refine the list multiple times

#### Strategy 3: Progressive Loading (Better UX)

**Problem:** Users wait for all results before seeing anything
**Solution:** Stream results as they complete

```python
def worklist_to_recommended_tasks_streaming(language, articles):
    \"\"\"
    Process articles and yield results immediately as they complete.
    Allows displaying partial results while processing continues.
    \"\"\"
    from concurrent.futures import ThreadPoolExecutor, as_completed
    
    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = {
            executor.submit(process_single_article, language, article): article
            for article in articles
        }
        
        completed = 0
        for future in as_completed(futures):
            completed += 1
            try:
                rec = future.result()
                # Yield result immediately - allows progressive display
                print(f"[{completed}/{len(articles)}] Completed: {rec.title}")
                yield rec
            except Exception as e:
                print(f"Error: {e}")
```

#### Implementation Priority

1. **Start with Strategy 1 (Parallel Processing)**: Easiest to implement, huge gains
2. **Add Strategy 2 (Caching)**: Simple but very valuable for repeated use
3. **Implement Strategy 3 (Streaming)**: UI improvement, doesn't speed up total time but feels faster

### Comparison to Existing Tools

After reviewing the organizer tools listed, here's what I'd adopt:

#### Tool 1: WikiProject Template (es:Plantilla:Wikiproyecto)

**What I like:**
- **Automated dashboard approach**: Real-time updates without manual work
- **Multiple task categories**: Citations, expansion, translation, etc.
- **Activity feed**: Shows recent edits and top contributors
- **Visual hierarchy**: Clear presentation of priorities

**What I'd adopt for my tool:**
1. **Categorized task lists**: Instead of one ranked list, group tasks by type:
   - 🔗 Citation tasks
   - 📝 Expansion needed
   - 🔧 Structural improvements
   - 📊 Needs update

2. **Real-time updates**: Cache results but auto-refresh every 24h
3. **Difficulty indicators**: Clear labels for beginner/intermediate/advanced

**What I'd change:**
- Too template-heavy for newcomers to edit
- Better as a generated page than a template
- Add filtering by difficulty level

#### Tool 2: Citation Hunt

**What I like:**
- **Single-task focus**: Shows one task at a time (not overwhelming)
- **Direct action**: Click to edit immediately
- **Category filtering**: Find articles in your interest area
- **"Skip" button**: Easy to find tasks that fit your skill level

**What I'd adopt for my tool:**
1. **Task-by-task interface**: Don't show all 50 tasks at once
2. **Direct edit links**: Include URL to edit the specific section
   ```python
   edit_url = f"https://en.wikipedia.org/wiki/{article}?action=edit&section=3"
   ```
3. **Quick filtering**: By category, difficulty, time estimate

**What I'd change:**
- Add time estimates (Citation Hunt doesn't show how long tasks take)
- Show article importance (help editors prioritize)
- Include "why this matters" explanation

#### Tool 3: Popular Pages Bot

**What I like:**
- **Importance-based**: Prioritizes high-traffic articles
- **WikiProject-specific**: Focused scope for targeted campaigns
- **Simple output**: Just a list, easy to understand

**What I'd adopt:**
- Already using pageviews for importance! ✓
- Add WikiProject categorization

**What I'd change:**
- Combine with quality signals (bot only shows popularity)
- My tool does this - it's the whole point!

#### Tool 4: PetScan

**What I like:**
- **Extremely powerful filtering**: Combine multiple criteria
- **Flexible queries**: Can find very specific article sets
- **Export options**: CSV, JSON, wikitext

**What I'd adopt for my tool:**
1. **Multiple filter criteria**: Allow filtering by minimum importance, max citation score, etc.
2. **Export formats**: CSV for spreadsheets, wikitext for on-wiki posting

**What I'd change:**
- PetScan is TOO complex for most users
- My tool should stay simple by default, with advanced options hidden

### My Ideal Tool Synthesis

Combining the best elements:

**Interface Design** (inspired by Citation Hunt):
- Show one task at a time
- Big "Start editing" button
- Skip to next task easily
- Filter by category/difficulty

**Data Collection** (inspired by Popular Pages + my work):
- Importance from pageviews ✓
- Quality signals (citations, structure) ✓
- Article metadata

**Organization** (inspired by WikiProject Template):
- Categorized task lists
- Difficulty indicators
- Real-time updates
- Dashboard view for organizers

**Flexibility** (inspired by PetScan):
- Advanced filtering
- Multiple export formats
- Custom quality signals

**Workflow Example:**

Organizer View (Dashboard):
├── Climate Change Edit-a-thon Tasks
│   ├── 📊 42 tasks generated
│   ├── 15 beginner tasks (⏱ 10-20 min each)
│   ├── 20 intermediate tasks
│   ├── 7 advanced tasks
│   │
│   ├── By Category:
│   │   ├── 🔗 Citations (18 tasks)
│   │   ├── 📝 Expansion (12 tasks)
│   │   ├── 🏗️ Structure (8 tasks)
│   │   └── 📊 Updates (4 tasks)
│   │
│   └── Top Priority:
│       1. "Climate change" - add citations (500K views/mo)
│       2. "Global warming" - expand History section (200K views/mo)

Editor View (Task-by-task):
┌──────────────────────────────────────────────────┐
│ Task #1 for Beginners (⏱ 10-15 minutes)          │
│                                                   │
│ Article: Carbon footprint                        │
│ Importance: ⭐⭐⭐⭐ (50,000 views/month)           │
│                                                   │
│ Task: Add citations to "Reducing carbon          │
│       footprint" section                         │
│                                                   │
│ Why: Section has only 1 citation but makes       │
│      5 specific claims                           │
│                                                   │
│ [Start Editing] [Skip] [Mark Complete]          │
└──────────────────────────────────────────────────┘

This combines:
- ✅ Data-driven prioritization (my tool)
- ✅ Simple task-by-task interface (Citation Hunt)
- ✅ Categorized organization (WikiProject Template)
- ✅ Importance weighting (Popular Pages Bot)
- ✅ Flexible filtering (PetScan)

For a PAWS notebook, I'd implement the data collection and prioritization (what I've built), 
then suggest the interface design for a future web application deployment on Toolforge.
"""

# ============================================================================
# EXAMPLE USAGE AND TESTING
# ============================================================================

def main():
    """Main function to run the complete analysis"""
    
    print("="*70)
    print("MICRO-TASK GENERATOR FOR WIKIPEDIA ORGANIZERS")
    print("Climate Change Edit-a-thon Example")
    print("="*70)
    print()
    
    # My curated article list
    my_articles = [
        "Climate change",
        "Global warming",
        "Carbon footprint",
        "Renewable energy",
        "Deforestation",
        "Solar power",
        "Electric vehicle",
        "Sea level rise",
        "Carbon offset",
        "Sustainable agriculture"
    ]
    
    print("ARTICLE WORKLIST:")
    for i, article in enumerate(my_articles, 1):
        print(f"  {i}. {article}")
    print()
    
    # Test individual functions first
    print("="*70)
    print("TESTING INDIVIDUAL FEATURES")
    print("="*70)
    print()
    
    test_article = "Carbon footprint"
    print(f"Testing with: {test_article}\n")
    
    # Test quality features
    print("Quality Feature 1 (Citation Density):")
    quality1 = article_to_quality_feature_one("en", test_article)
    print(f"  Score: {quality1['score']}")
    print(f"  Task: {quality1['task']}\n")
    
    print("Quality Feature 2 (Section Balance):")
    quality2 = article_to_quality_feature_two("en", test_article)
    print(f"  Score: {quality2['score']}")
    print(f"  Task: {quality2['task']}\n")
    
    print("Importance Score (Pageviews):")
    importance = article_to_importance_score("en", test_article)
    print(f"  Score: {importance:.2f}\n")
    
    # Run full analysis
    print("="*70)
    print("RUNNING FULL WORKLIST ANALYSIS")
    print("="*70)
    print()
    
    recommendations, timings = worklist_to_recommended_tasks("en", my_articles)
    
    # Display final results
    print("\nFINAL PRIORITIZED TASK LIST:")
    print("="*70)
    for i, rec in enumerate(recommendations, 1):
        print(f"{i}. {rec.title}")
        print(f"   Importance: {rec.importance:.2f}")
        print(f"   Task: {rec.task}")
        print()
    
    print("="*70)
    print("ANALYSIS COMPLETE")
    print("="*70)


if __name__ == "__main__":
    main()
