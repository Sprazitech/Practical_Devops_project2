# Setup Terraform

Terraform is a critical asset for your infrastructure management. Terraform is an open-source infrastructure as code (IaC) tool that allows you to define and provision infrastructure using a declarative configuration language. Technically speaking, we are setting up the Terraform CLI (command-line interface, configuration parser, state management tools, etc.).

## IMPORTANT:
Please ensure you don't already have Terraform before setting this up. See the section on how to check if you already have Terraform installed.

Also note that you have two options:
- You can either install Terraform on your system using a package manager (like apt, yum, brew, or choco)
- You can set up Terraform as a Portable Binary
  
I prefer the second option as I have more control over the Terraform setup. Also, it means you have to know (and do) a few more things about setting the system PATH to ensure the Terraform executable can be found when you run any command line terminal.

---

## How to Check if you already have Terraform Installed

There are many ways to check if you already have Terraform installed and set up in your system. We will be using the command line version check.

1. Launch your terminal (Cmder, Git Bash, cmd, or PowerShell on Windows; Terminal on macOS/Linux).
2. Run the command below:
   ```bash
   terraform --version
   ```
   or
   ```bash
   terraform version
   ```

If you get a response similar to below, you already have Terraform installed and set up:
```
Terraform v1.9.5
on linux_amd64
```

If your Terraform version is outdated and you wish to update it, google the steps and follow the instructions or simply ask for guidance from a member of the faculty.

---

## How to Set up Terraform by Installation

This option is simple but not my preferred option. It installs Terraform using your system's package manager and sets it up for your use.

### Linux (Ubuntu/Debian)
```bash
# Update package index
sudo apt-get update

# Install required packages
sudo apt-get install -y gnupg software-properties-common

# Add HashiCorp GPG key
wget -O- https://apt.releases.hashicorp.com/gpg | \
gpg --dearmor | \
sudo tee /usr/share/keyrings/hashicorp-archive-keyring.gpg > /dev/null

# Add HashiCorp repository
echo "deb [signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] \
https://apt.releases.hashicorp.com $(lsb_release -cs) main" | \
sudo tee /etc/apt/sources.list.d/hashicorp.list

# Update and install Terraform
sudo apt-get update
sudo apt-get install terraform
```

### macOS
```bash
# Using Homebrew
brew tap hashicorp/tap
brew install hashicorp/tap/terraform
```

### Windows
```powershell
# Using Chocolatey
choco install terraform

# Or using Scoop
scoop install terraform
```

### Sample Guides:
- Official Terraform Installation Guide: https://developer.hashicorp.com/terraform/install
- Linux Installation: https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli
- Windows Installation: https://phoenixnap.com/kb/how-to-install-terraform

**NOTE:** The installation typically places the Terraform binary in a system-wide location (like `/usr/local/bin` or `C:\Program Files`), making it accessible from anywhere on your machine.

---

## How to Set up Terraform Portable Style

This is my preferred option - portable style which gives control over the versions of Terraform I can use. You can easily maintain multiple versions and switch between them as needed.

### Manual Binary Download (All Platforms)

1. **Visit the Terraform Downloads page:**
   - Go to: https://www.terraform.io/downloads

2. **Download the appropriate binary for your system:**
   - Windows: `terraform_<VERSION>_windows_amd64.zip`
   - macOS: `terraform_<VERSION>_darwin_amd64.zip` (Intel) or `terraform_<VERSION>_darwin_arm64.zip` (Apple Silicon)
   - Linux: `terraform_<VERSION>_linux_amd64.zip`

3. **Extract the downloaded archive to your chosen location:**
   ```bash
   # Example for Linux/macOS
   unzip terraform_*.zip
   
   # Move to desired location (e.g., ~/tools/terraform)
   mkdir -p ~/tools/terraform
   mv terraform ~/tools/terraform/
   ```

4. **Verify the binary works:**
   ```bash
   # Navigate to the folder
   cd ~/tools/terraform
   
   # Run terraform
   ./terraform version
   ```

### Using Version Managers (Recommended for Multiple Versions)

#### tfenv (Linux/macOS)
```bash
# Install tfenv
git clone https://github.com/tfutils/tfenv.git ~/.tfenv

# Install specific Terraform version
~/.tfenv/bin/tfenv install 1.9.5

# Use the version
~/.tfenv/bin/tfenv use 1.9.5
```

#### tfswitch (All Platforms)
```bash
# Linux
curl -L https://raw.githubusercontent.com/warrensbox/terraform-switcher/release/install.sh | bash

# Then install and switch versions
tfswitch
```

Also check out **"terragrunt"** and **"tenv"** in your spare time - quite interesting tools for Terraform management.

---

## IMPORTANT NOTE: Setting up the PATH

It is **highly recommended** that you set the Terraform Path at the end so that you can use Terraform from every terminal on your PC (Cmder, cmd, Git Bash, PowerShell, etc.) without needing to switch to the Terraform directory each time you want to use it.

### Linux/macOS
Add to your `~/.bashrc`, `~/.zshrc`, or `~/.bash_profile`:
```bash
# For manual binary installation
export PATH="$HOME/tools/terraform:$PATH"

# For tfenv
export PATH="$HOME/.tfenv/bin:$PATH"
```

Then reload your shell:
```bash
source ~/.bashrc  # or ~/.zshrc
```

### Windows
1. Search for "Environment Variables" in the Start menu
2. Click "Edit the system environment variables"
3. Click "Environment Variables" button
4. Under "User variables" or "System variables", find and select "Path"
5. Click "Edit"
6. Click "New" and add the path to your Terraform directory (e.g., `C:\tools\terraform`)
7. Click "OK" to save

### Verification
After setting up the PATH, open a **new** terminal and run:
```bash
terraform --version
```

You should see the Terraform version information displayed, confirming that Terraform is properly set up and accessible from anywhere on your system.

---

## Additional Setup Steps

### 1. Enable Tab Completion (Optional but Recommended)
```bash
# Bash
terraform -install-autocomplete

# Restart your shell after this
```

### 2. Verify Installation with a Simple Test
```bash
# Create a test directory
mkdir terraform-test && cd terraform-test

# Initialize Terraform (this will download provider plugins)
terraform init

# This should complete successfully even without any .tf files
```

### 3. Configure Terraform Backend (if using remote state)
Refer to the `terraform/infra/backend.tf` in your project for backend configuration examples.

---

## Quick Reference Commands

```bash
# Check version
terraform version

# Format your Terraform files
terraform fmt

# Validate configuration
terraform validate

# Initialize working directory
terraform init

# Plan infrastructure changes
terraform plan

# Apply changes
terraform apply

# Destroy infrastructure
terraform destroy
```

---

## Troubleshooting

### Command Not Found
- Verify Terraform is in your PATH: `echo $PATH` (Linux/macOS) or `echo %PATH%` (Windows)
- Ensure you've restarted your terminal after PATH modifications
- Check file permissions: `chmod +x ~/tools/terraform/terraform` (Linux/macOS)

### Version Conflicts
- Use version managers like `tfenv` or `tfswitch` to manage multiple versions
- Check your project's required version in `.terraform-version` or `versions.tf`

### Permission Errors
- On Linux/macOS, you may need to use `sudo` for system-wide installations
- For portable installations, ensure your user has write permissions to the installation directory

---

**Happy Terraforming! 🚀**
