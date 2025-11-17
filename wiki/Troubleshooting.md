# Troubleshooting

Common issues and solutions when using this research template.

## General Issues

### Make command not found (Windows)

**Problem:** `make` is not available on Windows by default.

**Solutions:**

1. **Use Git Bash** (recommended):
   - Make is included with Git for Windows
   - Open Git Bash terminal in VS Code

2. **Install Make for Windows:**
   ```powershell
   # Using Chocolatey
   choco install make
   
   # Or use Windows Subsystem for Linux (WSL)
   wsl --install
   ```

3. **Use Python script alternative:**
   Create `build.py` to replace Makefile functionality

### Python command not found

**Problem:** Python not in PATH or wrong Python version.

**Solution:**
```bash
# Check Python installation
python --version
python3 --version

# If not found, install or add to PATH
# Windows: Add Python install dir to PATH
# Mac: brew install python
# Linux: apt-get install python3

# Use full path if needed
/usr/bin/python3 scripts/analysis.py
```

### Module not found errors

**Problem:** Python packages not installed.

**Solution:**
```bash
# Ensure you're in correct environment
conda activate research  # or source venv/bin/activate

# Install requirements
pip install -r scripts/requirements.txt

# Install specific package
pip install pandas numpy matplotlib
```

## Git Issues

### "fatal: not a git repository"

**Problem:** Not in a Git repository.

**Solution:**
```bash
# Initialize Git in current directory
git init

# Or clone the repository
git clone https://github.com/tlarroucau/AI_workshop.git
```

### Merge conflicts

**Problem:** Git can't automatically merge changes.

**Solution:**
```bash
# When conflict occurs, Git marks the file
# Open the file and look for conflict markers:

<<<<<<< HEAD
Your changes
=======
Their changes
>>>>>>> branch-name

# Edit to keep desired version
# Remove conflict markers
# Stage and commit:
git add conflicted-file.py
git commit -m "Resolve merge conflict"
```

**Using VS Code:**
- Conflict files are highlighted
- Click "Accept Current Change", "Accept Incoming Change", or "Accept Both"

### Push rejected (non-fast-forward)

**Problem:** Remote has commits you don't have locally.

**Solution:**
```bash
# Pull and merge first
git pull origin main

# Resolve any conflicts
# Then push
git push origin main
```

## Makefile Issues

### "No rule to make target"

**Problem:** Makefile target doesn't exist or typo.

**Solution:**
```bash
# List available targets
make help

# Or check Makefile directly
cat Makefile

# Use correct target name
make all  # not make All
```

### Makefile fails midway

**Problem:** Error in one step breaks the pipeline.

**Solution:**
```bash
# Run individual targets to isolate issue
make data       # Just data processing
make analysis   # Just analysis
make figures    # Just figure generation

# Check error message
# Fix the problematic script
# Resume from that point
```

### Permission denied errors

**Problem:** Files or directories not writable.

**Solution:**
```bash
# Check permissions
ls -la output/

# Fix permissions (Unix/Mac/Linux)
chmod -R u+w output/

# Windows: Right-click folder → Properties → Security
```

## LaTeX Issues

### LaTeX not found

**Problem:** LaTeX distribution not installed.

**Solutions:**

**Windows:** Install MiKTeX
```powershell
choco install miktex
```

**Mac:** Install MacTeX
```bash
brew install --cask mactex
```

**Linux:** Install TeX Live
```bash
sudo apt-get install texlive-full
```

### Missing LaTeX packages

**Problem:** Compilation fails due to missing `.sty` files.

**Solutions:**

1. **Automatic installation** (MiKTeX):
   - Enabled by default
   - MiKTeX downloads packages on-demand

2. **Manual installation** (TeX Live):
   ```bash
   # Install specific package
   tlmgr install booktabs
   
   # Update all packages
   tlmgr update --all
   ```

3. **Install full distribution** to avoid issues:
   ```bash
   # Linux
   sudo apt-get install texlive-full
   ```

### Bibliography not compiling

**Problem:** Citations show as `[?]` in PDF.

**Solution:**
```bash
# Run full compilation sequence
cd tex/paper
pdflatex paper.tex
bibtex paper
pdflatex paper.tex
pdflatex paper.tex

# Or use Makefile
make paper
```

### Figures not showing in PDF

**Problem:** `\includegraphics` can't find image files.

**Solution:**
```latex
% Check file path is correct
\includegraphics{../../output/figures/plot.pdf}

% Or set graphics path
\graphicspath{{../../output/figures/}}
\includegraphics{plot.pdf}

% Verify file exists
ls output/figures/plot.pdf
```

## VS Code Issues

### Extension not working

**Problem:** VS Code extension not activating.

**Solutions:**
```bash
# Reload window
Ctrl+Shift+P → "Reload Window"

# Reinstall extension
Ctrl+Shift+X → Find extension → Uninstall → Install

# Check extension logs
Ctrl+Shift+P → "Developer: Show Logs" → Extension Host
```

### Copilot not suggesting

**Problem:** GitHub Copilot inactive or not signed in.

**Solution:**
1. Check status bar (bottom right) for Copilot icon
2. Click icon → Sign in to GitHub
3. Verify subscription at https://github.com/settings/copilot
4. Reload VS Code

### IntelliSense not working (Python)

**Problem:** Code completion not showing.

**Solution:**
```bash
# Select Python interpreter
Ctrl+Shift+P → "Python: Select Interpreter"
# Choose correct environment

# Restart language server
Ctrl+Shift+P → "Python: Restart Language Server"

# Reinstall Pylance extension
```

## Data Issues

### File not found errors

**Problem:** Scripts can't find data files.

**Solution:**
```bash
# Ensure you're in project root
pwd
# Should show .../AI_workshop

# Run scripts from project root
python scripts/analysis.py

# Not from scripts directory:
cd scripts  # ❌ Don't do this
python analysis.py  # ❌ Won't find ../data/
```

### Encoding errors (CSV files)

**Problem:** Special characters cause errors.

**Solution:**
```python
# Specify encoding when reading
import pandas as pd
df = pd.read_csv('data/raw/data.csv', encoding='utf-8')

# Or try different encodings
df = pd.read_csv('data/raw/data.csv', encoding='latin1')
```

### Memory errors with large datasets

**Problem:** `MemoryError` when loading data.

**Solution:**
```python
# Read in chunks
chunks = pd.read_csv('large_file.csv', chunksize=10000)
for chunk in chunks:
    process(chunk)

# Or use specific columns
df = pd.read_csv('file.csv', usecols=['col1', 'col2'])

# Or use data types to reduce memory
df = pd.read_csv('file.csv', dtype={'id': 'int32'})
```

## GitHub Issues

### Authentication failed

**Problem:** Can't push to GitHub.

**Solutions:**

1. **Use Personal Access Token:**
   ```bash
   # Generate token at: github.com/settings/tokens
   # Use token as password when prompted
   ```

2. **Set up SSH key:**
   ```bash
   # Generate SSH key
   ssh-keygen -t ed25519 -C "your_email@example.com"
   
   # Add to GitHub: Settings → SSH keys
   # Test connection
   ssh -T git@github.com
   ```

3. **Use credential helper:**
   ```bash
   git config --global credential.helper cache
   ```

### Can't create pull request

**Problem:** No changes between branches.

**Solution:**
```bash
# Ensure branch has commits
git log origin/main..HEAD

# If empty, make and commit changes
git add .
git commit -m "Add changes"
git push
```

## AI Assistant Issues

### Copilot suggesting wrong code

**Problem:** Suggestions don't match your coding style.

**Solution:**
- Add `.github/copilot-instructions.md` to your repo
- Be more specific in comments before code
- Use inline chat to refine suggestions
- Reject and try again with different context

### MCP not working

**Problem:** AI agent can't access GitHub/files.

**Solution:**
1. Verify MCP server installation:
   ```bash
   npx @modelcontextprotocol/server-github --version
   ```

2. Check GitHub token permissions
3. Restart VS Code
4. Check MCP configuration in Copilot settings

## Performance Issues

### VS Code slow/freezing

**Solutions:**
```bash
# Disable unused extensions
# Exclude large directories from search
# Add to .vscode/settings.json:
{
    "files.watcherExclude": {
        "**/output/**": true,
        "**/__pycache__/**": true,
        "**/venv/**": true
    },
    "search.exclude": {
        "**/output": true,
        "**/venv": true
    }
}
```

### Git operations slow

**Problem:** Large repository or many files.

**Solution:**
```bash
# Use .gitignore effectively
# Check what's tracked:
git ls-files | wc -l

# Remove large files from history if needed
git filter-branch --tree-filter 'rm -rf output/' HEAD

# Use Git LFS for large files
git lfs track "*.dta"
```

## Getting More Help

### Before asking for help:

1. ✅ Check this troubleshooting guide
2. ✅ Read error messages carefully
3. ✅ Search error message on Google/Stack Overflow
4. ✅ Review relevant wiki pages
5. ✅ Try `make clean && make all`

### When asking for help:

Include:
- Operating system (Windows/Mac/Linux)
- Error message (full text)
- What you were trying to do
- What you've already tried
- Relevant code/configuration

### Where to get help:

- **GitHub Issues:** [Open an issue](https://github.com/tlarroucau/AI_workshop/issues)
- **Stack Overflow:** Tag with `git`, `python`, `latex`, etc.
- **VS Code Docs:** [https://code.visualstudio.com/docs](https://code.visualstudio.com/docs)
- **Workshop materials:** Review slides in `tex/slides/`

## Useful Diagnostic Commands

```bash
# Check Python environment
python --version
pip list
which python

# Check Git status
git --version
git status
git remote -v
git log --oneline -5

# Check LaTeX installation
pdflatex --version
bibtex --version

# Check VS Code setup
code --version
code --list-extensions

# Verify project structure
tree -L 2  # or ls -R on Windows
pwd
```

## Emergency: Start Fresh

If everything is broken:

```bash
# 1. Backup your work
cp -r AI_workshop AI_workshop_backup

# 2. Clean generated files
rm -rf output/*
rm -rf scripts/__pycache__
find . -name "*.pyc" -delete

# 3. Reset Git (if needed)
git reset --hard origin/main

# 4. Rebuild environment
conda create -n research-new python=3.10
conda activate research-new
pip install -r scripts/requirements.txt

# 5. Test
make all
```

If still broken, clone fresh copy and migrate your changes manually.
