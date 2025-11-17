# Getting Started

This guide will help you set up and start using the research project template.

## Prerequisites

Before you begin, ensure you have:
- [ ] A GitHub account (free for students at [education.github.com](https://education.github.com))
- [ ] Git installed on your computer
- [ ] VS Code installed
- [ ] Python 3.8+ installed (Anaconda recommended)

## Step 1: Clone the Repository

```bash
# Clone the template repository
git clone https://github.com/tlarroucau/AI_workshop.git

# Navigate to the directory
cd AI_workshop
```

Or fork the repository first if you want your own copy:
1. Go to https://github.com/tlarroucau/AI_workshop
2. Click "Fork" in the top right
3. Clone your forked repository

## Step 2: Set Up Python Environment

### Option A: Using Conda (Recommended)

```bash
# Create a new environment
conda create -n research python=3.10

# Activate the environment
conda activate research

# Install dependencies
pip install -r scripts/requirements.txt
```

### Option B: Using venv

```bash
# Create virtual environment
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (Mac/Linux)
source venv/bin/activate

# Install dependencies
pip install -r scripts/requirements.txt
```

## Step 3: Open in VS Code

```bash
# Open the project folder
code .
```

Or use File → Open Folder in VS Code.

## Step 4: Test the Workflow

Run the complete pipeline to verify everything works:

```bash
make all
```

This will:
1. Generate/process data
2. Run analysis scripts
3. Create figures and tables
4. Compile the paper and slides

## Step 5: Explore the Project

Key files to review:
- `README.md` - Project overview
- `Makefile` - Automation commands
- `scripts/analysis.py` - Main analysis code
- `tex/paper/paper.tex` - Paper template
- `.github/copilot-instructions.md` - AI agent guidance

## Next Steps

- Read the [Project Structure](Project-Structure) guide
- Learn about the [Basic Workflow](Basic-Workflow)
- Set up [VS Code extensions](VS-Code-Setup)
- Configure [Git](Git-Configuration)

## Common First-Time Issues

### Issue: Python not found
**Solution:** Make sure Python is in your PATH or use the full path to the Python executable.

### Issue: LaTeX compilation fails
**Solution:** Install a LaTeX distribution (TeX Live, MiKTeX, or MacTeX).

### Issue: Make command not found (Windows)
**Solution:** Install Make for Windows or use Git Bash.

## Getting Help

- Check [Troubleshooting](Troubleshooting)
- Review workshop [slides](../tex/slides/)
- Open an [issue on GitHub](https://github.com/tlarroucau/AI_workshop/issues)
