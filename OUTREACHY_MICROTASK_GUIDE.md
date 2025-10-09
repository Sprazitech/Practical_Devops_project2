# Complete Guide to the Micro-Task Generator Notebook
## Outreachy Microtask - Beginner-Friendly Tutorial

---

## 📚 Table of Contents
1. [Understanding the Project](#understanding-the-project)
2. [Key Concepts for Beginners](#key-concepts-for-beginners)
3. [Step-by-Step Completion Guide](#step-by-step-completion-guide)
4. [MediaWiki API Basics](#mediawiki-api-basics)
5. [Data Analysis Tips](#data-analysis-tips)
6. [Documentation Best Practices](#documentation-best-practices)
7. [Common Issues and Solutions](#common-issues-and-solutions)

---

## 🎯 Understanding the Project

### What is a Micro-Task Generator?
A micro-task generator is a tool that automatically identifies small, actionable improvements needed in Wikipedia articles. Think of it as a smart to-do list creator for Wikipedia editors!

**Example micro-tasks:**
- "Add citations to the 'History' section"
- "Fix 3 dead links in references"
- "Add an infobox to this article"
- "Improve the lead section (it's too short)"

### Why is this important?
- **For organizers:** Reduces the manual work of finding tasks for editing campaigns
- **For new editors:** Provides clear, specific entry points to contribute
- **For Wikipedia:** Improves article quality systematically

---

## 🧠 Key Concepts for Beginners

### 1. **Jupyter Notebooks**
- **What:** Interactive documents that mix code, text, and visualizations
- **Cells:** Two main types:
  - **Code cells:** Write and run Python code
  - **Markdown cells:** Write formatted text, explanations, headers
- **How to run:** Press `Shift + Enter` to run a cell

### 2. **PAWS (PAWS: A Web Shell)**
- A Jupyter notebook environment specifically for Wikimedia projects
- Connected to Wikimedia databases and APIs
- Your work is automatically saved and shareable via public links

### 3. **MediaWiki API**
- **What:** A way to programmatically access Wikipedia data
- **Think of it as:** A messenger that fetches information from Wikipedia
- **Example:** Instead of visiting a Wikipedia page, you ask the API to send you the data

### 4. **REST APIs**
- **REST:** Representational State Transfer
- **In simple terms:** A standardized way for programs to request and receive data
- **Like ordering at a restaurant:** You make a request (order), receive a response (food)

### 5. **JSON (JavaScript Object Notation)**
- A format for structuring data
- Looks like nested dictionaries and lists in Python
- Easy for both humans and computers to read

### 6. **Maintenance Templates**
- Special Wikipedia templates that flag issues in articles
- Examples: `{{Citation needed}}`, `{{Dead link}}`, `{{Expand section}}`
- These are goldmines for finding micro-tasks!

---

## 📝 Step-by-Step Completion Guide

### Phase 1: Setup and Understanding (30 minutes)

#### Step 1: Open Your Notebook in PAWS
1. Go to https://hub-paws.wmcloud.org/
2. Navigate to your forked notebook
3. Read through ALL cells first to understand the structure

#### Step 2: Install Required Libraries
The notebook likely starts with imports. Common libraries you'll need:

```python
import requests  # For making API calls
import pandas as pd  # For data analysis
import json  # For handling JSON data
import matplotlib.pyplot as plt  # For visualizations
from datetime import datetime  # For working with dates
```

**Add a markdown cell explaining:**
```markdown
## Required Libraries
- **requests:** Allows us to communicate with the MediaWiki API
- **pandas:** Helps us organize and analyze data in tables (DataFrames)
- **json:** Converts API responses into Python-friendly formats
- **matplotlib:** Creates charts and graphs to visualize our findings
```

#### Step 3: Understanding the MediaWiki API

**Add a markdown cell:**
```markdown
## Understanding the MediaWiki API

The MediaWiki API is our gateway to Wikipedia data. We'll use two main endpoints:

1. **Action API:** For detailed page information, categories, templates
   - URL: https://en.wikipedia.org/w/api.php
   
2. **REST API:** For modern, streamlined data access
   - URL: https://en.wikipedia.org/api/rest_v1/

### API Request Structure
Every API call needs:
- **Endpoint:** The URL we're calling
- **Parameters:** What we're asking for (like form fields)
- **Format:** How we want the response (usually JSON)
```

---

### Phase 2: Fetching Article Data (60 minutes)

#### Step 4: Get Basic Article Information

**Add a code cell:**
```python
def get_article_info(article_title):
    """
    Fetches basic information about a Wikipedia article.
    
    Parameters:
    - article_title (str): The title of the Wikipedia article
    
    Returns:
    - dict: Article data including length, revision count, etc.
    """
    url = "https://en.wikipedia.org/w/api.php"
    
    # Parameters define what we want from the API
    params = {
        'action': 'query',        # We want to query for information
        'titles': article_title,  # The article we're interested in
        'prop': 'info|revisions', # We want info and revision data
        'inprop': 'watchers',     # Include number of watchers
        'format': 'json'          # Return data as JSON
    }
    
    # Make the request
    response = requests.get(url, params=params)
    data = response.json()
    
    return data

# Test it with an example article
article_data = get_article_info("Python (programming language)")
print(json.dumps(article_data, indent=2))
```

**Add a markdown cell explaining the output:**
```markdown
### Understanding the Response

The API returns a nested JSON structure. Key fields:
- **pageid:** Unique identifier for the page
- **title:** The article title
- **touched:** Last time the page was modified
- **length:** Article size in bytes (helpful for finding stub articles)
- **watchers:** Number of users monitoring the page (indicates importance)

**Task for you:** Run the cell above and identify these fields in the output.
```

#### Step 5: Extract Maintenance Templates

**Add a code cell:**
```python
def get_maintenance_templates(article_title):
    """
    Finds all maintenance templates in an article.
    These templates flag issues like 'Citation needed' or 'Dead link'.
    
    Returns:
    - list: Names of maintenance templates found
    """
    url = "https://en.wikipedia.org/w/api.php"
    
    params = {
        'action': 'query',
        'titles': article_title,
        'prop': 'templates',      # Get all templates used in the page
        'tllimit': 'max',         # Get all templates (not just first 10)
        'format': 'json'
    }
    
    response = requests.get(url, params=params)
    data = response.json()
    
    # Extract template names
    pages = data['query']['pages']
    page_id = list(pages.keys())[0]
    
    templates = []
    if 'templates' in pages[page_id]:
        for template in pages[page_id]['templates']:
            templates.append(template['title'])
    
    return templates

# Test with an article that likely has issues
templates = get_maintenance_templates("Climate change")
print(f"Found {len(templates)} templates")

# Filter for maintenance templates (they often contain certain keywords)
maintenance_keywords = ['citation', 'dead', 'cleanup', 'expand', 'stub', 'verify']
maintenance_templates = [t for t in templates if any(kw in t.lower() for kw in maintenance_keywords)]
print(f"Maintenance templates: {maintenance_templates}")
```

**Add explanation:**
```markdown
### Why Maintenance Templates Matter

Maintenance templates are **direct indicators** of needed improvements. They're manually added by editors who identified problems.

**Common maintenance templates and what they mean:**
- `{{Citation needed}}` → Add references
- `{{Dead link}}` → Fix broken external links
- `{{Expand section}}` → Add more content to a section
- `{{Update}}` → Information is outdated
- `{{Cleanup}}` → Formatting or structure issues

**Your task:** Modify the code above to count how many of each type of maintenance template appears.
```

---

### Phase 3: Analyzing Article Quality (60 minutes)

#### Step 6: Get Article Metadata

**Add a code cell:**
```python
def get_article_metadata(article_title):
    """
    Gathers comprehensive metadata about an article for quality assessment.
    
    Returns:
    - dict: Metadata including references, sections, links, etc.
    """
    url = "https://en.wikipedia.org/w/api.php"
    
    params = {
        'action': 'parse',
        'page': article_title,
        'prop': 'sections|externallinks|categories',
        'format': 'json'
    }
    
    response = requests.get(url, params=params)
    data = response.json()
    
    if 'parse' not in data:
        return None
    
    metadata = {
        'title': article_title,
        'sections': len(data['parse']['sections']),
        'external_links': len(data['parse']['externallinks']),
        'categories': len(data['parse']['categories'])
    }
    
    return metadata

# Test with multiple articles
test_articles = [
    "Python (programming language)",
    "Climate change",
    "Artificial intelligence"
]

metadata_list = []
for article in test_articles:
    meta = get_article_metadata(article)
    if meta:
        metadata_list.append(meta)
        print(f"{article}: {meta['sections']} sections, {meta['external_links']} external links")
```

**Add explanation:**
```markdown
### Quality Signals in Metadata

Different metrics tell us about article quality:

1. **Number of sections:** 
   - Few sections (< 3) → Likely a stub, needs expansion
   - Many sections (> 10) → Comprehensive, but check for citation needs

2. **External links:**
   - Few links (< 5) → May need more references
   - Many links (> 50) → Check for dead links

3. **Categories:**
   - Few categories (< 3) → Poor categorization
   - Good categorization helps readers find related articles

**Exercise:** Create a simple "quality score" function that rates articles 1-10 based on these metrics.
```

#### Step 7: Identify Citation Gaps

**Add a code cell:**
```python
def analyze_citations(article_title):
    """
    Analyzes citation coverage in an article.
    Identifies sections that may need citations.
    """
    url = "https://en.wikipedia.org/w/api.php"
    
    # Get the article's wikitext (raw Wikipedia markup)
    params = {
        'action': 'parse',
        'page': article_title,
        'prop': 'wikitext|sections',
        'format': 'json'
    }
    
    response = requests.get(url, params=params)
    data = response.json()
    
    if 'parse' not in data:
        return None
    
    wikitext = data['parse']['wikitext']['*']
    sections = data['parse']['sections']
    
    # Count citation templates (rough estimate)
    # Common citation formats: <ref>, {{cite web}}, {{cite book}}, etc.
    ref_count = wikitext.count('<ref')
    cite_count = wikitext.count('{{cite')
    total_citations = ref_count + cite_count
    
    # Calculate citations per section
    citations_per_section = total_citations / len(sections) if sections else 0
    
    return {
        'title': article_title,
        'total_citations': total_citations,
        'sections': len(sections),
        'citations_per_section': round(citations_per_section, 2),
        'needs_citations': citations_per_section < 2  # Arbitrary threshold
    }

# Analyze multiple articles
for article in test_articles:
    result = analyze_citations(article)
    if result:
        print(f"\n{result['title']}:")
        print(f"  Total citations: {result['total_citations']}")
        print(f"  Citations per section: {result['citations_per_section']}")
        print(f"  Needs more citations: {result['needs_citations']}")
```

**Add explanation:**
```markdown
### Why Citation Analysis Matters

Citations are the backbone of Wikipedia's reliability. Well-cited articles:
- Build trust with readers
- Allow fact-checking
- Follow Wikipedia's "Verifiability" policy

**Rule of thumb:**
- < 1 citation per section → Likely needs citations
- 1-3 citations per section → Moderate coverage
- > 3 citations per section → Well-referenced

**Note:** This is a rough estimate. A better approach would analyze section-by-section.

**Challenge:** Extend this function to check each section individually and report which specific sections lack citations.
```

---

### Phase 4: Generating Prioritized Tasks (90 minutes)

#### Step 8: Create a Task Priority System

**Add a markdown cell:**
```markdown
## Task Prioritization Strategy

Not all tasks are equal! We need to prioritize based on:

1. **Impact:** How much will this improve the article?
2. **Effort:** How easy is this for a new editor?
3. **Urgency:** Is this blocking other improvements?

### Priority Levels:
- **High:** Easy tasks with high impact (add citations, fix dead links)
- **Medium:** Moderate effort tasks (expand sections, add images)
- **Low:** Complex tasks (major rewrites, technical content)
```

**Add a code cell:**
```python
def generate_micro_tasks(article_title):
    """
    Generates and prioritizes micro-tasks for an article.
    
    Returns:
    - list of dicts: Each task with title, description, priority, difficulty
    """
    tasks = []
    
    # Get article data
    metadata = get_article_metadata(article_title)
    templates = get_maintenance_templates(article_title)
    citations = analyze_citations(article_title)
    
    if not metadata or not citations:
        return tasks
    
    # Task 1: Check for citation needs
    if citations['needs_citations']:
        tasks.append({
            'type': 'Add Citations',
            'description': f'Article has only {citations["citations_per_section"]} citations per section. Add reliable sources.',
            'priority': 'High',
            'difficulty': 'Beginner',
            'estimated_time': '15-30 minutes'
        })
    
    # Task 2: Check for dead links (if many external links)
    if metadata['external_links'] > 20:
        tasks.append({
            'type': 'Fix Dead Links',
            'description': f'Article has {metadata["external_links"]} external links. Check and fix any dead links.',
            'priority': 'High',
            'difficulty': 'Beginner',
            'estimated_time': '20-40 minutes'
        })
    
    # Task 3: Check for stub status
    if metadata['sections'] < 3:
        tasks.append({
            'type': 'Expand Article',
            'description': f'Article only has {metadata["sections"]} sections. Consider adding more content.',
            'priority': 'Medium',
            'difficulty': 'Intermediate',
            'estimated_time': '1-2 hours'
        })
    
    # Task 4: Check maintenance templates
    for template in templates:
        template_lower = template.lower()
        if 'citation' in template_lower:
            tasks.append({
                'type': 'Add Citations',
                'description': f'Template "{template}" found. Add citations to flagged content.',
                'priority': 'High',
                'difficulty': 'Beginner',
                'estimated_time': '10-20 minutes'
            })
        elif 'dead link' in template_lower:
            tasks.append({
                'type': 'Fix Dead Link',
                'description': f'Dead link(s) identified. Replace with working sources.',
                'priority': 'High',
                'difficulty': 'Beginner',
                'estimated_time': '5-15 minutes'
            })
        elif 'expand' in template_lower:
            tasks.append({
                'type': 'Expand Content',
                'description': f'Template "{template}" indicates section needs expansion.',
                'priority': 'Medium',
                'difficulty': 'Intermediate',
                'estimated_time': '30-60 minutes'
            })
    
    return tasks

# Test the task generator
for article in test_articles:
    print(f"\n{'='*60}")
    print(f"MICRO-TASKS FOR: {article}")
    print('='*60)
    
    tasks = generate_micro_tasks(article)
    
    if not tasks:
        print("✓ Article appears to be in good shape!")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"\n{i}. {task['type']} [{task['priority']} Priority]")
            print(f"   Description: {task['description']}")
            print(f"   Difficulty: {task['difficulty']}")
            print(f"   Estimated time: {task['estimated_time']}")
```

**Add explanation:**
```markdown
### Understanding Task Prioritization

Our system prioritizes tasks based on:

1. **Beginner-friendly + High impact = High priority**
   - Example: Adding citations, fixing dead links
   
2. **Moderate effort + Moderate impact = Medium priority**
   - Example: Expanding sections, adding images

3. **Complex tasks = Lower priority** (for experienced editors)
   - Example: Major restructuring, technical rewrites

**Why this approach?**
- New editors can contribute immediately
- High-impact tasks improve article quality quickly
- Organizers can assign tasks based on editor experience

**Reflection question:** What other factors might influence task priority? (Hint: article popularity, recent edits, WikiProject importance)
```

---

### Phase 5: Data Analysis and Visualization (60 minutes)

#### Step 9: Analyze Multiple Articles

**Add a code cell:**
```python
def analyze_wikiproject_articles(category, limit=20):
    """
    Analyzes multiple articles from a Wikipedia category.
    Useful for WikiProject campaign planning.
    
    Parameters:
    - category: Wikipedia category name
    - limit: Maximum number of articles to analyze
    
    Returns:
    - DataFrame: Analysis results for all articles
    """
    url = "https://en.wikipedia.org/w/api.php"
    
    # Get articles in category
    params = {
        'action': 'query',
        'list': 'categorymembers',
        'cmtitle': f'Category:{category}',
        'cmlimit': limit,
        'cmtype': 'page',  # Only articles, not subcategories
        'format': 'json'
    }
    
    response = requests.get(url, params=params)
    data = response.json()
    
    if 'query' not in data or 'categorymembers' not in data['query']:
        print(f"Category '{category}' not found or has no articles")
        return None
    
    articles = [member['title'] for member in data['query']['categorymembers']]
    
    # Analyze each article
    results = []
    for article in articles[:limit]:
        print(f"Analyzing: {article}...")
        
        metadata = get_article_metadata(article)
        citations = analyze_citations(article)
        templates = get_maintenance_templates(article)
        tasks = generate_micro_tasks(article)
        
        if metadata and citations:
            results.append({
                'Article': article,
                'Sections': metadata['sections'],
                'External Links': metadata['external_links'],
                'Categories': metadata['categories'],
                'Citations': citations['total_citations'],
                'Citations per Section': citations['citations_per_section'],
                'Maintenance Templates': len(templates),
                'Generated Tasks': len(tasks),
                'High Priority Tasks': sum(1 for t in tasks if t['priority'] == 'High')
            })
    
    # Convert to DataFrame for easy analysis
    df = pd.DataFrame(results)
    return df

# Example: Analyze articles from a WikiProject
# Choose a category with manageable size
df = analyze_wikiproject_articles('Machine learning', limit=10)

if df is not None:
    print("\n" + "="*60)
    print("ANALYSIS SUMMARY")
    print("="*60)
    print(df.to_string())
    
    print("\n" + "="*60)
    print("STATISTICS")
    print("="*60)
    print(df.describe())
```

**Add explanation:**
```markdown
### Interpreting the Analysis

The DataFrame shows us patterns across multiple articles:

**Key metrics to look at:**
- **Articles with most tasks:** These need immediate attention
- **Articles with most high-priority tasks:** Best for new editors
- **Average citations per section:** Indicates overall category health
- **Correlation:** Do articles with more sections have more citations? (They should!)

**Exercise:** Calculate the correlation between:
1. Number of sections and number of citations
2. Number of external links and number of maintenance templates

Use: `df[['Sections', 'Citations']].corr()`
```

#### Step 10: Visualize the Data

**Add a code cell:**
```python
import matplotlib.pyplot as plt
import numpy as np

def visualize_analysis(df):
    """
    Creates visualizations of the article analysis.
    """
    if df is None or df.empty:
        print("No data to visualize")
        return
    
    # Create a figure with multiple subplots
    fig, axes = plt.subplots(2, 2, figsize=(15, 12))
    fig.suptitle('Wikipedia Article Analysis Dashboard', fontsize=16, fontweight='bold')
    
    # Plot 1: Tasks per article
    axes[0, 0].bar(range(len(df)), df['Generated Tasks'], color='steelblue')
    axes[0, 0].set_xlabel('Article Index')
    axes[0, 0].set_ylabel('Number of Tasks')
    axes[0, 0].set_title('Total Tasks Generated per Article')
    axes[0, 0].grid(axis='y', alpha=0.3)
    
    # Plot 2: High priority tasks
    axes[0, 1].bar(range(len(df)), df['High Priority Tasks'], color='coral')
    axes[0, 1].set_xlabel('Article Index')
    axes[0, 1].set_ylabel('High Priority Tasks')
    axes[0, 1].set_title('High Priority Tasks per Article')
    axes[0, 1].grid(axis='y', alpha=0.3)
    
    # Plot 3: Citations per section distribution
    axes[1, 0].hist(df['Citations per Section'], bins=10, color='mediumseaqueen', edgecolor='black')
    axes[1, 0].set_xlabel('Citations per Section')
    axes[1, 0].set_ylabel('Number of Articles')
    axes[1, 0].set_title('Distribution of Citation Density')
    axes[1, 0].axvline(2, color='red', linestyle='--', label='Minimum threshold')
    axes[1, 0].legend()
    
    # Plot 4: Sections vs Citations scatter
    axes[1, 1].scatter(df['Sections'], df['Citations'], alpha=0.6, s=100, color='purple')
    axes[1, 1].set_xlabel('Number of Sections')
    axes[1, 1].set_ylabel('Number of Citations')
    axes[1, 1].set_title('Sections vs Citations')
    axes[1, 1].grid(alpha=0.3)
    
    # Add trend line
    z = np.polyfit(df['Sections'], df['Citations'], 1)
    p = np.poly1d(z)
    axes[1, 1].plot(df['Sections'], p(df['Sections']), "r--", alpha=0.8, label='Trend')
    axes[1, 1].legend()
    
    plt.tight_layout()
    plt.show()
    
    print("\n" + "="*60)
    print("VISUALIZATION INSIGHTS")
    print("="*60)
    print(f"• Average tasks per article: {df['Generated Tasks'].mean():.1f}")
    print(f"• Articles needing attention: {(df['Generated Tasks'] > 0).sum()}")
    print(f"• Average citations per section: {df['Citations per Section'].mean():.2f}")
    print(f"• Articles below citation threshold: {(df['Citations per Section'] < 2).sum()}")

# Create visualizations
visualize_analysis(df)
```

**Add explanation:**
```markdown
### What the Visualizations Tell Us

1. **Tasks Bar Chart:**
   - Shows which articles need most work
   - Uniform heights → Category is generally healthy
   - Peaks → These articles need immediate attention

2. **High Priority Tasks:**
   - Identifies best articles for new editor campaigns
   - High bars = easy entry points for contributors

3. **Citation Distribution:**
   - Normal distribution → Most articles are similar quality
   - Skewed left → Many articles need citations
   - Skewed right → Category is well-referenced

4. **Sections vs Citations Scatter:**
   - Positive correlation → Longer articles have more citations (good!)
   - Outliers below trend → Need citations despite being long
   - Outliers above trend → Very well-referenced articles

**Question to reflect on:** If you were organizing an editing campaign, which articles would you assign to new editors based on these visualizations?
```

---

### Phase 6: Building the Task Generator (Final Phase)

#### Step 11: Create a Complete Task Generation System

**Add a code cell:**
```python
class WikiTaskGenerator:
    """
    A complete micro-task generator for Wikipedia articles.
    
    This class encapsulates all functionality for analyzing articles
    and generating prioritized tasks for editors.
    """
    
    def __init__(self):
        self.base_url = "https://en.wikipedia.org/w/api.php"
        self.task_history = []
    
    def analyze_article(self, article_title):
        """
        Comprehensive analysis of a single article.
        """
        print(f"🔍 Analyzing: {article_title}...")
        
        analysis = {
            'title': article_title,
            'metadata': self._get_metadata(article_title),
            'templates': self._get_templates(article_title),
            'citations': self._analyze_citations(article_title),
            'pageviews': self._get_pageviews(article_title)
        }
        
        return analysis
    
    def _get_metadata(self, article_title):
        """Helper: Get article metadata"""
        # Implementation here (use previous functions)
        return get_article_metadata(article_title)
    
    def _get_templates(self, article_title):
        """Helper: Get maintenance templates"""
        return get_maintenance_templates(article_title)
    
    def _analyze_citations(self, article_title):
        """Helper: Analyze citations"""
        return analyze_citations(article_title)
    
    def _get_pageviews(self, article_title):
        """
        Get article pageviews (popularity metric).
        Higher pageviews = higher priority for improvements.
        """
        # Simplified version - in real implementation, use Pageviews API
        # For now, return mock data
        import random
        return random.randint(100, 10000)
    
    def generate_tasks(self, article_title, include_reasoning=True):
        """
        Generate prioritized micro-tasks for an article.
        
        Parameters:
        - article_title: Article to analyze
        - include_reasoning: Include explanation for each task
        
        Returns:
        - list: Prioritized tasks with metadata
        """
        analysis = self.analyze_article(article_title)
        tasks = generate_micro_tasks(article_title)
        
        # Add popularity weighting
        pageviews = analysis['pageviews']
        for task in tasks:
            if pageviews > 5000:
                task['priority_note'] = '⭐ High-traffic article - increased priority'
            
            if include_reasoning:
                task['reasoning'] = self._explain_task(task, analysis)
        
        # Sort by priority
        priority_order = {'High': 0, 'Medium': 1, 'Low': 2}
        tasks.sort(key=lambda x: priority_order.get(x['priority'], 3))
        
        self.task_history.append({
            'article': article_title,
            'timestamp': datetime.now(),
            'tasks_generated': len(tasks)
        })
        
        return tasks
    
    def _explain_task(self, task, analysis):
        """
        Provide reasoning for why this task was generated.
        """
        reasoning = f"Based on analysis: "
        
        if task['type'] == 'Add Citations':
            cit_per_section = analysis['citations']['citations_per_section']
            reasoning += f"Article has {cit_per_section:.1f} citations per section (target: >2)."
        
        return reasoning
    
    def generate_campaign_tasks(self, category, max_articles=20):
        """
        Generate tasks for an entire editing campaign.
        
        Returns:
        - DataFrame: Tasks organized by article and priority
        """
        print(f"🚀 Generating campaign tasks for: {category}\n")
        
        # Get articles from category
        df = analyze_wikiproject_articles(category, limit=max_articles)
        
        if df is None:
            return None
        
        # Generate tasks for all articles
        all_tasks = []
        for article in df['Article']:
            tasks = self.generate_tasks(article, include_reasoning=False)
            for task in tasks:
                all_tasks.append({
                    'Article': article,
                    'Task Type': task['type'],
                    'Priority': task['priority'],
                    'Difficulty': task['difficulty'],
                    'Estimated Time': task['estimated_time'],
                    'Description': task['description']
                })
        
        campaign_df = pd.DataFrame(all_tasks)
        
        print(f"\n✅ Generated {len(all_tasks)} tasks across {len(df)} articles")
        print(f"   - High priority: {(campaign_df['Priority'] == 'High').sum()}")
        print(f"   - Beginner-friendly: {(campaign_df['Difficulty'] == 'Beginner').sum()}")
        
        return campaign_df
    
    def export_tasks(self, tasks_df, filename='campaign_tasks.csv'):
        """
        Export tasks to CSV for campaign organizers.
        """
        if tasks_df is not None:
            tasks_df.to_csv(filename, index=False)
            print(f"\n💾 Tasks exported to: {filename}")
            return filename
        return None

# Initialize the generator
generator = WikiTaskGenerator()

# Example usage
print("="*60)
print("SINGLE ARTICLE ANALYSIS")
print("="*60)
tasks = generator.generate_tasks("Python (programming language)")
for i, task in enumerate(tasks, 1):
    print(f"\n{i}. {task['type']} [{task['priority']}]")
    print(f"   {task['description']}")
    if 'reasoning' in task:
        print(f"   Why: {task['reasoning']}")

print("\n" + "="*60)
print("CAMPAIGN GENERATION")
print("="*60)
campaign_tasks = generator.generate_campaign_tasks("Machine learning", max_articles=5)
if campaign_tasks is not None:
    print("\nFirst 10 tasks:")
    print(campaign_tasks.head(10).to_string())
    
    # Export
    generator.export_tasks(campaign_tasks)
```

**Add explanation:**
```markdown
### The Complete System

We've now built a complete micro-task generator! Here's what it does:

**Key Features:**
1. **Article Analysis:** Gathers all relevant data
2. **Task Generation:** Creates specific, actionable tasks
3. **Prioritization:** Sorts by impact and difficulty
4. **Campaign Support:** Handles multiple articles at once
5. **Export:** Saves results for campaign organizers

**How Campaign Organizers Would Use This:**
1. Specify a WikiProject or category
2. Generate tasks for all articles
3. Export to spreadsheet
4. Assign tasks to editors based on experience level
5. Track progress as tasks are completed

**For New Editors:**
- Filter for "Beginner" difficulty
- Sort by "Estimated Time" for quick wins
- Group by "Task Type" to learn one skill at a time

### Potential Enhancements
Think about these for your final notebook:
- ✅ Integration with more existing tools (Citation Hunt, PetScan)
- ✅ Real-time pageview data (Wikimedia Pageviews API)
- ✅ Check for broken external links (verify URLs)
- ✅ Identify missing infoboxes
- ✅ Suggest WikiProjects to notify
- ✅ Estimate impact score based on article importance

**Your task:** Choose ONE enhancement and implement it!
```

---

## 📊 Data Analysis Tips

### Working with DataFrames
```python
# Common operations
df.head()           # First 5 rows
df.describe()       # Statistical summary
df['column'].mean() # Average of a column
df.sort_values('column', ascending=False)  # Sort
df[df['column'] > 10]  # Filter rows
```

### Handling API Errors
```python
def safe_api_call(url, params):
    """
    Makes an API call with error handling.
    """
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()  # Raise exception for bad status codes
        return response.json()
    except requests.exceptions.Timeout:
        print("⚠️  Request timed out")
        return None
    except requests.exceptions.RequestException as e:
        print(f"⚠️  API error: {e}")
        return None
```

### Debugging Tips
1. **Print intermediate results:** Use `print(json.dumps(data, indent=2))`
2. **Check API responses:** Visit the API URL in your browser
3. **Use small datasets first:** Test with 3-5 articles before scaling up
4. **Add try-except blocks:** Handle errors gracefully

---

## 📝 Documentation Best Practices

### Good Documentation Includes:

1. **Headers and Structure**
```markdown
## Main Section
### Subsection
#### Sub-subsection
```

2. **Explaining "Why" Not Just "What"**
❌ Bad: "This code gets article data"
✅ Good: "We fetch article data from the MediaWiki API to identify quality issues"

3. **Code Comments**
```python
# Calculate citations per section as a quality metric
# Articles with < 2 citations per section typically need improvement
citations_per_section = total_citations / num_sections
```

4. **Results Interpretation**
After every analysis, add a markdown cell explaining:
- What do the numbers mean?
- What patterns do you see?
- What surprises you?
- What would you recommend?

5. **Visualizations**
Always include:
- Clear title
- Axis labels
- Legend (if needed)
- Caption explaining what to look for

---

## 🔧 Common Issues and Solutions

### Issue 1: API Returns Empty Data
**Problem:** `'pages': {'-1': {'missing': ''}}`
**Solution:** Article title is incorrect or doesn't exist
- Check spelling
- Use exact Wikipedia title (case-sensitive)
- Check if article has been deleted

### Issue 2: Rate Limiting
**Problem:** Too many API requests
**Solution:** Add delays between requests
```python
import time
time.sleep(0.5)  # Wait 0.5 seconds between requests
```

### Issue 3: JSON Parsing Errors
**Problem:** Can't access nested data
**Solution:** Print the structure first
```python
print(json.dumps(data, indent=2))
# Then navigate carefully: data['query']['pages']['123']['title']
```

### Issue 4: Large Categories Timing Out
**Problem:** Category has thousands of articles
**Solution:** Use pagination or limit results
```python
params = {
    'cmlimit': 50,  # Only get 50 articles
    # ... other params
}
```

---

## 🎯 Completion Checklist

Before submitting your notebook, ensure you have:

- [ ] **Code cells** for each major function
- [ ] **Markdown cells** explaining concepts for beginners
- [ ] **Comments** in your code
- [ ] **At least 3 visualizations** with interpretations
- [ ] **Tested with multiple articles** from different categories
- [ ] **Error handling** in API calls
- [ ] **A summary section** explaining your findings
- [ ] **Reflections** on what you learned
- [ ] **Ideas for future improvements**
- [ ] **Clear, readable code** following Python conventions
- [ ] **Proper attribution** if you used external resources

---

## 🚀 Final Tips for Success

1. **Start Simple:** Get one article working, then scale up
2. **Document as You Go:** Don't wait until the end
3. **Test Frequently:** Run cells to catch errors early
4. **Ask Questions:** Add "Note to mentors" if you're unsure
5. **Be Creative:** Add your own ideas and analyses
6. **Show Your Thinking:** Explain uncertainties and choices
7. **Compare Tools:** Reference the existing tools from the task description
8. **Think About Users:** How would a campaign organizer use this?

---

## 📚 Additional Resources

### MediaWiki API Documentation
- Action API: https://www.mediawiki.org/wiki/API:Main_page
- REST API: https://www.mediawiki.org/wiki/API:REST_API
- Pageviews API: https://wikitech.wikimedia.org/wiki/Analytics/AQS/Pageviews

### Python Libraries
- Requests: https://requests.readthedocs.io/
- Pandas: https://pandas.pydata.org/docs/
- Matplotlib: https://matplotlib.org/stable/tutorials/index.html

### Wikipedia Policies
- Verifiability: https://en.wikipedia.org/wiki/Wikipedia:Verifiability
- Citing sources: https://en.wikipedia.org/wiki/Wikipedia:Citing_sources
- WikiProjects: https://en.wikipedia.org/wiki/Wikipedia:WikiProject

---

## 🌟 Good Luck!

Remember: The mentors are looking for:
- Your ability to learn and adapt
- How you explain complex concepts simply
- Your code quality and documentation
- Creative problem-solving
- How you work with new data

**They are NOT expecting perfection!** Show your thinking, explain your challenges, and demonstrate growth. You've got this! 🎉

---

*Created for Outreachy December 2025 - Micro-Task Generator Project*
