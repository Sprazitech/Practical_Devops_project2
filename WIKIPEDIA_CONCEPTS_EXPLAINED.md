# Wikipedia & MediaWiki Concepts for Complete Beginners

## 🌍 Understanding Wikipedia for Your Micro-Task Generator

This guide explains Wikipedia concepts you'll encounter while building your micro-task generator. Everything is explained assuming zero prior knowledge!

---

## Part 1: Wikipedia Basics

### What is Wikipedia?
Wikipedia is a free online encyclopedia that anyone can edit. Unlike traditional encyclopedias:
- **Collaborative**: Thousands of volunteers contribute
- **Open**: Anyone can read and edit (with some protections)
- **Massive**: 6+ million articles in English alone
- **Maintained by volunteers**: No paid staff writing articles

### Why Do We Need Task Generators?
**The Problem**: Wikipedia is huge and constantly needs improvements
- New articles need citations
- Links break over time
- Information becomes outdated
- Finding what needs work is hard

**Your Solution**: Automatically identify specific, small tasks that:
- New editors can complete easily
- Improve article quality systematically
- Help campaign organizers plan editing events

---

## Part 2: Wikipedia Structure

### Articles
The basic unit of Wikipedia. Each article:
- Has a unique title (e.g., "Python (programming language)")
- Contains text, images, infoboxes, and references
- Belongs to categories
- Has a history of all edits
- Is written in "wikitext" (Wikipedia's markup language)

**Example**: The article "Climate change" contains:
- Introduction paragraph (lead section)
- Multiple sections (Causes, Effects, etc.)
- References (citations)
- External links
- Categories (Climate change, Environmental issues, etc.)

### Categories
Wikipedia's organizational system. Think of them as:
- **Folders** that group related articles
- **Tags** that describe article topics
- **Hierarchical**: Categories can contain subcategories

**Examples**:
- Category:Machine learning
- Category:African history
- Category:Living people

**Why they matter for you**:
- You'll analyze all articles in a category together
- Good for WikiProject campaigns
- Helps identify article scope and importance

### Templates
Reusable pieces of code inserted into articles. Two main types:

#### 1. **Informational Templates** (don't indicate problems)
- `{{Infobox}}` - Information boxes on the right side
- `{{Cite web}}` - Formatted citations
- `{{Main}}` - Links to main articles

#### 2. **Maintenance Templates** (🎯 THESE ARE YOUR GOLDMINE!)
- `{{Citation needed}}` - Missing references
- `{{Dead link}}` - Broken external link
- `{{Expand section}}` - Section needs more content
- `{{Update}}` - Information is outdated
- `{{Cleanup}}` - Formatting issues

**Why they matter for you**:
Maintenance templates are explicit signals that Wikipedia editors have identified problems. Your generator should definitely create tasks for these!

### Sections
Articles are divided into sections:
- **Lead section**: Introductory paragraphs (no heading)
- **Content sections**: Main body (History, Description, etc.)
- **References section**: Where citations appear
- **External links section**: Related websites
- **See also section**: Related articles

**Quality indicators**:
- Articles with < 3 sections are usually stubs (need expansion)
- Well-developed articles have 8-15+ sections
- Missing references section = major problem

### Citations and References
Wikipedia's credibility depends on verifiable sources:
- **Citation**: Link to a reliable source backing up a claim
- **Reference**: The actual source (book, website, journal)
- **Inline citation**: Citation next to a specific fact

**Formats you'll see**:
```wiki
<ref>Source information</ref>          # Basic reference
{{cite web |url=... |title=...}}       # Formatted web citation
{{sfn|Author|Year|p=123}}              # Short footnote
```

**Why they matter for you**:
Articles need citations to be trustworthy. Your generator should:
- Count citations per section
- Identify sections without citations
- Flag articles with citation needed templates

---

## Part 3: Technical Concepts

### MediaWiki
The software that runs Wikipedia. Think of it as:
- **Content Management System**: Stores and serves Wikipedia content
- **Platform**: Powers many wikis, not just Wikipedia
- **Open Source**: Anyone can see and use the code

**For you**: You'll interact with MediaWiki through its API

### MediaWiki API
A way for programs (like yours!) to access Wikipedia data.

**What it does**:
- Fetches article content and metadata
- Returns data in a structured format (JSON)
- Lets you search, query, and analyze without scraping

**Analogy**: Like a drive-through window
- You make a request (order food)
- MediaWiki processes it (kitchen makes food)
- You get a response (receive food)

**Types of MediaWiki APIs**:
1. **Action API**: The main, powerful API
   - URL: `https://en.wikipedia.org/w/api.php`
   - Very flexible, can do almost anything
   - Returns nested JSON
   
2. **REST API**: Modern, simplified API
   - URL: `https://en.wikipedia.org/api/rest_v1/`
   - Easier to use, more structured
   - Less flexible

3. **Pageviews API**: Traffic statistics
   - URL: `https://wikimedia.org/api/rest_v1/`
   - Shows how many people view each article
   - Helps prioritize important articles

### API Requests
How you ask MediaWiki for data:

**Components**:
1. **Endpoint**: The URL you're calling
2. **Action**: What you want to do (`query`, `parse`, etc.)
3. **Parameters**: Specifics of your request
4. **Format**: How you want the response (`json`, `xml`)

**Example request**:
```
https://en.wikipedia.org/w/api.php?
  action=query              # I want to query for information
  &titles=Python            # About the article "Python"
  &prop=info                # Specifically, basic info
  &format=json              # Return as JSON
```

**Example response** (simplified):
```json
{
  "query": {
    "pages": {
      "23862": {
        "pageid": 23862,
        "title": "Python (programming language)",
        "length": 73492,
        "watchers": 156
      }
    }
  }
}
```

### JSON (JavaScript Object Notation)
A way to structure data that both humans and computers can read.

**Structure**:
- `{}` = Object/Dictionary (key-value pairs)
- `[]` = Array/List
- Keys in quotes: `"name": "value"`

**Example**:
```json
{
  "article": "Python",
  "sections": 12,
  "citations": 145,
  "tasks": [
    {"type": "Add citations", "priority": "High"},
    {"type": "Fix dead links", "priority": "Medium"}
  ]
}
```

**Why it matters**:
All API responses come as JSON. You'll need to:
- Parse JSON to get the data you need
- Navigate nested structures
- Extract specific values

**In Python**:
```python
import json

# Parse JSON string
data = json.loads(json_string)

# Access nested data
title = data['query']['pages']['123']['title']

# Pretty print
print(json.dumps(data, indent=2))
```

---

## Part 4: Quality Metrics

### Article Length
Measured in bytes (characters).

**Rough guidelines**:
- < 1,000 bytes: Stub (very short)
- 1,000-5,000: Short article
- 5,000-20,000: Standard article
- 20,000-50,000: Long article
- 50,000+: Very comprehensive

**Why it matters**:
Short articles likely need expansion. Include in your task generator!

### Watchers
Number of Wikipedia editors who have an article on their watchlist.

**What it indicates**:
- High watchers (50+) = Important article with active maintainers
- Low watchers (< 10) = May be neglected
- Zero watchers = Might have quality issues

**Why it matters**:
- High-watched articles should be prioritized (more people will see improvements)
- Low-watched articles might need attention

### Page Views
How many times an article is viewed per day/month.

**What it indicates**:
- High views = Many readers affected by quality
- Low views = Specialized topic, less urgent

**Why it matters**:
Use to prioritize tasks! Fixing a highly-viewed article helps more people.

**How to get it**:
```python
# Pageviews API
url = f"https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/en.wikipedia/all-access/all-agents/{article}/daily/{start_date}/{end_date}"
```

### Citation Density
Citations per section (or per 1000 bytes).

**What it indicates**:
- < 1 citation/section: Poor (likely needs citations)
- 1-2 citations/section: Fair
- 2-5 citations/section: Good
- 5+ citations/section: Excellent

**Why it matters**:
Wikipedia's core policy is verifiability. Low citation density = high priority task!

---

## Part 5: WikiProjects and Campaigns

### WikiProjects
Groups of editors focused on specific topics.

**Examples**:
- WikiProject Medicine
- WikiProject Africa
- WikiProject Women in Red
- WikiProject Computer Science

**What they do**:
- Maintain articles in their topic area
- Organize editing campaigns
- Create task lists for editors
- Set quality standards

**Why it matters for you**:
Your task generator helps WikiProjects by:
- Automatically finding work that needs doing
- Prioritizing tasks for campaigns
- Making it easier for new editors to contribute

### Editing Campaigns
Organized events where many editors work together.

**Types**:
- **Edit-a-thons**: In-person editing events (libraries, conferences)
- **Online campaigns**: Virtual editing drives
- **Contests**: Wikipedia editing competitions
- **Awareness months**: Focused on specific topics

**Your role**:
Campaign organizers need:
- Lists of articles needing work
- Specific, actionable tasks
- Tasks sorted by difficulty
- Time estimates

**Your micro-task generator provides exactly this!**

---

## Part 6: Practical Examples

### Example 1: Analyzing Article Quality

Let's analyze "Climate change":

**Basic info**:
```python
{
  'title': 'Climate change',
  'length': 84532,  # Long article
  'watchers': 423,   # Highly watched
  'sections': 23     # Very comprehensive
}
```

**Interpretation**:
- ✅ Long, comprehensive article
- ✅ Many editors watching
- ⚠️ But need to check citations and maintenance templates

**Citations**:
```python
{
  'total_citations': 512,
  'sections': 23,
  'citations_per_section': 22.3,  # Excellent!
  'quality': 'Excellent'
}
```

**Interpretation**:
- ✅ Very well-cited
- ✅ No citation tasks needed

**Maintenance templates found**:
```python
['Template:Update section', 'Template:Dead link']
```

**Generated tasks**:
1. **Update Section** (Priority: Medium)
   - Some sections have outdated information
2. **Fix Dead Links** (Priority: High)
   - At least one external link is broken

### Example 2: Comparing Two Articles

**Article A: "Python (programming language)"**
- Length: 73,492 bytes ✅ Comprehensive
- Sections: 18 ✅ Well-structured
- Citations/section: 8.5 ✅ Excellent
- Watchers: 156 ✅ Active community
- Tasks: 2 (minor updates only)

**Article B: "List of Python software"**
- Length: 4,213 bytes ⚠️ Short
- Sections: 4 ⚠️ Limited structure
- Citations/section: 0.8 ❌ Poor
- Watchers: 12 ⚠️ Few maintainers
- Tasks: 5 (add citations, expand, improve structure)

**Campaign recommendation**:
Focus on Article B for beginner editors:
- Clear improvement opportunities
- Lower risk (less-watched article)
- Multiple types of tasks to learn from

---

## Part 7: Common Patterns in Your Code

### Pattern 1: Making an API Call
```python
def get_data(article_title):
    url = "https://en.wikipedia.org/w/api.php"
    
    params = {
        'action': 'query',
        'titles': article_title,
        'format': 'json'
        # ... other parameters
    }
    
    response = requests.get(url, params=params)
    data = response.json()
    
    return data
```

### Pattern 2: Navigating Nested JSON
```python
# Get the page data
pages = data['query']['pages']
page_id = list(pages.keys())[0]

# Check if article exists
if page_id == '-1':
    return None

# Extract information
page_data = pages[page_id]
title = page_data['title']
length = page_data['length']
```

### Pattern 3: Analyzing and Deciding
```python
def generate_task_if_needed(article_data):
    tasks = []
    
    # Check citation coverage
    if article_data['citations_per_section'] < 2:
        tasks.append({
            'type': 'Add citations',
            'priority': 'High',
            'reason': 'Poor citation coverage'
        })
    
    # Check article length
    if article_data['length'] < 5000:
        tasks.append({
            'type': 'Expand article',
            'priority': 'Medium',
            'reason': 'Short article'
        })
    
    return tasks
```

### Pattern 4: Bulk Processing
```python
def analyze_many_articles(article_list):
    results = []
    
    for article in article_list:
        # Analyze each article
        data = analyze_article(article)
        results.append(data)
        
        # Be nice to servers
        time.sleep(0.5)
    
    # Convert to DataFrame
    df = pd.DataFrame(results)
    return df
```

---

## Part 8: Glossary

Quick reference for terms you'll encounter:

**Wikipedia Terms**:
- **Article**: A Wikipedia page about a topic
- **Edit**: A change to an article
- **Revision**: A saved version of an article
- **Diff**: Comparison between two revisions
- **Stub**: Very short article needing expansion
- **Vandalism**: Destructive edits
- **Patrol**: Checking recent edits for problems
- **Watchlist**: Articles an editor monitors

**Technical Terms**:
- **API**: Application Programming Interface (how programs talk to each other)
- **Endpoint**: Specific URL for an API function
- **Parameter**: Setting/option in an API request
- **JSON**: Data format (like a structured text document)
- **HTTP Request**: Asking a server for data
- **Response**: Server's reply to your request
- **Timeout**: Request took too long, failed
- **Rate limiting**: Server limits how fast you can make requests

**Data Analysis Terms**:
- **DataFrame**: Table-like data structure in pandas
- **Metric**: Measurable value (length, citations, etc.)
- **Threshold**: Cutoff point for decisions
- **Distribution**: How values spread across a dataset
- **Correlation**: Whether two values tend to change together
- **Outlier**: Data point very different from others

**Task Terms**:
- **Micro-task**: Small, specific improvement task
- **Priority**: How important/urgent a task is
- **Difficulty**: How hard a task is for editors
- **Campaign**: Organized editing effort
- **WikiProject**: Group maintaining a topic area

---

## Part 9: Debugging Tips

### Common API Issues

**Issue**: Article not found
```python
# Response:
{'query': {'pages': {'-1': {'missing': ''}}}}
```
**Fix**: Check spelling, article name is case-sensitive

**Issue**: Nested key error
```python
KeyError: 'categories'
```
**Fix**: Not all articles have all fields
```python
categories = page_data.get('categories', [])  # Returns [] if missing
```

**Issue**: Too many requests
```python
# Error: 429 Too Many Requests
```
**Fix**: Add delays
```python
import time
time.sleep(0.5)  # Wait between requests
```

### Debugging Strategy

1. **Print the full response**:
```python
print(json.dumps(data, indent=2))
```

2. **Check step by step**:
```python
print("Step 1: Got data")
print(f"Keys: {data.keys()}")
print("Step 2: Accessing query")
print(f"Query keys: {data['query'].keys()}")
```

3. **Test with known good articles**:
- "Python (programming language)" - long, well-maintained
- "Main Page" - guaranteed to exist
- Start simple, then try edge cases

---

## Part 10: Success Mindset

### What Makes a Good Micro-Task Generator?

**Technical Excellence**:
- ✅ Handles errors gracefully
- ✅ Makes efficient API calls
- ✅ Produces accurate analysis
- ✅ Generates actionable tasks

**User-Focused**:
- ✅ Tasks are specific and clear
- ✅ Prioritization makes sense
- ✅ Difficulty levels help matching to editors
- ✅ Time estimates are realistic

**Well-Documented**:
- ✅ Code is easy to understand
- ✅ Explanations are beginner-friendly
- ✅ Results are interpreted thoughtfully
- ✅ Shows awareness of limitations

### Your Unique Value

You bring fresh eyes to Wikipedia analysis!
- **New perspective**: You see things experienced editors might miss
- **Beginner empathy**: You understand new editor challenges
- **Creative ideas**: Your approach might be different (and better!)

### Remember

This isn't about being perfect. It's about:
- **Learning**: Showing you can master new APIs and concepts
- **Communication**: Explaining complex ideas simply
- **Problem-solving**: Tackling challenges creatively
- **Growth mindset**: Iterating and improving

---

## 🎯 Quick Reference: Most Important Concepts

If you only remember 10 things:

1. **Maintenance templates = direct task signals**
2. **Citations are critical for Wikipedia credibility**
3. **API responses are nested JSON (navigate carefully)**
4. **Priority = impact + effort + urgency**
5. **Categories group articles by topic**
6. **Sections < 3 usually means stub article**
7. **Be nice to servers (add delays)**
8. **High page views = higher task priority**
9. **WikiProjects organize topic areas**
10. **Document everything for beginners!**

---

## 📚 Learn More

### Official Documentation
- MediaWiki API: https://www.mediawiki.org/wiki/API:Main_page
- Wikipedia Policies: https://en.wikipedia.org/wiki/Wikipedia:Policies_and_guidelines
- WikiProjects: https://en.wikipedia.org/wiki/Wikipedia:WikiProject

### Tutorials
- API Sandbox (try queries): https://en.wikipedia.org/wiki/Special:ApiSandbox
- Python Requests: https://requests.readthedocs.io/
- Pandas: https://pandas.pydata.org/docs/getting_started/intro_tutorials/

### Community
- Wikipedia Village Pump: https://en.wikipedia.org/wiki/Wikipedia:Village_pump
- Outreachy task comments: Help other applicants!

---

**You now have all the conceptual knowledge you need!** 🎉

Go build an amazing micro-task generator and show the mentors what you can do!

---

*Created for Outreachy December 2025 Applicants*
*Last updated: 2025-10-09*
