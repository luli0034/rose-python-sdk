#!/bin/bash

# GitHub Actions Setup Script for Rose Python SDK
# This script helps set up GitHub Actions for automated testing and PyPI publishing

set -e

echo "🚀 Setting up GitHub Actions for Rose Python SDK"
echo "================================================"

# Check if we're in a git repository
if [ ! -d ".git" ]; then
    echo "❌ Error: Not in a git repository. Please run this script from the project root."
    exit 1
fi

# Check if GitHub Actions directory exists
if [ ! -d ".github/workflows" ]; then
    echo "❌ Error: .github/workflows directory not found. Please ensure the workflow files are in place."
    exit 1
fi

echo "✅ GitHub Actions workflows found"

# Check if required files exist
required_files=(
    ".github/workflows/test.yml"
    ".github/workflows/publish.yml"
    ".github/workflows/release.yml"
    "setup.py"
    "requirements.txt"
    "CHANGELOG.md"
)

for file in "${required_files[@]}"; do
    if [ ! -f "$file" ]; then
        echo "❌ Error: Required file $file not found"
        exit 1
    fi
done

echo "✅ All required files found"

# Check if we're on main branch
current_branch=$(git branch --show-current)
if [ "$current_branch" != "main" ]; then
    echo "⚠️  Warning: You're not on the main branch (current: $current_branch)"
    echo "   Consider switching to main branch for production setup"
fi

echo ""
echo "📋 Next Steps:"
echo "=============="
echo ""
echo "1. 🔐 Set up PyPI API Token:"
echo "   - Go to https://pypi.org and create an account"
echo "   - Create an API token in Account Settings → API tokens"
echo "   - Add the token as a GitHub secret:"
echo "     - Go to your GitHub repository"
echo "     - Settings → Secrets and variables → Actions"
echo "     - Add new secret: PYPI_API_TOKEN"
echo ""
echo "2. 🏷️  Update version in setup.py:"
echo "   - Edit setup.py and update the version number"
echo "   - Update CHANGELOG.md with your changes"
echo ""
echo "3. 🚀 Create and push a version tag:"
echo "   git add ."
echo "   git commit -m 'Bump version to X.X.X'"
echo "   git tag vX.X.X"
echo "   git push origin main"
echo "   git push origin vX.X.X"
echo ""
echo "4. 📊 Monitor the workflows:"
echo "   - Go to your GitHub repository"
echo "   - Click on the 'Actions' tab"
echo "   - Watch the workflows run"
echo ""
echo "5. 📚 Read the full setup guide:"
echo "   - See docs/GITHUB_ACTIONS_SETUP.md for detailed instructions"
echo ""

# Check if GitHub remote is set
if git remote get-url origin >/dev/null 2>&1; then
    repo_url=$(git remote get-url origin)
    echo "🔗 Repository URL: $repo_url"
    echo ""
    echo "📝 Update the repository URLs in:"
    echo "   - README.md (badge URLs)"
    echo "   - setup.py (project_urls)"
    echo "   - docs/GITHUB_ACTIONS_SETUP.md (example URLs)"
    echo ""
    echo "   Replace 'your-username' and 'your-org' with your actual GitHub username/org"
else
    echo "⚠️  Warning: No GitHub remote found. Make sure you've pushed to GitHub first."
fi

echo ""
echo "✅ Setup script completed!"
echo ""
echo "For detailed instructions, see: docs/GITHUB_ACTIONS_SETUP.md"
