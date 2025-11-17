# Overleaf Integration

Integrating Overleaf with your VS Code and Git workflow.

## Overview

Overleaf is a popular online LaTeX editor with real-time collaboration. While this template uses local LaTeX compilation in VS Code, you can integrate with Overleaf if needed for collaboration.

## Integration Methods

### Option 1: Git Sync (Recommended)

Overleaf Pro accounts can sync with Git repositories.

#### Setup

1. **In Overleaf:**
   - Create new project or open existing
   - Go to Menu → Git
   - Copy the Git URL (looks like: `https://git.overleaf.com/your-project-id`)

2. **In VS Code terminal:**
   ```bash
   # Add Overleaf as remote
   git remote add overleaf https://git.overleaf.com/your-project-id
   
   # Verify remotes
   git remote -v
   ```

#### Workflow

**Push changes to Overleaf:**
```bash
# Commit your changes locally
git add tex/paper/paper.tex
git commit -m "Update introduction"

# Push to both GitHub and Overleaf
git push origin main
git push overleaf main
```

**Pull changes from Overleaf:**
```bash
# Pull collaborator changes from Overleaf
git pull overleaf main

# Push to GitHub
git push origin main
```

**Automated sync:**

Create a git alias in `.git/config`:
```ini
[alias]
    sync-all = !git pull overleaf main && git push origin main && git push overleaf main
```

Usage:
```bash
git sync-all
```

### Option 2: Dropbox Sync

For Overleaf Free accounts (no Git access).

#### Setup

1. **Create Dropbox folder:**
   ```bash
   # Create a Dropbox sync folder
   mkdir ~/Dropbox/Overleaf-Sync
   ```

2. **Link to Overleaf:**
   - In Overleaf: Menu → Sync → Dropbox
   - Authorize Dropbox access
   - Choose sync folder

3. **Create symbolic link in project:**
   ```bash
   # Link paper directory to Dropbox
   ln -s ~/Dropbox/Overleaf-Sync/YourProject tex/paper-overleaf
   ```

#### Workflow

**Limitations:**
- ⚠️ **Sync lag**: Changes may take minutes to sync
- ⚠️ **Conflict potential**: Simultaneous edits can cause conflicts
- ⚠️ **One-way recommended**: Edit in Overleaf OR locally, not both

**Best practice:**
```bash
# Work locally
vim tex/paper/paper.tex

# Manually copy to Dropbox folder when ready
cp tex/paper/paper.tex ~/Dropbox/Overleaf-Sync/YourProject/

# Or use rsync for entire directory
rsync -av tex/paper/ ~/Dropbox/Overleaf-Sync/YourProject/
```

### Option 3: Download/Upload Manually

For occasional collaboration.

1. **Export from Overleaf:**
   - Menu → Source (download .zip)
   - Extract to `tex/paper/`
   
2. **Work locally**, then

3. **Upload to Overleaf:**
   - Create new version on Overleaf
   - Upload modified files

## Recommended Setup: Hybrid Approach

**For solo work:**
- Use VS Code + LaTeX Workshop extension
- Compile locally with `make paper`
- Commit to Git normally

**For collaboration:**
- Create Overleaf project linked via Git
- Collaborators edit in Overleaf
- You sync changes via Git
- Compile locally for final version

## LaTeX Workshop Extension (Local Alternative)

Instead of Overleaf, use LaTeX Workshop in VS Code:

### Installation

```bash
# Install extension
code --install-extension James-Yu.latex-workshop
```

### Features

- **Live preview**: See PDF while editing
- **Auto-compile**: Saves trigger compilation
- **Forward/inverse search**: Click PDF to jump to code and vice versa
- **IntelliSense**: Auto-complete for commands and references
- **Syntax highlighting**: Better than Overleaf

### Configuration

Add to `.vscode/settings.json`:

```json
{
    "latex-workshop.latex.autoBuild.run": "onSave",
    "latex-workshop.latex.recipe.default": "latexmk",
    "latex-workshop.view.pdf.viewer": "tab",
    "latex-workshop.latex.outDir": ".",
    "latex-workshop.latex.tools": [
        {
            "name": "pdflatex",
            "command": "pdflatex",
            "args": [
                "-synctex=1",
                "-interaction=nonstopmode",
                "-file-line-error",
                "%DOC%"
            ]
        },
        {
            "name": "bibtex",
            "command": "bibtex",
            "args": ["%DOCFILE%"]
        }
    ],
    "latex-workshop.latex.recipes": [
        {
            "name": "pdflatex -> bibtex -> pdflatex*2",
            "tools": ["pdflatex", "bibtex", "pdflatex", "pdflatex"]
        }
    ]
}
```

### Usage

1. Open `paper.tex` in VS Code
2. Save file (Ctrl+S) to trigger compilation
3. View PDF in side panel (Ctrl+Alt+V)
4. Click in PDF to jump to source (Ctrl+Click)

## Trade-offs: Overleaf vs Local

### Overleaf Advantages
- ✅ Real-time collaboration
- ✅ No LaTeX installation needed
- ✅ Version history built-in
- ✅ Cross-platform (works anywhere)
- ✅ Package management automatic

### Overleaf Disadvantages
- ❌ Requires internet connection
- ❌ Sync lag with Dropbox method
- ❌ Limited control over compilation
- ❌ Git sync requires Pro account ($)
- ❌ Slower compilation than local

### Local VS Code Advantages
- ✅ Fast compilation
- ✅ Full Git integration
- ✅ Works offline
- ✅ More control (custom builds)
- ✅ Better for large projects
- ✅ AI assistance (Copilot)

### Local VS Code Disadvantages
- ❌ Requires LaTeX installation
- ❌ No built-in real-time collaboration
- ❌ Setup complexity for beginners

## Best Practice Workflow

### For Individual Research

```bash
# Use local LaTeX Workshop
1. Edit in VS Code
2. Auto-compile on save
3. Commit to Git
4. Push to GitHub
```

### For Collaborative Papers

```bash
# Hybrid: Overleaf + Git
1. Create Overleaf project (Git-enabled)
2. Add as remote: git remote add overleaf <url>
3. Collaborators edit in Overleaf
4. You pull changes: git pull overleaf main
5. Make final edits locally
6. Push back: git push overleaf main
7. Compile locally for submission: make paper
```

### For Student Collaborators

```bash
# Use Overleaf, you sync
1. Give students Overleaf link
2. Students edit in Overleaf
3. You pull via Git periodically
4. Compile locally for quality control
5. Push polished version back
```

## Handling Merge Conflicts

When syncing Overleaf via Git:

```bash
# If conflict occurs
git pull overleaf main

# CONFLICT in paper.tex
# Edit file to resolve conflicts

# Look for conflict markers:
<<<<<<< HEAD
Your local changes
=======
Overleaf changes
>>>>>>> overleaf/main

# Choose which to keep or merge manually
# Then commit
git add paper.tex
git commit -m "Merge Overleaf changes"
```

## File Organization Tips

**Keep figures separate:**
```latex
% In paper.tex
\includegraphics{../../output/figures/plot.pdf}
```

**Use subfiles for large papers:**
```latex
% paper.tex
\documentclass{article}
\usepackage{subfiles}

\begin{document}
\subfile{sections/introduction}
\subfile{sections/methods}
\end{document}

% sections/introduction.tex
\documentclass[../paper.tex]{subfiles}
\begin{document}
Introduction content...
\end{document}
```

Allows collaborators to compile sections independently in Overleaf.

## Common Issues

### Issue: Overleaf can't find figures

**Problem:** Overleaf doesn't have `output/figures/` folder

**Solution 1:** Upload figures to Overleaf manually

**Solution 2:** Use relative paths that work both locally and in Overleaf:
```latex
\graphicspath{{../../output/figures/}{figures/}}
```

### Issue: Bibliography not syncing

**Problem:** `.bib` file missing in Overleaf

**Solution:** Ensure `references.bib` is committed to Git:
```bash
git add tex/paper/references.bib
git commit -m "Add bibliography file"
git push overleaf main
```

### Issue: Compilation errors in Overleaf but not locally

**Problem:** Different LaTeX versions or packages

**Solution:** Check Overleaf compiler settings:
- Menu → Compiler → Choose pdfLaTeX
- Check package versions match local

## Next Steps

- Learn [LaTeX Documents](LaTeX-Documents) best practices
- Review [Tables and Figures](Tables-and-Figures) generation
- Explore [Git Basics](Git-Basics) for version control
- Check [Troubleshooting](Troubleshooting) for common issues
