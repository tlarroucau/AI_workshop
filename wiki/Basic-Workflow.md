# Basic Workflow

Learn the typical day-to-day workflow for research projects using this template.

## The Standard Research Cycle

```
1. Create Issue → 2. Create Branch → 3. Develop → 4. Test → 5. Commit → 6. Pull Request → 7. Merge
```

## Detailed Workflow

### 1. Create an Issue

Track your work with GitHub Issues:

```bash
# On GitHub, create a new issue
Title: "Add robustness checks for Model 2"
Description: Include regression with clustered standard errors
Label: enhancement
```

Or use AI agent with MCP:
```
Ask Copilot: "Create an issue for adding clustered SE robustness checks"
```

### 2. Create a Feature Branch

Avoid working directly on `main`:

```bash
# Create and switch to new branch
git checkout -b feature/clustered-se

# Or reference the issue number
git checkout -b issue-42-robustness
```

### 3. Develop Your Analysis

Edit files in your branch:

```python
# scripts/analysis.py
def run_robustness_checks(data):
    """
    Compute regression with clustered standard errors.
    
    Parameters
    ----------
    data : pd.DataFrame
        Input dataset
        
    Returns
    -------
    results : RegressionResults
        Model estimation results
    """
    # Your code here
    pass
```

Use AI assistance:
- **Copilot Chat**: "Add a function to compute clustered standard errors"
- **Inline suggestions**: Start typing and accept suggestions with Tab
- **Edit mode**: Select code and ask AI to refactor

### 4. Test Your Changes

Run the pipeline frequently:

```bash
# Run just the analysis
make analysis

# Regenerate figures
make figures

# Full pipeline
make all
```

Verify outputs:
- Check `output/figures/` for plots
- Review `output/tables/` for LaTeX tables
- Compile paper: `make paper`

### 5. Commit Your Changes

Make atomic commits (one logical change):

```bash
# Check what changed
git status

# Stage specific files
git add scripts/analysis.py

# Or stage all changes
git add .

# Commit with descriptive message
git commit -m "Add clustered SE robustness checks

- Implement robust_regression() function
- Add diagnostic plots
- Update summary table
- Addresses #42"
```

**Good commit messages:**
- Start with imperative verb: "Add", "Fix", "Update", "Remove"
- Reference issues: "Closes #42" or "Addresses #42"
- Explain *why*, not just *what*

### 6. Push and Create Pull Request

```bash
# Push branch to GitHub
git push -u origin feature/clustered-se
```

On GitHub:
1. Click "Compare & pull request"
2. Add description of changes
3. Link to related issue
4. Request review from collaborators
5. Wait for CI checks (if configured)

Or use AI agent:
```
Ask Copilot: "Create PR for this branch linking to issue #42"
```

### 7. Review and Merge

**Review checklist:**
- [ ] Code runs without errors (`make all`)
- [ ] Outputs look correct
- [ ] Code follows project conventions
- [ ] Docstrings added/updated
- [ ] No sensitive data committed

**Merge options:**
- **Squash and merge**: Clean history (recommended)
- **Merge commit**: Preserve all commits
- **Rebase**: Linear history

After merging:
```bash
# Switch back to main
git checkout main

# Pull latest changes
git pull

# Delete local branch
git branch -d feature/clustered-se
```

## Daily Commands

### Starting work
```bash
# Update your local main branch
git checkout main
git pull

# Create feature branch
git checkout -b feature/my-feature
```

### During work
```bash
# Check status
git status

# See changes
git diff

# Test code
make all

# Commit often
git add .
git commit -m "Descriptive message"
```

### Finishing work
```bash
# Push changes
git push -u origin feature/my-feature

# Create PR on GitHub
# Review and merge
```

## Using the Makefile

The Makefile automates common tasks:

```bash
make all        # Complete pipeline (recommended)
make data       # Process data only
make analysis   # Run analysis scripts
make figures    # Generate plots
make tables     # Create LaTeX tables
make paper      # Compile paper PDF
make slides     # Compile presentation
make clean      # Remove generated files
```

**Pro tip:** Always run `make clean && make all` before committing to ensure reproducibility.

## Working with AI Assistants

### GitHub Copilot Chat

**Ask Mode:**
```
"How does this regression function work?"
"What's the best way to handle missing data here?"
```

**Edit Mode:**
```
Select code → "Refactor this to use pandas groupby"
```

**Agent Mode:**
```
"@workspace add type hints to all functions in analysis.py"
```

**Note:** We can use Local, Background, and Cloud agents in parallel.

### Using MCP

If MCP is configured:
```
"Create an issue for adding panel regression analysis and add it to the project board"
```

The AI agent will:
1. Create GitHub issue
2. Add to project board
3. Suggest implementation approach

## Best Practices

### ✅ DO
- Commit early and often
- Write descriptive commit messages
- Test before committing (`make all`)
- Use branches for all changes
- Pull latest main before starting new work
- Keep commits atomic (one logical change)

### ❌ DON'T
- Commit directly to main
- Commit generated outputs
- Use vague messages like "update" or "fix"
- Commit large binary files
- Commit API keys or passwords
- Mix unrelated changes in one commit

## Troubleshooting Common Issues

### "I forgot to create a branch"
```bash
# Stash your changes
git stash

# Create and switch to branch
git checkout -b feature/my-feature

# Restore changes
git stash pop
```

### "I need to update from main"
```bash
# Commit your current work first
git add .
git commit -m "Work in progress"

# Update from main
git checkout main
git pull
git checkout feature/my-feature
git merge main
```

### "Make fails"
Check the error message and:
1. Verify Python environment is activated
2. Check data files exist in `data/raw/`
3. Review the specific target in Makefile
4. Check for syntax errors in scripts

## Next Steps

- Understand [Git Basics](Git-Basics) in detail
- Learn about [GitHub Workflow](GitHub-Workflow)
- Explore [AI-Assisted Development](GitHub-Copilot)
- Master [Makefile Automation](Makefile-Automation)
