#!/usr/bin/env python3
"""
GitHub Deployment Automation Script
Automates the process of pushing your ML API to GitHub
"""

import os
import sys
import subprocess
import getpass
from pathlib import Path

print("=" * 70)
print("🚀 GITHUB DEPLOYMENT AUTOMATION")
print("=" * 70)

# ============================================================================
# Check prerequisites
# ============================================================================
print("\n📋 Checking prerequisites...")

# Check if git is installed
try:
    subprocess.run(["git", "--version"], capture_output=True, check=True)
    print("✅ Git is installed")
except:
    print("❌ Git is not installed!")
    print("   Download: https://git-scm.com/download/win")
    sys.exit(1)

# Check if we're in the right directory
if not os.path.exists("main.py") or not os.path.exists("model.pkl"):
    print("❌ Not in project directory (missing main.py or model.pkl)")
    sys.exit(1)

print("✅ In correct project directory")

# ============================================================================
# Get GitHub information
# ============================================================================
print("\n" + "=" * 70)
print("📝 GITHUB REPOSITORY INFORMATION")
print("=" * 70)

username = input("\n👤 Enter your GitHub username: ").strip()
repo_name = input("📦 Enter repository name [banknote-authentication-api]: ").strip()
if not repo_name:
    repo_name = "banknote-authentication-api"

repo_url = f"https://github.com/{username}/{repo_name}.git"

print(f"\n✅ Repository URL: {repo_url}")

# ============================================================================
# Get user info
# ============================================================================
print("\n" + "=" * 70)
print("👤 GIT USER CONFIGURATION")
print("=" * 70)

git_name = input("\nEnter your name for commits [skip for default]: ").strip()
git_email = input("Enter your email for commits [skip for default]: ").strip()

# ============================================================================
# Step 1: Configure git
# ============================================================================
print("\n" + "=" * 70)
print("⚙️  STEP 1: Configuring Git")
print("=" * 70)

if git_name:
    subprocess.run(["git", "config", "--global", "user.name", git_name], check=True)
    print(f"✅ Git user name: {git_name}")

if git_email:
    subprocess.run(["git", "config", "--global", "user.email", git_email], check=True)
    print(f"✅ Git email: {git_email}")

# ============================================================================
# Step 2: Initialize git repository
# ============================================================================
print("\n" + "=" * 70)
print("📦 STEP 2: Initializing Git Repository")
print("=" * 70)

# Check if git already initialized
if not os.path.exists(".git"):
    subprocess.run(["git", "init"], check=True)
    print("✅ Repository initialized")
else:
    print("ℹ️  Repository already initialized")

# ============================================================================
# Step 3: Add all files
# ============================================================================
print("\n" + "=" * 70)
print("📂 STEP 3: Adding Files to Git")
print("=" * 70)

subprocess.run(["git", "add", "."], check=True)

# Show status
result = subprocess.run(["git", "status", "--short"], capture_output=True, text=True, check=True)
files = result.stdout.strip().split("\n")
print(f"\n✅ Added {len([f for f in files if f])} files:")
for file in files[:10]:  # Show first 10
    if file:
        print(f"   {file}")
if len(files) > 10:
    print(f"   ... and {len(files)-10} more files")

# ============================================================================
# Step 4: Create initial commit
# ============================================================================
print("\n" + "=" * 70)
print("💾 STEP 4: Creating Initial Commit")
print("=" * 70)

commit_message = """🚀 Initial commit: Bank Note Authentication ML API v1.0

- Trained Logistic Regression model with 98.55% test accuracy
- FastAPI application with auto-generated Swagger documentation
- Docker containerization for production-ready deployment
- Complete deployment guides and documentation
- Model size: 1.2 KB (lightweight and efficient)
- Production ready - ready to deploy!"""

subprocess.run(["git", "commit", "-m", commit_message], check=True)
print("✅ Initial commit created")

# ============================================================================
# Step 5: Add remote
# ============================================================================
print("\n" + "=" * 70)
print("🌐 STEP 5: Adding GitHub Remote")
print("=" * 70)

# Check if remote exists
result = subprocess.run(["git", "remote", "-v"], capture_output=True, text=True)

if "origin" in result.stdout:
    print("⚠️  Remote 'origin' already exists")
    remove = input("   Remove and add new remote? (y/n) [y]: ").strip().lower()
    if remove != "n":
        subprocess.run(["git", "remote", "remove", "origin"], check=True)
        subprocess.run(["git", "remote", "add", "origin", repo_url], check=True)
        print(f"✅ Remote updated: {repo_url}")
else:
    subprocess.run(["git", "remote", "add", "origin", repo_url], check=True)
    print(f"✅ Remote added: {repo_url}")

# ============================================================================
# Step 6: Rename branch
# ============================================================================
print("\n" + "=" * 70)
print("🔄 STEP 6: Renaming Branch to 'main'")
print("=" * 70)

subprocess.run(["git", "branch", "-M", "main"], check=True)
print("✅ Branch renamed to 'main'")

# ============================================================================
# Step 7: Push to GitHub
# ============================================================================
print("\n" + "=" * 70)
print("📤 STEP 7: Pushing to GitHub")
print("=" * 70)

print("\n⏳ This will push your code to GitHub...")
print("   You may be prompted for authentication.")
print("   Options:")
print("   1. GitHub Personal Access Token (Recommended)")
print("   2. GitHub CLI (gh auth login)")
print("   3. SSH key authentication")
print("\n📝 To create a token: https://github.com/settings/tokens/new")
print("   Scopes needed: repo (all)")

try:
    subprocess.run(["git", "push", "-u", "origin", "main"], check=True)
    print("\n✅ Code pushed to GitHub successfully!")
except subprocess.CalledProcessError as e:
    print(f"\n❌ Push failed: {e}")
    print("\n🔧 Troubleshooting steps:")
    print("   1. Check your GitHub username and token")
    print("   2. Create a personal access token at: https://github.com/settings/tokens")
    print("   3. Try pushing again with: git push -u origin main")
    sys.exit(1)

# ============================================================================
# Final Summary
# ============================================================================
print("\n" + "=" * 70)
print("✅ DEPLOYMENT COMPLETE!")
print("=" * 70)

print(f"""
🎉 Your GitHub repository is now live!

📍 Repository URL: {repo_url}

✅ What was done:
   ✓ Git repository initialized
   ✓ All files added and staged
   ✓ Initial commit created
   ✓ Remote repository added
   ✓ Branch renamed to 'main'
   ✓ Code pushed to GitHub

📊 Next steps:

1. Visit your repository:
   {repo_url}

2. Verify all files are there:
   - main.py ✅
   - model.pkl ✅
   - requirements.txt ✅
   - Dockerfile ✅
   - Documentation files ✅

3. Share with your team:
   "Check out my ML API: {repo_url}"

4. For deployment:
   - Team clones: git clone {repo_url}
   - Read: QUICK_START.md
   - Deploy with Docker

📚 Documentation available in repo:
   - README.md - Project overview
   - QUICK_START.md - 5-minute setup
   - DEPLOYMENT_GUIDE.md - Detailed guide
   - HANDOFF_DOCUMENT.md - Technical brief

🚀 Ready for production deployment!
""")

print("=" * 70)
print("✨ SUCCESS! Your code is on GitHub! ✨")
print("=" * 70)
