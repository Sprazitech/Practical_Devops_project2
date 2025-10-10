# Quick Command Reference for Gerrit Sandbox

## One-Time Setup (Do this first!)

```bash
# Install git-review
pip install git-review

# Configure git with your info
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# Clone the sandbox repository
git clone https://opendev.org/opendev/sandbox
cd sandbox

# Setup git-review (connects to Gerrit)
git review -s
```

## Creating and Submitting Your Dummy Patch

```bash
# Make sure you're in the sandbox directory
cd sandbox

# Create your dummy file (replace YourName with your actual name)
echo "Hello from [Your Name]! Learning Gerrit for Ironic internship." > hello-yourname.txt

# Check what you've changed
git status

# Stage your changes
git add hello-yourname.txt

# Commit with a message
git commit -m "Add hello file for Gerrit practice

This is my first patch to learn the OpenStack contribution workflow.
Preparing for the Ironic node history API internship project.
"

# Submit to Gerrit for review
git review

# The output will give you a URL - save this for your Outreachy submission!
```

## Copy This Exact Sequence (Beginner Template)

```bash
# Step 1: Install git-review (if not already installed)
pip install git-review

# Step 2: Clone sandbox
git clone https://opendev.org/opendev/sandbox
cd sandbox

# Step 3: Setup git-review
git review -s

# Step 4: Create your dummy file
echo "Practice patch by [YOUR NAME] - $(date)" > practice-yourname.txt

# Step 5: Add and commit
git add practice-yourname.txt
git commit -m "Add practice file for learning Gerrit

This patch is part of my Outreachy application for the
Ironic node deployment history API internship.
"

# Step 6: Submit to Gerrit
git review
```

## What You'll See

When you run `git review`, you should see something like:

```
remote: Processing changes: refs: 1, new: 1, done
remote:
remote: SUCCESS
remote:
remote:   https://review.opendev.org/c/opendev/sandbox/+/123456 Your practice patch [NEW]
remote:
To https://review.opendev.org/opendev/sandbox
 * [new reference]         HEAD -> refs/for/master
```

**Save that URL!** That's your patch link for the Outreachy submission.

## Troubleshooting

### If git-review asks for username:
- Your Gerrit credentials aren't set up
- Go to https://review.opendev.org/ → Settings → HTTP Credentials
- Generate new password and follow instructions

### If you get "No .gitreview file found":
- You're not in the sandbox directory
- Run: `cd sandbox` then `git review -s`

### If commit message is rejected:
- Make sure your commit message has:
  1. A short title (first line)
  2. A blank line
  3. A detailed description

### If you need to fix your commit message:
```bash
git commit --amend
# Edit the message, save, and exit
git review
```

## After Submission

1. ✅ Copy the Gerrit URL from terminal
2. ✅ Open it in browser to see your patch
3. ✅ Submit the URL on Outreachy project page
4. ✅ Done! You've completed this initial task!

---

**Pro Tip:** You can submit multiple practice patches. Each `git review` creates a new review in Gerrit!
