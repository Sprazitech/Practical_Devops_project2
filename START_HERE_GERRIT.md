# 🚀 START HERE: Your Gerrit Sandbox Dummy Patch Guide

## 👋 Welcome!

You're working on the Outreachy internship application for the **Ironic Node Deployment History API** project. This guide will help you complete one of the initial tasks: **Submit a dummy patch using Gerrit sandbox**.

---

## 📖 What Documents to Use

I've created three helpful guides for you:

### 1️⃣ **COMPLETE_WALKTHROUGH.md** ⭐ START WITH THIS
- **Best for:** Complete beginners
- **Contains:** Step-by-step instructions with screenshots
- **Time:** 15-30 minutes
- **Use this if:** You've never used Gerrit before

### 2️⃣ **GERRIT_QUICK_COMMANDS.md**
- **Best for:** Quick reference
- **Contains:** Just the commands you need to copy-paste
- **Use this if:** You want to see all commands at once

### 3️⃣ **GERRIT_SANDBOX_GUIDE.md**
- **Best for:** Understanding the process
- **Contains:** Detailed explanations and troubleshooting
- **Use this if:** You want to learn more about Gerrit

### 4️⃣ **sample-dummy-patch.txt**
- **What it is:** An example file you can use as inspiration
- **Use it:** As a template for your own dummy file

---

## ⚡ Super Quick Start (If You're in a Hurry)

Already know git? Here's the fastest path:

```bash
# Install git-review
pip install git-review

# Clone and setup
git clone https://opendev.org/opendev/sandbox
cd sandbox
git review -s

# Create dummy file
echo "Practice patch from [YourName]" > hello-yourname.txt

# Commit and submit
git add hello-yourname.txt
git commit -m "Add practice file

This is for Outreachy Ironic internship application.
"
git review
```

Copy the URL you get and submit it to Outreachy!

---

## 🎯 The Goal

By the end of this task, you should have:
1. ✅ A Gerrit account set up
2. ✅ git-review installed and configured
3. ✅ A dummy patch submitted to the sandbox
4. ✅ A Gerrit URL to submit on the Outreachy page

---

## 📝 About Your Application

You're applying for an internship to work on OpenStack Ironic. The project involves:

**Main Goal:** Extend the Ironic node history API

**What you'll add:**
- Track when nodes transition between states (provision, active, etc.)
- Record which user/project triggered state changes
- Add power consumption data for each state
- Create filters to query this information
- Build a summary API for recent data

**Initial Tasks (Before Internship):**
1. ✅ Write an article about Ironic (max 1000 words)
2. ✅ Install Bifrost and write a report about your experience
3. ✅ **Submit a dummy patch to Gerrit sandbox** ← You're here!

---

## 🔗 Important Links

### For This Task:
- **Gerrit Sandbox:** https://review.opendev.org/admin/repos/opendev/sandbox
- **Sandbox Documentation:** https://docs.opendev.org/opendev/infra-manual/latest/sandbox.html
- **Gerrit Web UI:** https://review.opendev.org/

### For Your Application:
- **Ironic Docs:** https://docs.openstack.org/ironic/latest/user/index.html
- **Bifrost Docs:** https://docs.openstack.org/bifrost/latest/
- **Node History API:** https://docs.openstack.org/api-ref/baremetal/#node-history
- **Outreachy Project Page:** (Check your email/application)

### If You Need Help:
- **IRC Chat:** #openstack-ironic on irc.oftc.net
- **Developer Manual:** https://docs.opendev.org/opendev/infra-manual/latest/

---

## 💡 Tips for Success

### Do's ✅
- Use a descriptive filename (like `hello-yourname.txt`)
- Write a clear commit message
- Test that your Gerrit URL opens in a browser before submitting
- Keep your dummy patch simple - it's just for practice!
- Ask for help if you get stuck (IRC channel)

### Don'ts ❌
- Don't worry about your patch being "good" - it's just practice!
- Don't try to patch actual Ironic code yet
- Don't stress if you make mistakes - you can submit multiple times
- Don't skip setting up HTTP credentials in Gerrit

---

## 🎓 What You're Learning

This task teaches you:
1. **Git basics** - version control fundamentals
2. **Gerrit workflow** - how OpenStack does code review
3. **git-review tool** - specialized tool for Gerrit
4. **OpenDev infrastructure** - where OpenStack development happens
5. **Collaboration skills** - working with open source tools

These skills are essential for the internship!

---

## 📋 Checklist

Before you start:
- [ ] I have a Launchpad account
- [ ] I can log into https://review.opendev.org/
- [ ] Git is installed on my computer
- [ ] I have a terminal/command prompt ready

After completion:
- [ ] I successfully ran `git review`
- [ ] I got a Gerrit URL (https://review.opendev.org/c/opendev/sandbox/+/XXXXX)
- [ ] I can see my patch in the web browser
- [ ] I submitted the URL to Outreachy

---

## 🚦 What to Do Right Now

**Step 1:** Open `COMPLETE_WALKTHROUGH.md` in this folder  
**Step 2:** Follow the instructions step-by-step  
**Step 3:** Submit your Gerrit URL to Outreachy  
**Step 4:** Celebrate! 🎉

---

## ❓ Frequently Asked Questions

**Q: Will my dummy patch be merged into real code?**  
A: No! The sandbox is just for practice. Your patch won't affect any real projects.

**Q: How long does this take?**  
A: Usually 15-30 minutes, including setup.

**Q: Can I submit multiple patches?**  
A: Yes! Feel free to practice as many times as you want.

**Q: Do I need to know Python for this task?**  
A: No! This task is just about learning the workflow. Python comes later.

**Q: What if my patch isn't reviewed?**  
A: That's normal! The sandbox patches often aren't reviewed. Just having the URL is enough.

**Q: Can I use GitHub instead of Gerrit?**  
A: No, OpenStack uses Gerrit. Learning it is part of the task.

---

## 🎯 Success Looks Like This

When you're done, you'll have:
1. A terminal showing: `remote: SUCCESS` and a Gerrit URL
2. A web page showing your patch at review.opendev.org
3. A link like: `https://review.opendev.org/c/opendev/sandbox/+/123456`

---

## 🌟 You've Got This!

Remember: Everyone who contributes to OpenStack started exactly where you are now. The sandbox is designed for learning, so don't worry about making mistakes.

**Now go to COMPLETE_WALKTHROUGH.md and let's get started!** 🚀

---

**Questions?** Check the troubleshooting sections in the other guides, or ask in #openstack-ironic IRC channel.

**Good luck with your Outreachy application!** 💪
