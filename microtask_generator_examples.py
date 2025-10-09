"""
Micro-Task Generator - Code Examples
Outreachy December 2025 Application

This file contains working code examples for the Micro-Task Generator notebook.
Copy and adapt these functions into your PAWS Jupyter notebook.

Author: Outreachy Applicant
Date: 2025-10-09
"""

import requests
import json
import pandas as pd
from datetime import datetime, timedelta
import time

# ============================================================================
# PART 1: BASIC API INTERACTIONS
# ============================================================================

def get_article_basic_info(article_title):
    """
    Fetches basic information about a Wikipedia article.
    
    This is your first API call! It gets:
    - Page ID (unique identifier)
    - Article length (in bytes)
    - Last modified date
    - Number of watchers
    
    Parameters:
        article_title (str): The exact title of the Wikipedia article
        
    Returns:
        dict: Article information or None if article doesn't exist
        
    Example:
        info = get_article_basic_info("Python (programming language)")
        print(f"Article length: {info['length']} bytes")
    """
    url = "https://en.wikipedia.org/w/api.php"
    
    params = {
        'action': 'query',
        'titles': article_title,
        'prop': 'info',
        'inprop': 'watchers',
        'format': 'json'
    }
    
    try:
        response = requests.get(url, params=params, timeout=10)
        data = response.json()
        
        # Navigate the nested JSON structure
        pages = data.get('query', {}).get('pages', {})
        page_id = list(pages.keys())[0]
        
        # Check if article exists
        if page_id == '-1' or 'missing' in pages[page_id]:
            print(f"❌ Article '{article_title}' not found")
            return None
        
        page_data = pages[page_id]
        
        return {
            'title': page_data.get('title'),
            'pageid': page_data.get('pageid'),
            'length': page_data.get('length'),
            'watchers': page_data.get('watchers', 0),
            'touched': page_data.get('touched')
        }
        
    except Exception as e:
        print(f"⚠️  Error fetching article: {e}")
        return None


def get_article_categories(article_title):
    """
    Gets all categories an article belongs to.
    
    Categories help organize Wikipedia and indicate article topics.
    They're useful for:
    - Understanding article context
    - Finding similar articles
    - Determining WikiProject membership
    
    Parameters:
        article_title (str): Article name
        
    Returns:
        list: Category names (without "Category:" prefix)
    """
    url = "https://en.wikipedia.org/w/api.php"
    
    params = {
        'action': 'query',
        'titles': article_title,
        'prop': 'categories',
        'cllimit': 'max',  # Get all categories
        'format': 'json'
    }
    
    response = requests.get(url, params=params)
    data = response.json()
    
    pages = data.get('query', {}).get('pages', {})
    page_id = list(pages.keys())[0]
    
    if page_id == '-1':
        return []
    
    categories = []
    if 'categories' in pages[page_id]:
        for cat in pages[page_id]['categories']:
            # Remove "Category:" prefix for cleaner display
            cat_name = cat['title'].replace('Category:', '')
            categories.append(cat_name)
    
    return categories


# ============================================================================
# PART 2: ANALYZING ARTICLE QUALITY
# ============================================================================

def get_maintenance_templates(article_title):
    """
    Identifies maintenance templates (issue flags) in an article.
    
    Maintenance templates are Wikipedia's way of flagging problems:
    - {{Citation needed}} → Missing references
    - {{Dead link}} → Broken external links  
    - {{Expand section}} → Needs more content
    - {{Update}} → Information is outdated
    
    These templates are GOLD for generating micro-tasks!
    
    Parameters:
        article_title (str): Article name
        
    Returns:
        list: Template names found in the article
    """
    url = "https://en.wikipedia.org/w/api.php"
    
    params = {
        'action': 'query',
        'titles': article_title,
        'prop': 'templates',
        'tllimit': 'max',
        'format': 'json'
    }
    
    response = requests.get(url, params=params)
    data = response.json()
    
    pages = data.get('query', {}).get('pages', {})
    page_id = list(pages.keys())[0]
    
    templates = []
    if page_id != '-1' and 'templates' in pages[page_id]:
        for template in pages[page_id]['templates']:
            templates.append(template['title'])
    
    return templates


def filter_maintenance_templates(all_templates):
    """
    Filters a template list to find only maintenance/cleanup templates.
    
    Most articles have many templates (infoboxes, navboxes, etc.).
    We only care about maintenance templates that indicate problems.
    
    Parameters:
        all_templates (list): All template names from an article
        
    Returns:
        dict: Maintenance templates grouped by type
    """
    # Keywords that indicate maintenance templates
    maintenance_keywords = {
        'citation': ['citation', 'cite', 'verify', 'ref'],
        'expansion': ['expand', 'stub', 'incomplete', 'section'],
        'cleanup': ['cleanup', 'improve', 'rewrite'],
        'update': ['update', 'dated', 'current'],
        'links': ['dead link', 'broken', 'link rot']
    }
    
    categorized = {
        'citation': [],
        'expansion': [],
        'cleanup': [],
        'update': [],
        'links': [],
        'other': []
    }
    
    for template in all_templates:
        template_lower = template.lower()
        
        categorized_flag = False
        for category, keywords in maintenance_keywords.items():
            if any(keyword in template_lower for keyword in keywords):
                categorized[category].append(template)
                categorized_flag = True
                break
        
        if not categorized_flag:
            categorized['other'].append(template)
    
    # Remove empty categories
    return {k: v for k, v in categorized.items() if v}


def analyze_article_structure(article_title):
    """
    Analyzes the structure of an article (sections, links, etc.).
    
    Structure analysis helps identify:
    - Stub articles (few sections)
    - Missing components (no references section)
    - Potential link issues (many external links might have dead ones)
    
    Parameters:
        article_title (str): Article name
        
    Returns:
        dict: Structural information
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
    
    if 'error' in data:
        print(f"⚠️  Error: {data['error']['info']}")
        return None
    
    parse_data = data.get('parse', {})
    
    sections = parse_data.get('sections', [])
    section_names = [s['line'] for s in sections]
    
    return {
        'total_sections': len(sections),
        'section_names': section_names,
        'external_links_count': len(parse_data.get('externallinks', [])),
        'external_links': parse_data.get('externallinks', []),
        'categories_count': len(parse_data.get('categories', [])),
        'has_references_section': any('reference' in s.lower() for s in section_names)
    }


def estimate_citation_coverage(article_title):
    """
    Estimates how well-cited an article is.
    
    This is a rough estimate based on counting citation markers in the wikitext.
    Better articles have more citations distributed throughout.
    
    Parameters:
        article_title (str): Article name
        
    Returns:
        dict: Citation statistics
    """
    url = "https://en.wikipedia.org/w/api.php"
    
    params = {
        'action': 'parse',
        'page': article_title,
        'prop': 'wikitext|sections',
        'format': 'json'
    }
    
    response = requests.get(url, params=params)
    data = response.json()
    
    if 'error' in data:
        return None
    
    parse_data = data.get('parse', {})
    wikitext = parse_data.get('wikitext', {}).get('*', '')
    sections = parse_data.get('sections', [])
    
    # Count different types of citations
    ref_tags = wikitext.count('<ref')  # <ref> tags
    cite_templates = wikitext.count('{{cite')  # {{cite web}}, {{cite book}}, etc.
    sfn_templates = wikitext.count('{{sfn')  # Short footnote citations
    
    total_citations = ref_tags + cite_templates + sfn_templates
    
    # Calculate density
    sections_count = len(sections) if sections else 1
    citations_per_section = total_citations / sections_count
    
    # Categorize citation quality
    if citations_per_section < 1:
        quality = "Poor"
    elif citations_per_section < 2:
        quality = "Fair"
    elif citations_per_section < 5:
        quality = "Good"
    else:
        quality = "Excellent"
    
    return {
        'total_citations': total_citations,
        'sections': sections_count,
        'citations_per_section': round(citations_per_section, 2),
        'quality': quality,
        'needs_citations': citations_per_section < 2
    }


# ============================================================================
# PART 3: GENERATING MICRO-TASKS
# ============================================================================

def generate_tasks_from_article(article_title):
    """
    Main function: Generates prioritized micro-tasks for an article.
    
    This combines all analysis functions to create actionable tasks
    that editors can complete to improve the article.
    
    Parameters:
        article_title (str): Article to analyze
        
    Returns:
        list: Prioritized tasks with metadata
    """
    print(f"🔍 Analyzing '{article_title}'...\n")
    
    tasks = []
    
    # Gather all data
    basic_info = get_article_basic_info(article_title)
    structure = analyze_article_structure(article_title)
    citations = estimate_citation_coverage(article_title)
    all_templates = get_maintenance_templates(article_title)
    maint_templates = filter_maintenance_templates(all_templates)
    
    if not basic_info or not structure:
        print("❌ Could not analyze article")
        return tasks
    
    # Task 1: Check citation coverage
    if citations and citations['needs_citations']:
        tasks.append({
            'id': 1,
            'type': 'Add Citations',
            'priority': 'High',
            'difficulty': 'Beginner',
            'description': f"Article has only {citations['citations_per_section']} citations per section (target: >2). Add reliable sources to improve verifiability.",
            'estimated_time': '15-30 minutes',
            'reason': f"Citation quality: {citations['quality']}",
            'tags': ['citations', 'verifiability']
        })
    
    # Task 2: Address maintenance templates
    if 'citation' in maint_templates:
        for template in maint_templates['citation'][:3]:  # Top 3
            tasks.append({
                'id': len(tasks) + 1,
                'type': 'Fix Citation Issues',
                'priority': 'High',
                'difficulty': 'Beginner',
                'description': f"Template '{template}' indicates missing or problematic citations. Add reliable sources.",
                'estimated_time': '10-20 minutes',
                'reason': 'Flagged by Wikipedia editors',
                'tags': ['template', 'citations']
            })
    
    if 'links' in maint_templates:
        tasks.append({
            'id': len(tasks) + 1,
            'type': 'Fix Dead Links',
            'priority': 'High',
            'difficulty': 'Beginner',
            'description': f"Article has dead link templates. Replace with working sources or use archive.org.",
            'estimated_time': '5-15 minutes per link',
            'reason': 'Dead links reduce article reliability',
            'tags': ['links', 'maintenance']
        })
    
    # Task 3: Check for stub/expansion needs
    if structure['total_sections'] < 3:
        tasks.append({
            'id': len(tasks) + 1,
            'type': 'Expand Article',
            'priority': 'Medium',
            'difficulty': 'Intermediate',
            'description': f"Article only has {structure['total_sections']} sections. Consider adding more content.",
            'estimated_time': '1-2 hours',
            'reason': 'Appears to be a stub article',
            'tags': ['expansion', 'content']
        })
    
    if 'expansion' in maint_templates:
        tasks.append({
            'id': len(tasks) + 1,
            'type': 'Expand Sections',
            'priority': 'Medium',
            'difficulty': 'Intermediate',
            'description': f"Expansion templates found: {', '.join(maint_templates['expansion'][:2])}",
            'estimated_time': '30-60 minutes',
            'reason': 'Sections flagged as needing expansion',
            'tags': ['expansion', 'template']
        })
    
    # Task 4: Check references section
    if not structure['has_references_section'] and citations and citations['total_citations'] > 0:
        tasks.append({
            'id': len(tasks) + 1,
            'type': 'Add References Section',
            'priority': 'Medium',
            'difficulty': 'Beginner',
            'description': "Article has citations but no dedicated References section. Add one for better organization.",
            'estimated_time': '5-10 minutes',
            'reason': 'Standard Wikipedia structure',
            'tags': ['structure', 'formatting']
        })
    
    # Task 5: Check for many external links (potential dead links)
    if structure['external_links_count'] > 20:
        tasks.append({
            'id': len(tasks) + 1,
            'type': 'Verify External Links',
            'priority': 'Medium',
            'difficulty': 'Beginner',
            'description': f"Article has {structure['external_links_count']} external links. Check for and fix any dead links.",
            'estimated_time': '20-40 minutes',
            'reason': 'High link count increases chance of dead links',
            'tags': ['links', 'maintenance']
        })
    
    # Task 6: Update old content
    if 'update' in maint_templates:
        tasks.append({
            'id': len(tasks) + 1,
            'type': 'Update Content',
            'priority': 'Medium',
            'difficulty': 'Intermediate',
            'description': "Article flagged as needing updates. Review and update outdated information.",
            'estimated_time': '30-60 minutes',
            'reason': 'Content may be outdated',
            'tags': ['update', 'accuracy']
        })
    
    # Sort by priority
    priority_order = {'High': 0, 'Medium': 1, 'Low': 2}
    tasks.sort(key=lambda x: priority_order.get(x['priority'], 3))
    
    # Re-number tasks after sorting
    for i, task in enumerate(tasks, 1):
        task['id'] = i
    
    return tasks


def format_tasks_output(article_title, tasks):
    """
    Formats tasks in a readable way for display.
    
    Parameters:
        article_title (str): Article name
        tasks (list): Generated tasks
    """
    print("=" * 70)
    print(f"MICRO-TASKS FOR: {article_title}")
    print("=" * 70)
    
    if not tasks:
        print("✅ No issues found! Article appears to be in good shape.")
        return
    
    print(f"\nFound {len(tasks)} tasks:\n")
    
    for task in tasks:
        priority_emoji = {
            'High': '🔴',
            'Medium': '🟡',
            'Low': '🟢'
        }.get(task['priority'], '⚪')
        
        difficulty_emoji = {
            'Beginner': '👶',
            'Intermediate': '👤',
            'Advanced': '🎓'
        }.get(task['difficulty'], '')
        
        print(f"{priority_emoji} Task #{task['id']}: {task['type']}")
        print(f"   Priority: {task['priority']} | Difficulty: {task['difficulty']} {difficulty_emoji}")
        print(f"   Time: {task['estimated_time']}")
        print(f"   Description: {task['description']}")
        print(f"   Reason: {task['reason']}")
        print(f"   Tags: {', '.join(task['tags'])}")
        print()


# ============================================================================
# PART 4: BULK ANALYSIS FOR CAMPAIGNS
# ============================================================================

def get_category_articles(category, limit=50):
    """
    Gets articles from a Wikipedia category.
    
    This is useful for WikiProject campaigns where you want to analyze
    all articles in a specific topic area.
    
    Parameters:
        category (str): Category name (without "Category:" prefix)
        limit (int): Maximum number of articles to fetch
        
    Returns:
        list: Article titles
    """
    url = "https://en.wikipedia.org/w/api.php"
    
    params = {
        'action': 'query',
        'list': 'categorymembers',
        'cmtitle': f'Category:{category}',
        'cmlimit': min(limit, 500),  # API max is 500
        'cmtype': 'page',  # Only pages, not subcategories
        'format': 'json'
    }
    
    response = requests.get(url, params=params)
    data = response.json()
    
    if 'query' not in data:
        print(f"❌ Category '{category}' not found")
        return []
    
    members = data['query'].get('categorymembers', [])
    articles = [member['title'] for member in members]
    
    print(f"✅ Found {len(articles)} articles in category '{category}'")
    return articles


def analyze_multiple_articles(articles, delay=0.5):
    """
    Analyzes multiple articles and compiles results.
    
    Parameters:
        articles (list): List of article titles
        delay (float): Seconds to wait between API calls (be nice to servers!)
        
    Returns:
        DataFrame: Analysis results for all articles
    """
    results = []
    
    print(f"🚀 Analyzing {len(articles)} articles...\n")
    
    for i, article in enumerate(articles, 1):
        print(f"[{i}/{len(articles)}] {article}...")
        
        basic_info = get_article_basic_info(article)
        structure = analyze_article_structure(article)
        citations = estimate_citation_coverage(article)
        tasks = generate_tasks_from_article(article)
        
        if basic_info and structure and citations:
            results.append({
                'Article': article,
                'Length (bytes)': basic_info['length'],
                'Watchers': basic_info['watchers'],
                'Sections': structure['total_sections'],
                'External Links': structure['external_links_count'],
                'Total Citations': citations['total_citations'],
                'Citations/Section': citations['citations_per_section'],
                'Citation Quality': citations['quality'],
                'Tasks Generated': len(tasks),
                'High Priority Tasks': sum(1 for t in tasks if t['priority'] == 'High'),
                'Beginner Tasks': sum(1 for t in tasks if t['difficulty'] == 'Beginner')
            })
        
        # Be nice to Wikipedia's servers
        time.sleep(delay)
    
    df = pd.DataFrame(results)
    return df


def generate_campaign_summary(df):
    """
    Creates a summary report for campaign organizers.
    
    Parameters:
        df (DataFrame): Results from analyze_multiple_articles()
    """
    if df.empty:
        print("No data to summarize")
        return
    
    print("\n" + "=" * 70)
    print("CAMPAIGN SUMMARY REPORT")
    print("=" * 70)
    
    total_articles = len(df)
    articles_with_tasks = (df['Tasks Generated'] > 0).sum()
    total_tasks = df['Tasks Generated'].sum()
    total_high_priority = df['High Priority Tasks'].sum()
    total_beginner = df['Beginner Tasks'].sum()
    
    print(f"\n📊 Overview:")
    print(f"   • Total articles analyzed: {total_articles}")
    print(f"   • Articles needing work: {articles_with_tasks} ({articles_with_tasks/total_articles*100:.1f}%)")
    print(f"   • Total tasks generated: {total_tasks}")
    print(f"   • High priority tasks: {total_high_priority}")
    print(f"   • Beginner-friendly tasks: {total_beginner}")
    
    print(f"\n📈 Statistics:")
    print(f"   • Average article length: {df['Length (bytes)'].mean():.0f} bytes")
    print(f"   • Average sections per article: {df['Sections'].mean():.1f}")
    print(f"   • Average citations per section: {df['Citations/Section'].mean():.2f}")
    print(f"   • Average tasks per article: {df['Tasks Generated'].mean():.1f}")
    
    print(f"\n🎯 Top Priority Articles (most tasks):")
    top_articles = df.nlargest(5, 'Tasks Generated')[['Article', 'Tasks Generated', 'High Priority Tasks']]
    for idx, row in top_articles.iterrows():
        print(f"   • {row['Article']}: {row['Tasks Generated']} tasks ({row['High Priority Tasks']} high priority)")
    
    print(f"\n📚 Citation Quality Distribution:")
    quality_counts = df['Citation Quality'].value_counts()
    for quality, count in quality_counts.items():
        print(f"   • {quality}: {count} articles ({count/total_articles*100:.1f}%)")
    
    print(f"\n💡 Recommendations:")
    
    poor_citations = df[df['Citation Quality'] == 'Poor']
    if len(poor_citations) > 0:
        print(f"   • {len(poor_citations)} articles have poor citation coverage - prioritize for citation campaigns")
    
    many_links = df[df['External Links'] > 20]
    if len(many_links) > 0:
        print(f"   • {len(many_links)} articles have >20 external links - check for dead links")
    
    short_articles = df[df['Sections'] < 3]
    if len(short_articles) > 0:
        print(f"   • {len(short_articles)} articles are stubs - good for expansion campaigns")
    
    print()


# ============================================================================
# EXAMPLE USAGE
# ============================================================================

if __name__ == "__main__":
    print("="*70)
    print("MICRO-TASK GENERATOR - EXAMPLES")
    print("="*70)
    print()
    
    # Example 1: Analyze a single article
    print("EXAMPLE 1: Single Article Analysis")
    print("-" * 70)
    article = "Python (programming language)"
    tasks = generate_tasks_from_article(article)
    format_tasks_output(article, tasks)
    
    print("\n" + "="*70 + "\n")
    
    # Example 2: Analyze articles from a category
    print("EXAMPLE 2: Category Campaign Analysis")
    print("-" * 70)
    category = "Machine learning"
    articles = get_category_articles(category, limit=5)
    
    if articles:
        df = analyze_multiple_articles(articles[:5])  # Analyze first 5
        print("\n📊 Results Table:")
        print(df.to_string(index=False))
        
        generate_campaign_summary(df)
        
        # Save to CSV
        output_file = "campaign_analysis.csv"
        df.to_csv(output_file, index=False)
        print(f"\n💾 Results saved to: {output_file}")
    
    print("\n" + "="*70)
    print("✅ Examples completed!")
    print("="*70)
