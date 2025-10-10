# Complete Beginner's Walkthrough: Submit Dummy Patch to Gerrit

## 🎯 What You're Going to Do

You're going to create a simple text file and submit it to the OpenDev Gerrit Sandbox. This proves you can use the tools needed for the Ironic internship!

**Time needed:** 15-30 minutes  
**Difficulty:** Beginner-friendly

---

## 📋 Before You Start - Checklist

- [ ] You have a Launchpad account (create at https://launchpad.net/)
- [ ] You can access https://review.opendev.org/ (sign in with Launchpad)
- [ ] Git is installed on your computer
- [ ] You have a terminal/command prompt open

---

## 🚀 Step-by-Step Instructions

### STEP 1: Set Up Your Gerrit Account (5 minutes)

1. **Go to Gerrit:** Open https://review.opendev.org/
2. **Sign in:** Click "Sign In" and use your Launchpad account
3. **Generate credentials:**
   - Click your name in top-right corner
   - Click "Settings"
   - Click "HTTP Credentials" in the left menu
   - Click "Generate New Password"
   - **Important:** Follow the instructions shown - they'll give you commands to run
   - Copy those commands and save them somewhere

### STEP 2: Install git-review (2 minutes)

Open your terminal and run:

```bash
pip install git-review
```

If that doesn't work, try:
```bash
pip3 install git-review
```

Or on Ubuntu/Debian:
```bash
sudo apt-get install git-review
```

**Check it worked:**
```bash
git-review --version
```
You should see a version number.

### STEP 3: Configure Git (2 minutes)

Tell git who you are:

```bash
git config --global user.name "Your Full Name"
git config --global user.email "your.email@example.com"
```

Replace with your actual name and email!

### STEP 4: Clone the Sandbox (3 minutes)

```bash
# Go to a folder where you want to download the sandbox
# For example: cd ~/Projects or cd ~/Documents

# Clone the sandbox repository
git clone https://opendev.org/opendev/sandbox

# Enter the sandbox directory
cd sandbox

# Set up git-review for this repository
git review -s
```

**What you'll see:**
- If it asks for your username, enter your Launchpad username
- It might download some files - this is normal
- If successful, it will finish silently or say "Done"

### STEP 5: Create Your Dummy File (1 minute)

Now you're going to create a simple file. Replace `yourname` with your actual name (no spaces):

```bash
echo "Hello! This is my first Gerrit patch.
My name is [Your Name].
I'm applying for the Ironic internship.
Date: $(date)" > hello-yourname.txt
```

**Example:**
If your name is "Jane Smith", you might run:
```bash
echo "Hello! This is my first Gerrit patch.
My name is Jane Smith.
I'm applying for the Ironic internship.
Date: $(date)" > hello-janesmith.txt
```

**Check it was created:**
```bash
ls hello-*.txt
cat hello-*.txt
```

### STEP 6: Commit Your Change (2 minutes)

```bash
# Tell git you want to include this file
git add hello-*.txt

# Create a commit (like a save point)
git commit -m "Add hello file for Gerrit practice

This is my first patch to learn the OpenStack workflow.
I am applying for the Ironic node history API internship.
This is a practice patch for the Gerrit sandbox.
"
```

**What you'll see:**
```
[master abc1234] Add hello file for Gerrit practice
 1 file changed, 4 insertions(+)
 create mode 100644 hello-yourname.txt
```

### STEP 7: Submit to Gerrit! (2 minutes)

This is the exciting part:

```bash
git review
```

**What you'll see:**
```
remote: Processing changes: refs: 1, new: 1, done
remote:
remote: SUCCESS
remote:
remote:   https://review.opendev.org/c/opendev/sandbox/+/123456 Add hello file [NEW]
remote:
```

**🎉 That URL is your patch!** Copy it!

### STEP 8: View Your Patch (1 minute)

1. Copy the URL from the terminal (the one that says `https://review.opendev.org/c/opendev/sandbox/+/...`)
2. Open it in your web browser
3. You should see your patch with:
   - Your commit message
   - The file you added
   - Your name as the owner

**Take a screenshot of this page!**

---

## ✅ What to Submit for Outreachy

On the Outreachy submissions page, submit:

1. **The Gerrit URL** - Copy it exactly from your terminal
2. **Optional:** A screenshot showing your patch in Gerrit

**Example URL format:**
`https://review.opendev.org/c/opendev/sandbox/+/123456`

---

## ❗ Common Problems and Solutions

### Problem: "git review -s" asks for username and I don't know it
**Solution:** Your Launchpad username is in your Launchpad profile URL:
- Go to https://launchpad.net/~yourname
- The part after `~` is your username

### Problem: "git review" says "No .gitreview file found"
**Solution:** You're not in the sandbox folder. Run:
```bash
cd sandbox
git review -s
git review
```

### Problem: Permission denied when running git review
**Solution:** You haven't set up HTTP credentials in Gerrit
1. Go to https://review.opendev.org/settings/#HTTPCredentials
2. Click "Generate New Password"
3. Follow the exact commands shown

### Problem: "Change-Id is missing"
**Solution:** Run this, then try again:
```bash
git review -s
git commit --amend --no-edit
git review
```

### Problem: My commit message is rejected
**Solution:** Your message needs a blank line after the title:
```bash
git commit --amend
# In the editor, make sure there's a blank line after the first line
# Save and exit
git review
```

### Problem: I made a mistake and want to start over
**Solution:**
```bash
# Go back to the original state
git reset --hard origin/master

# Start from STEP 5 again
```

---

## 🎓 Understanding What You Just Did

Let me explain what happened in simple terms:

1. **git clone** - You downloaded a copy of the sandbox project
2. **git add** - You told git to track your new file
3. **git commit** - You saved your change with a description
4. **git review** - You uploaded your change to Gerrit for review

This is the same process you'll use when contributing to Ironic!

---

## 🎯 Next Steps

After completing this:

1. ✅ Submit the Gerrit URL to Outreachy
2. 📖 Start working on the other initial tasks:
   - Write an article about Ironic (max 1000 words)
   - Install and try Bifrost, write a report
3. 🌟 You can practice more by submitting additional dummy patches!

---

## 📚 Additional Resources

- **Gerrit Sandbox Docs:** https://docs.opendev.org/opendev/infra-manual/latest/sandbox.html
- **Git Basics:** https://git-scm.com/book/en/v2/Getting-Started-Git-Basics
- **OpenStack Contributor Guide:** https://docs.openstack.org/contributors/
- **Need Help?** Join #openstack-ironic on irc.oftc.net

---

## 🌟 Congratulations!

You've just completed your first Gerrit submission! This is a real accomplishment - you've used the same tools that professional OpenStack developers use every day.

Good luck with your Outreachy application! 🚀
