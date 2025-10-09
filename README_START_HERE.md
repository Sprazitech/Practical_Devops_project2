# 🎓 Outreachy Micro-Task Generator - Complete Beginner's Guide

## 👋 Welcome!

Congratulations on getting started with your Outreachy application! This guide provides everything you need to complete the Micro-Task Generator notebook successfully.

**What you have**: Access to PAWS and a forked notebook
**What you need**: Detailed guidance to complete it  
**What's here**: Complete beginner-friendly resources!

---

## 📂 Your Resource Files

I've created several comprehensive guides for you. Here's how to use them:

### 1. 🚀 **START HERE: COMPLETION_CHECKLIST.md**
**Read this FIRST!**
- Step-by-step action plan
- Organized into phases with time estimates
- Clear checkboxes to track progress
- Total time: ~22 hours over 1-2 weeks

**When to use**: 
- Planning your work schedule
- Tracking your progress
- When you're unsure what to do next

---

### 2. 📖 **OUTREACHY_MICROTASK_GUIDE.md**
**Your comprehensive technical reference**
- Detailed explanations of every component
- Complete code examples with explanations
- Data analysis and visualization guidance
- Documentation best practices
- 40+ pages of beginner-friendly content

**When to use**:
- Learning how to implement each section
- Understanding why you're doing each step
- Getting code examples to adapt
- Learning best practices for documentation

**Key sections**:
- Phase 1: Setup and Understanding
- Phase 2: Fetching Article Data
- Phase 3: Analyzing Article Quality
- Phase 4: Generating Prioritized Tasks
- Phase 5: Data Analysis and Visualization
- Phase 6: Building the Complete System

---

### 3. 💻 **microtask_generator_examples.py**
**Working Python code you can use**
- Complete, tested functions
- Comprehensive comments
- Ready to copy into your notebook
- Example usage demonstrations

**When to use**:
- Need working code to adapt
- Stuck on implementation
- Want to see best practices
- Testing concepts before integrating

**Key functions**:
```python
get_article_basic_info()      # Fetch article metadata
get_maintenance_templates()   # Find issue templates
analyze_article_structure()   # Analyze sections/links
estimate_citation_coverage()  # Check citation quality
generate_tasks_from_article() # Main task generator
analyze_multiple_articles()   # Bulk analysis
```

---

### 4. 🧠 **WIKIPEDIA_CONCEPTS_EXPLAINED.md**
**Understanding Wikipedia and MediaWiki**
- Wikipedia structure and terminology
- How the MediaWiki API works
- Quality metrics explained
- WikiProjects and campaigns
- Technical concepts simplified
- Common patterns and debugging tips

**When to use**:
- You're new to Wikipedia editing
- Don't understand a concept
- Need to explain something in your notebook
- Want deeper understanding of the ecosystem

**Key topics**:
- What are maintenance templates?
- How do categories work?
- Understanding JSON responses
- Citation density metrics
- API request structure

---

## 🗺️ Your Learning Path

### Week 1: Foundation & Core Functions

**Day 1-2: Setup and Learning**
1. Read: `COMPLETION_CHECKLIST.md` (Phase 1-2)
2. Read: `WIKIPEDIA_CONCEPTS_EXPLAINED.md` (Parts 1-3)
3. Set up PAWS and test environment
4. Make first API call successfully

**Day 3-4: Build Core Functions**
1. Reference: `OUTREACHY_MICROTASK_GUIDE.md` (Phase 2-3)
2. Copy functions from: `microtask_generator_examples.py`
3. Implement article analysis
4. Implement task generation
5. Test with 3-5 articles

**Day 5: Data Analysis**
1. Reference: `OUTREACHY_MICROTASK_GUIDE.md` (Phase 4)
2. Analyze a category of 10-20 articles
3. Create pandas DataFrame
4. Calculate statistics

### Week 2: Polish & Complete

**Day 6-7: Visualizations**
1. Reference: `OUTREACHY_MICROTASK_GUIDE.md` (Phase 5)
2. Create 3-4 visualizations
3. Build analysis dashboard
4. Write interpretations

**Day 8-9: Documentation**
1. Reference: `OUTREACHY_MICROTASK_GUIDE.md` (Phase 6)
2. Add comprehensive markdown cells
3. Explain concepts for beginners
4. Write reflection and summary

**Day 10: Polish & Submit**
1. Follow: `COMPLETION_CHECKLIST.md` (Phase 7-8)
2. Review and fix errors
3. Get public link
4. Request mentor feedback

---

## 🎯 Quick Start (30 Minutes)

Want to dive in immediately? Follow these steps:

### Step 1: Open Your Notebook (5 min)
1. Go to https://hub-paws.wmcloud.org/
2. Open your forked Micro-Task Generator notebook
3. Read through it once (don't code yet)

### Step 2: Test the Environment (10 min)
```python
# Cell 1: Imports
import requests
import json
import pandas as pd
import matplotlib.pyplot as plt

print("✅ All libraries imported successfully!")
```

```python
# Cell 2: Test API call
url = "https://en.wikipedia.org/w/api.php"
params = {
    'action': 'query',
    'titles': 'Python (programming language)',
    'prop': 'info',
    'format': 'json'
}

response = requests.get(url, params=params)
data = response.json()

print("✅ API call successful!")
print(json.dumps(data, indent=2))
```

### Step 3: Copy Your First Function (10 min)
Open `microtask_generator_examples.py` and copy the `get_article_basic_info()` function into your notebook. Run it!

```python
# Test it
info = get_article_basic_info("Python (programming language)")
print(f"Article: {info['title']}")
print(f"Length: {info['length']} bytes")
print(f"Watchers: {info['watchers']}")
```

### Step 4: Add Documentation (5 min)
Add a markdown cell above your code explaining:
- What this function does
- Why we need this information
- What the results tell us

**Congratulations!** 🎉 You've started your notebook!

---

## 📋 Suggested Daily Schedule

### For Working/Busy Schedule (2-3 hours/day)

**Week 1:**
- Mon: Setup + API basics (2h)
- Tue: Continue API exploration (2h)
- Wed: Build analysis functions (2h)
- Thu: Build task generator (3h)
- Fri: Test with multiple articles (2h)
- Weekend: Catch up or get ahead

**Week 2:**
- Mon: Create visualizations (3h)
- Tue: More visualizations + analysis (2h)
- Wed: Add documentation throughout (3h)
- Thu: Polish and review (2h)
- Fri: Final review + request feedback (2h)
- Weekend: Address feedback

### For Full-Time Focus (4-6 hours/day)

**Days 1-2:** Setup through core functions
**Days 3-4:** Bulk analysis + visualizations
**Days 5-6:** Documentation + polish
**Day 7:** Final review + submit for feedback
**Days 8-9:** Incorporate feedback + finalize

---

## 💡 Pro Tips for Success

### Using These Resources Effectively

1. **Don't try to read everything at once**
   - Use the checklist to know what to read when
   - Reference guides as needed, not all at once

2. **Code first, perfect later**
   - Get something working, then improve it
   - Don't get stuck trying to make perfect code on first try

3. **Document as you go**
   - Add markdown cells immediately after coding
   - Easier than trying to document everything at the end

4. **Test frequently**
   - Run cells after every change
   - Catch errors early when they're easier to fix

5. **Ask for help when stuck > 30 minutes**
   - Post in Outreachy task comments
   - Other applicants can often help!

### Common Pitfalls to Avoid

❌ **Don't**: Copy code without understanding it
✅ **Do**: Read the code, add comments explaining how it works

❌ **Don't**: Analyze 100+ articles at once (slow, might timeout)
✅ **Do**: Start with 5-10 articles, then scale up

❌ **Don't**: Skip documentation to "save time"
✅ **Do**: Document thoroughly - it's a major evaluation criterion

❌ **Don't**: Wait until the end to test
✅ **Do**: Test each function as you build it

❌ **Don't**: Panic if something doesn't work
✅ **Do**: Read error messages, print intermediate values, debug systematically

---

## 🎓 Learning Resources

### Before You Start
**If you're new to any of these, spend a few hours on tutorials first:**

- **Python basics**: https://docs.python.org/3/tutorial/
- **Pandas**: https://pandas.pydata.org/docs/getting_started/intro_tutorials/
- **Matplotlib**: https://matplotlib.org/stable/tutorials/introductory/pyplot.html
- **APIs**: https://www.freecodecamp.org/news/apis-for-beginners/

### While You Work
- **MediaWiki API docs**: https://www.mediawiki.org/wiki/API:Main_page
- **API Sandbox** (test queries): https://en.wikipedia.org/wiki/Special:ApiSandbox
- **Stack Overflow**: Search for "mediawiki api python"

### Understanding Wikipedia
- **How Wikipedia works**: https://en.wikipedia.org/wiki/Wikipedia:Introduction
- **WikiProjects**: https://en.wikipedia.org/wiki/Wikipedia:WikiProject
- **Maintenance templates**: https://en.wikipedia.org/wiki/Category:Maintenance_templates

---

## ❓ FAQ

### "How good does my notebook need to be?"
Focus on:
- **Completeness**: All sections done
- **Clarity**: Beginners can understand
- **Functionality**: Code works without errors
- **Thoughtfulness**: Shows your thinking and learning

Mentors are looking for **effort, learning ability, and communication skills**, not perfection!

### "What if I don't understand something?"
1. Read the relevant section in `WIKIPEDIA_CONCEPTS_EXPLAINED.md`
2. Try the example code in `microtask_generator_examples.py`
3. Read the detailed explanation in `OUTREACHY_MICROTASK_GUIDE.md`
4. Ask in Outreachy task comments
5. Search MediaWiki API documentation

### "How much time should this take?"
- **Minimum viable**: ~15 hours
- **Recommended**: ~20-25 hours
- **Excellent submission**: 25-30 hours

Quality > speed. Better to take extra time and do it well!

### "Can I use AI assistance (ChatGPT, etc.)?"
Be careful:
- ✅ OK: Understanding concepts, debugging errors
- ✅ OK: Explaining code you wrote
- ⚠️ Careful: Generating code (you must understand it!)
- ❌ No: Having AI complete the notebook for you

**Rule of thumb**: If you can't explain every line, don't include it.

### "Should I add extra features?"
Focus on completing the basics WELL first, then if you have time:
- ✅ Compare to existing tools (Citation Hunt, PetScan, etc.)
- ✅ Add creative analyses
- ✅ Propose future enhancements
- ❌ Don't add features that break the core functionality

---

## 🆘 Getting Help

### Where to Ask
1. **Outreachy task page comments** - Best for task-specific questions
2. **Stack Overflow** - Tag: `mediawiki-api`, `python`
3. **MediaWiki support** - For API-specific issues

### How to Ask Good Questions
Include:
- What you're trying to do
- What you expected to happen
- What actually happened
- Your code (simplified if possible)
- Error messages (full text)

**Good question example**:
```
I'm trying to count citations in an article using the code below,
but I'm getting KeyError: 'wikitext'. The API response shows {...}.
What am I doing wrong?

[code here]
```

**Poor question example**:
```
My code doesn't work. Help?
```

---

## ✅ Final Checklist Before Submitting for Feedback

Use this before requesting mentor feedback:

**Functionality**:
- [ ] All code cells run without errors
- [ ] Kernel → Restart & Run All succeeds completely
- [ ] Functions handle errors (try-except blocks)
- [ ] Tested with at least 10 articles

**Analysis**:
- [ ] Analyzed at least one full category
- [ ] Created 3+ visualizations with interpretations
- [ ] Generated tasks with priorities and difficulty
- [ ] Calculated meaningful statistics

**Documentation**:
- [ ] Every code cell has explanation in markdown
- [ ] Concepts explained for beginners
- [ ] Results are interpreted thoughtfully
- [ ] Summary section with findings

**Quality**:
- [ ] Code is well-commented
- [ ] Visualizations have titles and labels
- [ ] No debug/test print statements left
- [ ] Personal reflection included
- [ ] Compared to 2+ existing tools

**Professionalism**:
- [ ] Your name at the top
- [ ] Date included
- [ ] Spell-checked markdown
- [ ] Public PAWS link works

---

## 🚀 You're Ready!

You now have:
- ✅ Clear action plan (`COMPLETION_CHECKLIST.md`)
- ✅ Comprehensive guide (`OUTREACHY_MICROTASK_GUIDE.md`)
- ✅ Working code examples (`microtask_generator_examples.py`)
- ✅ Conceptual understanding (`WIKIPEDIA_CONCEPTS_EXPLAINED.md`)
- ✅ Success roadmap (this document!)

**Next steps:**
1. Bookmark this folder
2. Open `COMPLETION_CHECKLIST.md`
3. Start with Phase 1
4. Reference other guides as needed

**Remember**: You're not just completing a task - you're:
- Learning valuable skills (Python, APIs, data analysis)
- Contributing to Wikipedia's mission
- Demonstrating your potential as an intern
- Joining a global open-source community

---

## 💪 You've Got This!

The mentors have designed this task to be challenging but achievable. They want you to succeed!

**Key mindsets:**
- 🧠 **Curiosity**: Explore and ask "why?"
- 🔄 **Iteration**: First version doesn't need to be perfect
- 📝 **Documentation**: Explain your thinking
- 🤝 **Community**: Help other applicants too!
- 🎯 **Focus**: Complete basics well before adding extras

**When you're done**, you'll have:
- A complete, working micro-task generator
- Experience with real-world APIs
- Wikipedia data analysis skills
- A portfolio piece for your application
- Confidence in your abilities!

---

## 📞 Support

If you have questions about these guides themselves:
1. Reread the relevant section carefully
2. Check if another guide explains it differently
3. Ask in Outreachy task comments
4. Reference the official MediaWiki API documentation

---

**Good luck with your Outreachy application!** 🎉

Remember: The goal isn't perfection - it's to show your learning, thinking, and communication skills. Be yourself, do your best, and demonstrate your growth!

---

*Created with ❤️ for Outreachy December 2025 Applicants*
*Last updated: 2025-10-09*

---

## 📚 Document Navigation

- **📋 COMPLETION_CHECKLIST.md** - Your action plan
- **📖 OUTREACHY_MICROTASK_GUIDE.md** - Detailed technical guide  
- **💻 microtask_generator_examples.py** - Working code
- **🧠 WIKIPEDIA_CONCEPTS_EXPLAINED.md** - Concepts explained
- **🏠 README_START_HERE.md** - This document
