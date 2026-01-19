#!/bin/bash
# Upload wiki pages to GitHub

set -e  # Exit on error

REPO_URL="https://github.com/tlarroucau/AI_workshop.wiki.git"
WIKI_DIR="wiki"
TEMP_DIR="temp-wiki"

echo "📚 Starting wiki upload..."

# Clone wiki repository
echo "1️⃣  Cloning wiki repository..."
if [ -d "$TEMP_DIR" ]; then
    rm -rf "$TEMP_DIR"
fi
git clone "$REPO_URL" "$TEMP_DIR"

# Copy wiki files
echo "2️⃣  Copying wiki files..."
cp "$WIKI_DIR"/*.md "$TEMP_DIR"/

# Show what will be uploaded
echo "3️⃣  Files to upload:"
ls -1 "$TEMP_DIR"/*.md

# Commit and push
echo "4️⃣  Committing and pushing..."
cd "$TEMP_DIR"
git add .
git commit -m "Add/update comprehensive wiki documentation

- Home: Navigation and quick start
- Getting-Started: Installation guide
- Project-Structure: Directory layout
- Basic-Workflow: Research cycle
- R-Setup: R with radian in VS Code
- Stata-MATLAB-Integration: Statistical software
- Overleaf-Integration: LaTeX collaboration
- Troubleshooting: Common issues"

git push origin master

# Cleanup
echo "5️⃣  Cleaning up..."
cd ..
rm -rf "$TEMP_DIR"

echo "✅ Wiki upload complete!"
echo "🌐 View at: https://github.com/tlarroucau/AI_workshop/wiki"
