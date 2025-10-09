# Micro-Task Generator Notebook - Completion Checklist

## 🚀 Quick Start: Your Action Plan

This checklist provides a beginner-friendly roadmap for completing the Outreachy microtask notebook. Follow these steps in order!

---

## Phase 1: Setup & Exploration (Day 1 - 2 hours)

### ✅ Access Your Notebook
- [ ] Log into PAWS: https://hub-paws.wmcloud.org/
- [ ] Navigate to your forked notebook
- [ ] Read through the entire notebook once (don't code yet, just read!)
- [ ] Make a copy as backup (File → Make a Copy)

### ✅ Understand the Structure
- [ ] Identify which cells are code vs markdown
- [ ] Note which cells are already complete
- [ ] List which cells you need to complete
- [ ] Write down questions you have

### ✅ Test the Environment
- [ ] Run the import cell to make sure libraries work
- [ ] Try a simple API call (copy from examples file)
- [ ] Print "Hello Wikipedia!" to test the environment

**Estimated time: 2 hours**

---

## Phase 2: Learn the Basics (Day 1-2 - 3 hours)

### ✅ Master the MediaWiki API
- [ ] Read: https://www.mediawiki.org/wiki/API:Main_page (skim, don't deep dive)
- [ ] Test the API in your browser: 
  ```
  https://en.wikipedia.org/w/api.php?action=query&titles=Python&format=json
  ```
- [ ] Understand the response structure (it's nested JSON)
- [ ] Copy the `get_article_basic_info()` function from examples
- [ ] Run it with your favorite Wikipedia article
- [ ] Add a markdown cell explaining what you learned

### ✅ Understand Maintenance Templates
- [ ] Visit a Wikipedia article with issues (try "List of common misconceptions")
- [ ] Find templates like {{Citation needed}}
- [ ] Click "Edit" to see how templates look in wikitext
- [ ] Copy the `get_maintenance_templates()` function
- [ ] Test it on 3 different articles
- [ ] Document: Which templates appear most often?

### ✅ Practice Data Analysis
- [ ] Copy the `analyze_article_structure()` function
- [ ] Run it on 5 articles of different sizes
- [ ] Create a simple table comparing the results
- [ ] Add interpretation: What patterns do you see?

**Estimated time: 3 hours**

---

## Phase 3: Build Core Functions (Day 2-3 - 4 hours)

### ✅ Complete the Citation Analysis Section
- [ ] Implement or adapt `estimate_citation_coverage()`
- [ ] Test on articles with good vs poor citations
- [ ] Add markdown explaining citation quality thresholds
- [ ] Create a simple bar chart comparing citation coverage
- [ ] Write interpretation: What does "well-cited" mean?

### ✅ Complete the Task Generation Section
- [ ] Implement `generate_tasks_from_article()`
- [ ] Make sure it returns a list of task dictionaries
- [ ] Each task should have: type, priority, difficulty, description, time estimate
- [ ] Test on 3 articles: one good, one medium, one poor quality
- [ ] Document: Why did each task get its priority level?

### ✅ Add Error Handling
- [ ] Wrap API calls in try-except blocks
- [ ] Test with a non-existent article
- [ ] Handle timeout errors
- [ ] Add helpful error messages
- [ ] Document: What could go wrong?

**Estimated time: 4 hours**

---

## Phase 4: Bulk Analysis (Day 3-4 - 4 hours)

### ✅ Implement Category Analysis
- [ ] Copy `get_category_articles()` function
- [ ] Choose a manageable category (10-20 articles)
  - Good options: "Machine learning", "Climate change", "Python software"
- [ ] Fetch articles from the category
- [ ] List them in a table with basic info

### ✅ Analyze Multiple Articles
- [ ] Implement `analyze_multiple_articles()`
- [ ] Add a progress indicator (print statements)
- [ ] Include time.sleep() to be respectful to servers
- [ ] Create a pandas DataFrame with results
- [ ] Save results to CSV

### ✅ Calculate Statistics
- [ ] Use pandas to calculate:
  - Mean citations per section
  - Median article length
  - Percentage needing citations
  - Distribution of task counts
- [ ] Document each calculation
- [ ] Explain what the numbers mean

**Estimated time: 4 hours**

---

## Phase 5: Visualizations (Day 4-5 - 3 hours)

### ✅ Create At Least 3 Visualizations
Choose from these options:

**Option 1: Task Distribution**
- [ ] Bar chart showing tasks generated per article
- [ ] Color-code by priority (high=red, medium=yellow, low=green)
- [ ] Add title and axis labels
- [ ] Write interpretation below the chart

**Option 2: Citation Quality**
- [ ] Histogram of citations per section
- [ ] Add vertical line at "good quality" threshold
- [ ] Show how many articles fall below threshold
- [ ] Explain what this means for a campaign

**Option 3: Article Structure**
- [ ] Scatter plot: sections (x-axis) vs citations (y-axis)
- [ ] Add trend line
- [ ] Color points by task count
- [ ] Interpret: Do longer articles have more citations?

**Option 4: Maintenance Templates**
- [ ] Pie chart or bar chart of template types
- [ ] Show which issues are most common
- [ ] Suggest priorities for campaigns

### ✅ Create a Dashboard
- [ ] Combine 3-4 plots in a single figure (use subplots)
- [ ] Give it a title: "Campaign Analysis Dashboard"
- [ ] Make it visually appealing
- [ ] Add an overall interpretation

**Estimated time: 3 hours**

---

## Phase 6: Documentation & Reflection (Day 5-6 - 3 hours)

### ✅ Add Comprehensive Markdown Cells

For each code cell, add a markdown cell that explains:
- [ ] **What** the code does (high level)
- [ ] **Why** this step is important
- [ ] **How** it works (for beginners)
- [ ] **What** you found in the results

### ✅ Write Beginner-Friendly Explanations
Use this template:

```markdown
## [Section Name]

### What we're doing
[1-2 sentences explaining the goal]

### Why this matters
[Explain the importance for Wikipedia/campaigns/new editors]

### How it works
[Break down the technical approach in simple terms]

### What we found
[Your analysis of the results]

### Questions to consider
[Thought-provoking questions about the data]
```

### ✅ Add Code Comments
- [ ] Comment every function with a docstring
- [ ] Add inline comments for complex logic
- [ ] Explain API parameters
- [ ] Document any assumptions you made

### ✅ Create a Summary Section
At the end of your notebook, add:

- [ ] **Key Findings** (3-5 bullet points)
- [ ] **Recommendations for Campaign Organizers**
- [ ] **What I Learned** (personal reflection)
- [ ] **Challenges I Faced** (be honest!)
- [ ] **Future Improvements** (what would you add?)
- [ ] **Comparison to Existing Tools** (mention 2-3 from the task description)

**Estimated time: 3 hours**

---

## Phase 7: Polish & Review (Day 6 - 2 hours)

### ✅ Code Quality
- [ ] Remove any test/debug print statements
- [ ] Ensure consistent naming conventions
- [ ] Make sure all cells run in order (Kernel → Restart & Run All)
- [ ] Fix any errors that appear
- [ ] Check for PEP 8 style compliance (use `import autopep8` if needed)

### ✅ Notebook Flow
- [ ] Read through from start to finish
- [ ] Does each section flow logically to the next?
- [ ] Are there gaps in explanation?
- [ ] Is the difficulty progression smooth?
- [ ] Would a beginner understand this?

### ✅ Visuals & Formatting
- [ ] All visualizations have titles and labels
- [ ] Tables are formatted nicely
- [ ] Markdown uses headers appropriately
- [ ] No overly long code cells (break them up!)
- [ ] Include your name and date at the top

### ✅ Final Checks
- [ ] Spell check your markdown cells
- [ ] All links work (if you added any)
- [ ] No hardcoded paths or personal information
- [ ] Results are reproducible (anyone can run your notebook)

**Estimated time: 2 hours**

---

## Phase 8: Request Feedback (Day 7)

### ✅ Get Your Public Link
- [ ] In PAWS, get your notebook's public URL
  - Format: `https://public-paws.wmcloud.org/User:YourUsername/notebook_name.ipynb`
- [ ] Test the link in an incognito browser window
- [ ] Make sure others can view it

### ✅ Self-Review Checklist
Before requesting mentor feedback, verify:

- [ ] ✅ Notebook runs completely without errors
- [ ] ✅ All questions/TODOs in original notebook are addressed
- [ ] ✅ At least 3 visualizations with interpretations
- [ ] ✅ Analysis of 10+ articles from at least one category
- [ ] ✅ Clear beginner-friendly explanations throughout
- [ ] ✅ Code is well-commented
- [ ] ✅ Includes personal reflections and insights
- [ ] ✅ Comparison to at least 2 existing tools
- [ ] ✅ Summary section with findings and recommendations

### ✅ Request Feedback
- [ ] Compose professional email to mentors
- [ ] Include: silviaegt@wikimedia.org, sbisson@wikimedia.org, isaac@wikimedia.org
- [ ] Subject: "Outreachy Micro-task Notebook - Feedback Request - [Your Name]"
- [ ] Include your public PAWS link
- [ ] Briefly mention 1-2 things you're proud of
- [ ] Ask 1-2 specific questions if you have any

**Email Template:**
```
Subject: Outreachy Micro-task Notebook - Feedback Request - [Your Name]

Dear Sylvia, Stéphane, and Isaac,

I have completed the Micro-Task Generator notebook for the Outreachy 
application and would appreciate your feedback.

Public notebook link: [YOUR PAWS LINK]

Key highlights:
- Analyzed [X] articles across [Y] categories
- Generated [Z] micro-tasks with priority and difficulty ratings
- Created visualizations showing [brief description]
- Compared approach to Citation Hunt and PetScan tools

I'm particularly interested in feedback on [specific aspect].

Thank you for your time and guidance!

Best regards,
[Your Name]
```

**Estimated time: 1 hour**

---

## Phase 9: Incorporate Feedback & Finalize (After feedback)

### ✅ After Receiving Feedback
- [ ] Read feedback carefully
- [ ] Make a list of suggested improvements
- [ ] Prioritize changes (critical vs nice-to-have)
- [ ] Implement the changes
- [ ] Document what you changed in a new markdown cell
- [ ] Re-test the entire notebook

### ✅ Final Submission
- [ ] Ensure notebook is complete and polished
- [ ] Record contribution in Outreachy application
- [ ] Include public PAWS link in application
- [ ] Add a note about improvements made after feedback

---

## 📚 Resources Quick Reference

### Essential Links
- **PAWS**: https://hub-paws.wmcloud.org/
- **MediaWiki API**: https://www.mediawiki.org/wiki/API:Main_page
- **API Sandbox**: https://en.wikipedia.org/wiki/Special:ApiSandbox
- **Pandas Documentation**: https://pandas.pydata.org/docs/
- **Matplotlib Gallery**: https://matplotlib.org/stable/gallery/index.html

### Example Categories to Analyze
Choose categories with 20-100 articles for best results:
- "Machine learning"
- "Climate change"
- "Python software"
- "Women scientists"
- "African history"
- "Renewable energy"

### Common API Endpoints You'll Use
```python
# Get article info
https://en.wikipedia.org/w/api.php?action=query&titles=ARTICLE&prop=info&format=json

# Get templates
https://en.wikipedia.org/w/api.php?action=query&titles=ARTICLE&prop=templates&format=json

# Get categories
https://en.wikipedia.org/w/api.php?action=query&list=categorymembers&cmtitle=Category:NAME&format=json

# Parse article
https://en.wikipedia.org/w/api.php?action=parse&page=ARTICLE&format=json
```

---

## 💡 Pro Tips

### Time Management
- **Don't rush!** Quality > Speed
- Work in focused 2-hour blocks
- Take breaks between phases
- Start early to allow time for questions

### When You're Stuck
1. Read the error message carefully
2. Print intermediate values to debug
3. Test with simpler data first
4. Search the MediaWiki API documentation
5. Ask questions in the Outreachy task comments
6. Help other applicants (teaching reinforces learning!)

### Standing Out
- **Go beyond requirements:** Add creative analyses
- **Show your thinking:** Explain uncertainties and choices
- **Be thorough:** Don't skip the "boring" parts like documentation
- **Connect to real campaigns:** Show you understand the practical use
- **Compare approaches:** Discuss trade-offs and alternatives

### What Mentors Are Looking For
✅ **Python skills**: Clean, functional code
✅ **Learning ability**: How you tackle new APIs and data
✅ **Documentation**: Clear explanations for beginners
✅ **Critical thinking**: Insights about the data
✅ **Communication**: Can you explain complex concepts simply?
✅ **Initiative**: Creative ideas and extra effort

---

## ⏱️ Total Time Estimate

| Phase | Time | Cumulative |
|-------|------|------------|
| Setup & Exploration | 2h | 2h |
| Learn the Basics | 3h | 5h |
| Build Core Functions | 4h | 9h |
| Bulk Analysis | 4h | 13h |
| Visualizations | 3h | 16h |
| Documentation & Reflection | 3h | 19h |
| Polish & Review | 2h | 21h |
| Request Feedback | 1h | 22h |

**Total: ~22 hours** spread over 1-2 weeks

**Note:** This is for someone new to Wikipedia APIs. You might be faster or slower - that's okay!

---

## 🎯 Success Criteria

You'll know you're ready to submit when:

- [ ] ✅ A beginner can read your notebook and understand Wikipedia data analysis
- [ ] ✅ All code runs without errors
- [ ] ✅ Your visualizations tell a clear story
- [ ] ✅ Your task generator produces actionable, prioritized tasks
- [ ] ✅ You've analyzed at least 10 articles comprehensively
- [ ] ✅ You've explained your thinking and findings clearly
- [ ] ✅ You feel proud of your work!

---

## 🆘 Getting Help

### Where to Ask Questions
1. **Outreachy task comments**: Help other applicants too!
2. **MediaWiki API documentation**: Very comprehensive
3. **Stack Overflow**: Tag with `mediawiki-api` and `python`
4. **Wikipedia Village Pump**: For Wikipedia-specific questions

### What to Ask
- ✅ "I'm trying to X but getting error Y. Here's my code..."
- ✅ "What's the best way to count citations in wikitext?"
- ✅ "Is this approach reasonable for analyzing maintenance templates?"
- ❌ "Can someone complete this for me?"
- ❌ "What's Python?" (do basic tutorials first)

---

## 🎉 You've Got This!

Remember:
- **Mentors want to help you succeed**
- **Mistakes are learning opportunities**
- **Your unique perspective adds value**
- **Effort and growth matter more than perfection**

Good luck with your Outreachy application! 🚀

---

*Created for Outreachy December 2025 Applicants*
*Last updated: 2025-10-09*
