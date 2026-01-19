# AI Agent Instructions

This document provides guidance for AI coding agents (GitHub Copilot, Cursor, Cline, etc.) working in this research project repository.

## Project Overview

This is a **reproducible research project template** that demonstrates:
- Data analysis workflows in Python
- LaTeX document generation (papers and slides)
- Automated build processes via Makefile
- Git/GitHub best practices for research collaboration

## Architecture & Structure

### Data Flow
```
data/raw/*.csv → scripts/analysis.py → output/{figures,tables}/ → tex/{paper,slides}/{figures,tables}/
```

### Key Components

1. **Data Layer** (`data/`)
   - `raw/`: Immutable source data (CSV format)
   - `processed/`: Cleaned/transformed datasets
   - Never modify raw data - transformations go in scripts

2. **Analysis Layer** (`scripts/`)
   - `analysis.py`: Main analysis pipeline
   - `utils.py`: Reusable helper functions
   - All scripts output to `output/` directory

3. **Output Layer** (`output/`)
   - `figures/`: PNG/PDF plots for inclusion in papers
   - `tables/`: LaTeX-formatted tables (.tex files)
   - Gitignored (regenerated via `make`)
   - **Note:** Outputs are copied to `tex/paper/` and `tex/slides/` by the `update-outputs` Makefile target.

4. **Document Layer** (`tex/`)
   - `paper/`: Research paper source
   - `slides/`: Beamer presentation
   - Compiled PDFs go to respective directories

## Development Conventions

### Python Code Style
- **PEP 8 compliance** for code style
- **Type hints** for function signatures
- **Docstrings** using NumPy format
- **pandas** for data manipulation
- **matplotlib/seaborn** for visualization
- **statsmodels/scipy** for statistical analysis

Example function pattern:
```python
def analyze_data(df: pd.DataFrame, column: str) -> Dict[str, float]:
    """
    Compute summary statistics for a column.
    
    Parameters
    ----------
    df : pd.DataFrame
        Input dataset
    column : str
        Column name to analyze
        
    Returns
    -------
    Dict[str, float]
        Dictionary with mean, std, min, max
    """
    # Implementation
```

### File Naming
- **Snake_case** for Python files and data files: `analysis_script.py`, `sample_data.csv`
- **Descriptive names** for outputs: `regression_results.png`, `summary_stats_table.tex`
- **Date prefixes** for versioned data: `2024_11_data.csv`

### Git Workflow
- **Atomic commits**: One logical change per commit
- **Descriptive messages**: "Add regression analysis for model 2" not "Update analysis.py"
- **Branch naming**: `feature/add-robustness-checks`, `fix/data-loading-bug`
- **Issues first**: Create issue before starting work, reference in commits

### LaTeX Conventions
- **Tables**: Use `booktabs` package. Include via `\input{tables/filename.tex}`, store in `tex/{paper,slides}/tables/`
- **Figures**: Include via `\includegraphics{figures/filename.pdf}`, store in `tex/{paper,slides}/figures/`
- **Bibliography**: BibTeX format in `references.bib`
- **Slides**: Beamer with `metropolis` or `madrid` theme

## Common Tasks & Workflows

### Adding New Analysis
1. Create feature branch: `git checkout -b feature/new-analysis`
2. Update `scripts/analysis.py` or create new script
3. Test manually: `python scripts/analysis.py`
4. Update Makefile if needed
5. Run full pipeline: `make update-outputs` (to analyze and copy outputs) or `make all`
6. Commit and push, create PR

### Generating Tables for LaTeX
Tables should be generated as `.tex` files in `output/tables/` with:
- `\begin{table}` and `\caption{}` included
- `booktabs` formatting (`\toprule`, `\midrule`, `\bottomrule`)
- Proper float placement (`[htbp]`)
- Label for cross-reference (`\label{tab:results}`)

Example code:
```python
def save_latex_table(df: pd.DataFrame, filename: str, caption: str, label: str):
    """Save DataFrame as formatted LaTeX table."""
    latex_str = df.to_latex(
        index=True,
        escape=False,
        column_format='l' + 'r' * len(df.columns),
        caption=caption,
        label=label
    )
    # Add booktabs formatting
    latex_str = latex_str.replace('\\toprule', '\\toprule')
    with open(f'output/tables/{filename}', 'w') as f:
        f.write(latex_str)
```

### Creating Figures
- **Size**: 6-8 inches wide for papers, 10-12 for slides
- **DPI**: 300 for publication quality
- **Format**: Save both PNG (for preview) and PDF (for LaTeX)
- **Style**: Use consistent color palette (e.g., `seaborn` themes)

Example:
```python
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")
sns.set_palette("colorblind")

fig, ax = plt.subplots(figsize=(8, 6))
# ... plotting code ...
plt.tight_layout()
plt.savefig('output/figures/regression_plot.pdf', bbox_inches='tight')
plt.savefig('output/figures/regression_plot.png', dpi=300, bbox_inches='tight')
```

## Makefile Integration

The Makefile orchestrates the entire workflow. When adding new targets:
- Use `.PHONY` for non-file targets
- Declare dependencies clearly
- Include help text (appears in `make help`)
- Clean outputs should be in `make clean`

## Dependencies Management

### Python
All dependencies in `scripts/requirements.txt`:
```
pandas>=1.5.0
numpy>=1.23.0
matplotlib>=3.6.0
seaborn>=0.12.0
scipy>=1.9.0
statsmodels>=0.14.0
```

Update with: `pip freeze > scripts/requirements.txt` (after testing)

### LaTeX
Required packages (usually in full TeX distributions):
- `beamer` (slides)
- `booktabs` (tables)
- `graphicx` (figures)
- `natbib` or `biblatex` (references)

## Testing & Validation

Before committing analysis changes:
1. **Run full pipeline**: `make clean && make all`
2. **Check outputs**: Verify figures and tables generated correctly
3. **Compile documents**: Ensure LaTeX compiles without errors
4. **Review diffs**: `git diff` to check unintended changes

## Working with Issues

Use GitHub Issues for:
- **Feature requests**: "Add panel regression analysis"
- **Bugs**: "Data loading fails with empty CSV"
- **Documentation**: "Update README with new analysis section"
- **Questions**: "Should we use fixed or random effects?"

Issue-driven development:
1. Create issue describing task
2. Create branch referencing issue number
3. Reference issue in commits: `Closes #42`
4. Create PR linking to issue

## AI Agent Best Practices

When generating code:
- **Match existing style**: Follow conventions above
- **Add docstrings**: For all new functions
- **Update requirements**: If adding new packages
- **Test before committing**: Run the code
- **Explain changes**: Add comments for complex logic
- **Update documentation**: Modify README/AGENTS.md if needed

When assisting with debugging:
- **Check Makefile**: Issues often in build process
- **Verify paths**: Ensure relative paths work from repo root
- **Review data**: Check CSV format and column names
- **Test incrementally**: Isolate the failing component

## Project-Specific Notes

- This is a **teaching template**, so code should be clear and well-commented
- Prioritize **reproducibility** over optimization
- Include **example outputs** so students can verify their setup
- Keep **dependencies minimal** for easier installation
- Document **every step** - students may be new to these tools

## Quick Reference Commands

```bash
# Full workflow
make all

# Individual steps
make data analysis figures tables paper slides

# Clean and rebuild
make clean
make all

# Python virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r scripts/requirements.txt

# Git workflow
git checkout -b feature/my-feature
# ... make changes ...
git add .
git commit -m "Descriptive message"
git push -u origin feature/my-feature
# Create PR on GitHub
```

---

*Last updated: November 2024*
