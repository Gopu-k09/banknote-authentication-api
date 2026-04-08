#!/usr/bin/env python3
"""
Automated GitHub Deployment for: Gopu-k09
Deploys Bank Note Authentication ML API to GitHub
"""

import os
import sys
import subprocess
import json
from pathlib import Path

# ============================================================================
# CONFIGURATION
# ============================================================================
GITHUB_USERNAME = "Gopu-k09"
REPO_NAME = "banknote-authentication-api"
REPO_URL = f"https://github.com/{GITHUB_USERNAME}/{REPO_NAME}.git"

print("=" * 70)
print("🚀 AUTOMATED GITHUB DEPLOYMENT")
print("=" * 70)
print(f"\n📍 GitHub Username: {GITHUB_USERNAME}")
print(f"📦 Repository Name: {REPO_NAME}")
print(f"🌐 Repository URL: {REPO_URL}\n")

# ============================================================================
# Check Prerequisites
# ============================================================================
print("📋 Checking prerequisites...\n")

# Check if git is installed
try:
    result = subprocess.run(["git", "--version"], capture_output=True, text=True, check=True)
    print(f"✅ Git installed: {result.stdout.strip()}")
except FileNotFoundError:
    print("❌ ERROR: Git is not installed!")
    print("\n📥 INSTALL GIT:")
    print("   1. Download: https://git-scm.com/download/win")
    print("   2. Install with default settings")
    print("   3. Restart VS Code")
    print("   4. Run this script again")
    sys.exit(1)
except Exception as e:
    print(f"❌ Error checking Git: {e}")
    sys.exit(1)

# Check if we're in the right directory
if not os.path.exists("main.py") or not os.path.exists("model.pkl"):
    print("❌ Not in project directory (missing main.py or model.pkl)")
    sys.exit(1)

print("✅ In correct project directory")

# ============================================================================
# STEP 1: Configure Git
# ============================================================================
print("\n" + "=" * 70)
print("⚙️  STEP 1: Configuring Git")
print("=" * 70)

try:
    subprocess.run(["git", "config", "--global", "user.name", "Gopu K09"], check=True)
    print("✅ Git user name configured")
    
    subprocess.run(["git", "config", "--global", "user.email", "gopu.k09@gmail.com"], check=True)
    print("✅ Git email configured")
except Exception as e:
    print(f"⚠️  Warning configuring git: {e}")

# ============================================================================
# STEP 2: Initialize Git Repository
# ============================================================================
print("\n" + "=" * 70)
print("📦 STEP 2: Initializing Git Repository")
print("=" * 70)

try:
    if os.path.exists(".git"):
        print("ℹ️  Git repository already initialized")
    else:
        subprocess.run(["git", "init"], check=True)
        print("✅ Repository initialized")
except Exception as e:
    print(f"❌ Error initializing repository: {e}")
    sys.exit(1)

# ============================================================================
# STEP 3: Add Files
# ============================================================================
print("\n" + "=" * 70)
print("📂 STEP 3: Adding Files to Git")
print("=" * 70)

try:
    subprocess.run(["git", "add", "."], check=True)
    result = subprocess.run(["git", "status", "--short"], capture_output=True, text=True, check=True)
    files = [f for f in result.stdout.strip().split("\n") if f]
    print(f"✅ Added {len(files)} files")
    for file in files[:10]:
        print(f"   {file}")
    if len(files) > 10:
        print(f"   ... and {len(files)-10} more files")
except Exception as e:
    print(f"❌ Error adding files: {e}")
    sys.exit(1)

# ============================================================================
# STEP 4: Create Initial Commit
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
- Ready for production deployment!

Model Performance:
  • Test Accuracy: 98.55%
  • Training Accuracy: 99.18%
  • F1-Score: 0.99
  • Model Type: Logistic Regression

Quick Start:
  1. Docker: docker build -t banknote-api .
  2. Run: docker run -p 8000:8000 banknote-api
  3. Test: http://localhost:8000/docs

Documentation:
  - QUICK_START.md - 5-minute setup guide
  - DEPLOYMENT_GUIDE.md - Comprehensive guide
  - README.md - Project overview"""

try:
    subprocess.run(["git", "commit", "-m", commit_message], check=True)
    print("✅ Initial commit created")
except subprocess.CalledProcessError as e:
    if "nothing to commit" in str(e.stderr):
        print("ℹ️  Nothing new to commit")
    else:
        print(f"⚠️  Warning: {e}")
except Exception as e:
    print(f"⚠️  Warning creating commit: {e}")

# ============================================================================
# STEP 5: Add Remote
# ============================================================================
print("\n" + "=" * 70)
print("🌐 STEP 5: Adding GitHub Remote")
print("=" * 70)

try:
    result = subprocess.run(["git", "remote", "-v"], capture_output=True, text=True)
    
    if "origin" in result.stdout:
        print("⚠️  Remote 'origin' already exists")
        try:
            subprocess.run(["git", "remote", "remove", "origin"], check=True)
            print("✅ Old remote removed")
        except:
            pass
    
    subprocess.run(["git", "remote", "add", "origin", REPO_URL], check=True)
    print(f"✅ Remote added: {REPO_URL}")
except Exception as e:
    print(f"❌ Error adding remote: {e}")
    sys.exit(1)

# ============================================================================
# STEP 6: Rename Branch
# ============================================================================
print("\n" + "=" * 70)
print("🔄 STEP 6: Renaming Branch to 'main'")
print("=" * 70)

try:
    subprocess.run(["git", "branch", "-M", "main"], check=True)
    print("✅ Branch renamed to 'main'")
except Exception as e:
    print(f"⚠️  Warning renaming branch: {e}")

# ============================================================================
# STEP 7: Push to GitHub
# ============================================================================
print("\n" + "=" * 70)
print("📤 STEP 7: Pushing to GitHub")
print("=" * 70)

print(f"""
🌐 Repository URL: {REPO_URL}

📝 BEFORE PROCEEDING:

1. Create Repository on GitHub:
   → Go to: https://github.com/new
   → Name: {REPO_NAME}
   → Description: ML API for bank note authentication
   → Visibility: Public
   → DO NOT check "Initialize with README"
   → Click "Create repository"

2. Create Personal Access Token:
   → Go to: https://github.com/settings/tokens/new
   → Name: git-mlmodel
   → Scope: Check ✓ repo (all)
   → Click "Generate token"
   → COPY the token (won't show again!)

3. When prompted:
   → Username: {GITHUB_USERNAME} (or 'git')
   → Password: Paste your Personal Access Token

⏳ Pushing to GitHub...
""")

try:
    subprocess.run(["git", "push", "-u", "origin", "main"], check=True)
    print("\n✅ Code pushed to GitHub successfully!")
    success = True
except subprocess.CalledProcessError as e:
    print(f"\n❌ Push failed!")
    print(f"\n🔧 TROUBLESHOOTING:")
    print("   1. Make sure you created the repository on GitHub")
    print("   2. Repository must be EMPTY (no README)")
    print("   3. Use Personal Access Token, not password")
    print("   4. Token must have 'repo' scope")
    print("   5. Try again: git push -u origin main")
    success = False
except Exception as e:
    print(f"\n❌ Error: {e}")
    success = False

# ============================================================================
# Final Summary
# ============================================================================
print("\n" + "=" * 70)
if success:
    print("✅ DEPLOYMENT SUCCESSFUL!")
    print("=" * 70)
    print(f"""
🎉 Your GitHub repository is live!

📍 Repository URL:
   {REPO_URL}

✅ Next Steps:

1. Verify on GitHub:
   → Visit: {REPO_URL}
   → Check all files are there

2. Share with team:
   → GitHub URL: {REPO_URL}
   → Read QUICK_START.md for deployment

3. Team can deploy:
   $ git clone {REPO_URL}
   $ cd {REPO_NAME}
   $ docker build -t banknote-api .
   $ docker run -p 8000:8000 banknote-api

📚 Documentation Available:
   - README.md - Overview
   - QUICK_START.md - 5-minute setup
   - DEPLOYMENT_GUIDE.md - Detailed guide

🚀 Your ML API is now on GitHub!
""")
else:
    print("⚠️  DEPLOYMENT INCOMPLETE")
    print("=" * 70)
    print(f"""
⚠️  Push to GitHub failed. Here's what to do:

1. Verify repository exists:
   Go to: https://github.com/new
   Create empty repository: {REPO_NAME}

2. Try again manually:
   $ cd d:\\mlmodel
   $ git remote remove origin
   $ git remote add origin {REPO_URL}
   $ git push -u origin main

3. When prompted:
   - Username: {GITHUB_USERNAME}
   - Password: Your Personal Access Token
     (Create at: https://github.com/settings/tokens/new)

Need manual steps? See: GITHUB_COMPLETE_GUIDE.md
""")

print("=" * 70)
