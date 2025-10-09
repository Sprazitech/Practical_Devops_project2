# 📇 Micro-Task Generator Quick Reference Card

> Keep this open while working on your notebook!

---

## 🎯 Core API Endpoints

### Get Article Info
```python
url = "https://en.wikipedia.org/w/api.php"
params = {
    'action': 'query',
    'titles': 'Article_Name',
    'prop': 'info',
    'format': 'json'
}
response = requests.get(url, params=params)
```

### Get Templates
```python
params = {
    'action': 'query',
    'titles': 'Article_Name',
    'prop': 'templates',
    'format': 'json'
}
```

### Parse Article Structure
```python
params = {
    'action': 'parse',
    'page': 'Article_Name',
    'prop': 'sections|externallinks',
    'format': 'json'
}
```

### Get Category Members
```python
params = {
    'action': 'query',
    'list': 'categorymembers',
    'cmtitle': 'Category:Name',
    'cmlimit': 50,
    'format': 'json'
}
```

---

## 🔍 Navigating API Responses

### Standard Pattern
```python
response = requests.get(url, params=params)
data = response.json()

# Get the page data
pages = data['query']['pages']
page_id = list(pages.keys())[0]

# Check if exists
if page_id == '-1':
    print("Article not found")
else:
    page_data = pages[page_id]
    title = page_data['title']
```

### Safe Access
```python
# Use .get() to avoid KeyErrors
value = data.get('key', default_value)

# For nested structures
watchers = page_data.get('watchers', 0)
categories = page_data.get('categories', [])
```

---

## 📊 Quality Thresholds

### Article Length (bytes)
- ❌ < 1,000 = Stub
- ⚠️ 1,000-5,000 = Short
- ✅ 5,000-20,000 = Standard
- ⭐ 20,000+ = Comprehensive

### Citation Density (per section)
- ❌ < 1 = Poor
- ⚠️ 1-2 = Fair
- ✅ 2-5 = Good
- ⭐ 5+ = Excellent

### Sections
- ❌ < 3 = Likely stub
- ✅ 3-8 = Decent structure
- ⭐ 8+ = Well-developed

### Watchers
- ⚠️ < 10 = Low attention
- ✅ 10-50 = Moderate
- ⭐ 50+ = High importance

---

## ✅ Maintenance Templates to Watch

### High Priority (Easy Tasks)
- `{{Citation needed}}`
- `{{Dead link}}`
- `{{Verify source}}`
- `{{Fix}}`

### Medium Priority (Moderate Tasks)
- `{{Expand section}}`
- `{{Update}}`
- `{{Cleanup}}`
- `{{Improve}}`

### Stub Templates
- `{{Stub}}`
- `{{*-stub}}` (any stub variant)

---

## 🎨 Common Visualization Templates

### Bar Chart
```python
plt.figure(figsize=(10, 6))
plt.bar(df['Article'], df['Tasks'])
plt.xlabel('Articles')
plt.ylabel('Number of Tasks')
plt.title('Tasks Generated per Article')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
```

### Histogram
```python
plt.figure(figsize=(8, 6))
plt.hist(df['Citations/Section'], bins=10)
plt.xlabel('Citations per Section')
plt.ylabel('Number of Articles')
plt.title('Citation Density Distribution')
plt.axvline(2, color='r', linestyle='--', label='Threshold')
plt.legend()
plt.show()
```

### Scatter Plot
```python
plt.figure(figsize=(8, 6))
plt.scatter(df['Sections'], df['Citations'])
plt.xlabel('Number of Sections')
plt.ylabel('Number of Citations')
plt.title('Article Structure vs Citations')
plt.grid(alpha=0.3)
plt.show()
```

---

## 🏗️ Task Generation Template

```python
def generate_task(article_data):
    """Template for creating a task"""
    return {
        'id': 1,
        'type': 'Task Type',
        'priority': 'High|Medium|Low',
        'difficulty': 'Beginner|Intermediate|Advanced',
        'description': 'Clear, specific description',
        'estimated_time': '10-20 minutes',
        'reason': 'Why this task was generated',
        'tags': ['tag1', 'tag2']
    }
```

### Priority Guidelines
- **High**: Easy + High impact (citations, dead links)
- **Medium**: Moderate effort (expand sections, update)
- **Low**: Complex (major rewrites)

### Difficulty Guidelines
- **Beginner**: < 30 min, clear steps (add citation, fix link)
- **Intermediate**: 30-60 min, some research (expand section)
- **Advanced**: 60+ min, expertise needed (technical rewrite)

---

## 📝 Pandas Quick Reference

### Creating DataFrame
```python
df = pd.DataFrame(results)
```

### Basic Operations
```python
df.head()                    # First 5 rows
df.describe()                # Statistics
df['column'].mean()          # Average
df['column'].sum()           # Total
df['column'].max()           # Maximum
df.sort_values('col')        # Sort
df[df['col'] > 10]           # Filter
```

### Useful for Analysis
```python
# Count by category
df['Priority'].value_counts()

# Group by
df.groupby('Priority')['Tasks'].sum()

# Correlation
df[['Sections', 'Citations']].corr()

# Top N
df.nlargest(5, 'Tasks')
```

---

## 🐛 Debugging Checklist

### API Not Responding?
- [ ] Check internet connection
- [ ] Verify URL is correct
- [ ] Check article name spelling
- [ ] Add timeout: `requests.get(url, params, timeout=10)`

### KeyError?
- [ ] Print full response: `print(json.dumps(data, indent=2))`
- [ ] Use `.get()` for safe access
- [ ] Check if article exists (page_id != '-1')

### Empty Results?
- [ ] Article might not have that data
- [ ] Check if template filtering is too strict
- [ ] Verify category name is exact

### Code Runs Slow?
- [ ] Add delays: `time.sleep(0.5)`
- [ ] Reduce number of articles analyzed
- [ ] Process in batches

---

## 💡 Documentation Template

### For Each Code Cell, Add Markdown:

```markdown
## [Section Title]

### Purpose
[1-2 sentences: what this does]

### Why It Matters
[Explain importance]

### How It Works
[Break down the approach]

### Code Explanation
[Key parts of the code]

### Results Interpretation
[What we found and what it means]
```

---

## ⚡ Time-Saving Shortcuts

### Test with Known Articles
- "Python (programming language)" - comprehensive
- "Earth" - very long, well-cited
- "Climate change" - active, maintained
- Try smaller topics for stub examples

### Test Categories (manageable size)
- "Machine learning"
- "Python software"
- "Sustainable technologies"

### Reusable Code Blocks
```python
# Error handling wrapper
def safe_api_call(url, params):
    try:
        response = requests.get(url, params=params, timeout=10)
        return response.json()
    except Exception as e:
        print(f"Error: {e}")
        return None

# Progress indicator
for i, item in enumerate(items, 1):
    print(f"[{i}/{len(items)}] Processing {item}...")
    # ... do work ...
    time.sleep(0.5)
```

---

## 📋 Before Requesting Feedback

- [ ] `Kernel → Restart & Run All` succeeds
- [ ] No error messages
- [ ] All visualizations display correctly
- [ ] Markdown cells are complete
- [ ] Code is commented
- [ ] Results are interpreted
- [ ] Summary section written
- [ ] Public link works

---

## 🎓 Key Concepts Reminder

### Maintenance Templates → Direct Tasks
Templates like `{{Citation needed}}` are gold! They tell you exactly what needs fixing.

### Citations = Wikipedia Credibility
Low citations per section (<2) = high priority task

### Watchers + Views = Importance
High-traffic articles should be prioritized

### Task Characteristics
- **Specific**: "Add citation to History section"
- **Actionable**: Clear steps to complete
- **Measurable**: Can verify when done
- **Prioritized**: Based on impact and effort

---

## 🆘 When Stuck

### 5-Minute Rule
Stuck for 5+ minutes? Try:
1. Print intermediate values
2. Test with simpler data
3. Check API Sandbox
4. Reread error message carefully

### 30-Minute Rule
Still stuck after 30 minutes?
1. Search Stack Overflow
2. Ask in task comments
3. Review relevant guide section
4. Take a break and return

---

## 📈 Progress Tracker

```
Phase 1: Setup [___] 2h
Phase 2: Basic Functions [___] 3h
Phase 3: Core Implementation [___] 4h
Phase 4: Bulk Analysis [___] 4h
Phase 5: Visualizations [___] 3h
Phase 6: Documentation [___] 3h
Phase 7: Polish [___] 2h

Total: ___/21h
```

---

## 🎯 Success Metrics

Your notebook should:
- ✅ Generate 3-10 tasks per article
- ✅ Analyze 10+ articles successfully
- ✅ Have 3+ visualizations
- ✅ Include citation analysis
- ✅ Prioritize tasks logically
- ✅ Be understandable to beginners
- ✅ Show your thinking process

---

## 🔗 Essential Links

- **API Sandbox**: https://en.wikipedia.org/wiki/Special:ApiSandbox
- **PAWS**: https://hub-paws.wmcloud.org/
- **API Docs**: https://www.mediawiki.org/wiki/API:Main_page
- **Pandas Docs**: https://pandas.pydata.org/docs/
- **Matplotlib Gallery**: https://matplotlib.org/stable/gallery/

---

## 💬 Quick Markdown Syntax

```markdown
# Header 1
## Header 2
### Header 3

**bold**
*italic*
`code`

- Bullet point
1. Numbered list

[Link text](URL)

> Quote

| Table | Header |
|-------|--------|
| Cell  | Cell   |
```

---

## 🎉 Final Reminders

- **Save often**: PAWS auto-saves, but use Ctrl+S
- **Test frequently**: Don't write 100 lines before testing
- **Document as you go**: Easier than later
- **Be nice to servers**: Add `time.sleep(0.5)` in loops
- **Ask for help**: Task comments are your friend
- **Show your work**: Explain your thinking
- **Quality > quantity**: Better to do basics well

---

**Print this and keep it visible while coding!** 📌

*Quick Reference Card for Outreachy Microtask*
*Version 1.0 - 2025-10-09*
