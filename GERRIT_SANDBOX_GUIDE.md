# Beginner's Guide to Submitting a Dummy Patch to Gerrit Sandbox

## What is Gerrit?
Gerrit is a code review tool used by OpenStack and OpenInfra projects. Before contributing to real projects, you'll practice using the **Gerrit Sandbox** - a safe environment where you can learn without affecting real code.

## Prerequisites

Before you start, you need:
1. **A Launchpad account** - Sign up at https://launchpad.net/
2. **An OpenDev account** - Use your Launchpad credentials to sign in at https://review.opendev.org/
3. **Git installed** on your computer
4. **git-review installed** - This tool helps push changes to Gerrit

## Step-by-Step Instructions

### Step 1: Install git-review
```bash
# On Ubuntu/Debian
sudo apt-get install git-review

# Or using pip
pip install git-review
```

### Step 2: Configure Git (if not already done)
```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

### Step 3: Set up Gerrit Authentication
1. Go to https://review.opendev.org/
2. Sign in with your Launchpad account
3. Click your name (top right) → Settings
4. Go to "HTTP Credentials" section
5. Click "Generate New Password"
6. Follow the instructions to save your credentials

### Step 4: Clone the Gerrit Sandbox Repository
```bash
# Clone the sandbox
git clone https://opendev.org/opendev/sandbox
cd sandbox

# Set up git-review
git review -s
```

### Step 5: Create a Dummy Change
```bash
# Create a new file with your name (example)
echo "Hello from [Your Name]! This is my first Gerrit patch." > hello-yourname.txt

# Or edit the README
echo "Practice patch by [Your Name]" >> README.rst

# Check what you've changed
git status
```

### Step 6: Commit Your Change
```bash
# Stage your changes
git add hello-yourname.txt

# Commit with a message
git commit -m "Add hello file for testing

This is a test patch to learn Gerrit workflow.
"
```

### Step 7: Submit to Gerrit
```bash
# Push your change for review
git review
```

### Step 8: View Your Patch
After running `git review`, you'll get a URL like:
`https://review.opendev.org/c/opendev/sandbox/+/XXXXXX`

This is your patch! You can:
- View it in your browser
- Share this link in your Outreachy submission
- See it in the Gerrit web interface

## Common Issues and Solutions

### Issue: "git review" command not found
**Solution:** Install git-review: `pip install git-review`

### Issue: Authentication fails
**Solution:** 
1. Make sure you've generated HTTP credentials in Gerrit
2. Run `git review -s` again to reconfigure

### Issue: "No .gitreview file found"
**Solution:** You're not in the sandbox directory. Run:
```bash
cd /path/to/sandbox
git review -s
```

### Issue: Change-Id missing
**Solution:** git-review should add this automatically. If not:
1. Install the commit-msg hook: `git review -s`
2. Amend your commit: `git commit --amend`

## What Makes a Good Dummy Patch?

For your Outreachy application, your dummy patch should:
1. ✅ Make a simple, harmless change (like adding a text file with your name)
2. ✅ Have a clear commit message
3. ✅ Successfully appear in Gerrit
4. ❌ Don't worry about it being "merged" - the sandbox is for practice!

## Example Dummy Patch Ideas

1. **Add a personal hello file:**
   ```bash
   echo "Hello! I'm learning Gerrit for the Ironic project internship." > hello-yourname.txt
   ```

2. **Add your name to a list:**
   ```bash
   echo "- [Your Name] - [Date]" >> CONTRIBUTORS.txt
   ```

3. **Create a simple test file:**
   ```bash
   echo "Testing Gerrit workflow - $(date)" > test-$(date +%Y%m%d).txt
   ```

## Next Steps After Submission

1. ✅ Copy the Gerrit review URL from the terminal output
2. ✅ Submit this URL on the Outreachy project page
3. ✅ You can abandon the patch later (it's just for practice!)

## Resources

- 📚 Gerrit Sandbox Documentation: https://docs.opendev.org/opendev/infra-manual/latest/sandbox.html
- 📚 Developer Manual: https://docs.opendev.org/opendev/infra-manual/latest/
- 💬 Get Help: #openstack-ironic on irc.oftc.net

---

**Remember:** The sandbox is for learning! Don't be afraid to experiment. You can submit multiple patches to practice. 🚀
