# Wiki Setup Instructions

This directory contains wiki pages for the AI_workshop repository.

## Uploading to GitHub Wiki

### Method 1: Using GitHub Web Interface (Easiest)

1. Go to your repository: `https://github.com/tlarroucau/AI_workshop`
2. Click the "Wiki" tab
3. Click "Create the first page" or "New Page"
4. Copy content from each `.md` file in this directory
5. Save each page with the corresponding name (without `.md` extension)

**Page order to create:**
1. Home (from `Home.md`)
2. Getting-Started (from `Getting-Started.md`)
3. Project-Structure (from `Project-Structure.md`)
4. Basic-Workflow (from `Basic-Workflow.md`)
5. R-Setup (from `R-Setup.md`)
6. Stata-MATLAB-Integration (from `Stata-MATLAB-Integration.md`)
7. Overleaf-Integration (from `Overleaf-Integration.md`)
8. Troubleshooting (from `Troubleshooting.md`)

### Method 2: Using Git (Advanced)

GitHub wikis are actually Git repositories themselves.

```bash
# Clone the wiki repository
git clone https://github.com/tlarroucau/AI_workshop.wiki.git

# Copy wiki files
cp wiki/*.md AI_workshop.wiki/

# Commit and push
cd AI_workshop.wiki
git add .
git commit -m "Add comprehensive wiki documentation"
git push origin master
```

### Method 3: Bulk Upload Script

Create a script to automate wiki creation:

```bash
#!/bin/bash
# upload-wiki.sh

WIKI_REPO="https://github.com/tlarroucau/AI_workshop.wiki.git"

# Clone wiki
git clone $WIKI_REPO temp-wiki
cd temp-wiki

# Copy all wiki files
cp ../wiki/*.md .

# Commit and push
git add .
git commit -m "Add comprehensive wiki documentation"
git push origin master

# Cleanup
cd ..
rm -rf temp-wiki

echo "Wiki pages uploaded successfully!"
```

Usage:
```bash
chmod +x upload-wiki.sh
./upload-wiki.sh
```

## Wiki Pages Included

1. **Home.md** - Main landing page with navigation
2. **Getting-Started.md** - Installation and setup guide
3. **Project-Structure.md** - Detailed explanation of directory layout
4. **Basic-Workflow.md** - Day-to-day research workflow
5. **R-Setup.md** - Setting up R with radian in VS Code
6. **Stata-MATLAB-Integration.md** - Working with Stata and MATLAB
7. **Overleaf-Integration.md** - Syncing with Overleaf
8. **Troubleshooting.md** - Common issues and solutions

## Additional Pages to Create Later

You may want to add these pages later:

- **Installation-Guide.md** - Detailed software installation
- **VS-Code-Setup.md** - VS Code configuration and extensions
- **Git-Configuration.md** - Git setup and best practices
- **Python-Environment.md** - Managing Python environments
- **Data-Management.md** - Best practices for data handling
- **Running-Analysis.md** - How to run analysis scripts
- **Tables-and-Figures.md** - Creating publication-ready outputs
- **LaTeX-Documents.md** - Working with LaTeX files
- **Git-Basics.md** - Git fundamentals
- **GitHub-Workflow.md** - Using GitHub features
- **Branching-Strategy.md** - Git branching best practices
- **Pull-Requests.md** - Creating and reviewing PRs
- **GitHub-Copilot.md** - Using Copilot effectively
- **VS-Code-Chat-Modes.md** - AI chat features
- **MCP-Setup.md** - Model Context Protocol configuration
- **AI-Best-Practices.md** - Guidelines for AI-assisted research
- **Makefile-Automation.md** - Understanding and customizing Makefile

## Customization

Feel free to:
- Edit any page to match your specific setup
- Add your institution's name/logo
- Include project-specific examples
- Add screenshots or diagrams
- Link to additional resources

## Maintaining the Wiki

After initial setup:

```bash
# Edit wiki files locally in wiki/ directory
vim wiki/Getting-Started.md

# Update wiki repository
cd AI_workshop.wiki
git pull
cp ../wiki/Getting-Started.md .
git add Getting-Started.md
git commit -m "Update getting started guide"
git push
```

## Wiki Formatting Tips

GitHub wikis support:
- Markdown syntax
- Code blocks with syntax highlighting
- Tables
- Links between wiki pages: `[Page Title](Page-Name)`
- Images: Upload via web interface or use external URLs
- Emoji: `:heavy_check_mark:` → ✔️

## Making Wiki Public

GitHub wikis are public by default for public repositories. To make wiki editable by collaborators:

1. Go to repository Settings
2. Scroll to "Features" section
3. Check "Restrict editing to collaborators only" if desired

## Next Steps

1. Upload these wiki pages to your GitHub repository
2. Review and customize content for your specific needs
3. Add additional pages as your project grows
4. Keep wiki updated as you improve the workflow
5. Encourage students/collaborators to contribute improvements

---

**Note:** This wiki directory is separate from the GitHub wiki and serves as source files. The GitHub wiki is a separate Git repository that needs to be populated with these files.
