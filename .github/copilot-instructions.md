# GitHub Copilot Workspace Instructions

## Project Context
This is a **reproducible research project template** for the ASU workshop on Git, GitHub, and Agentic AI. It demonstrates end-to-end workflows from data analysis to paper compilation.

## Code Style & Patterns

### Python
- Use **pandas** for data manipulation, **matplotlib/seaborn** for plots
- Include **type hints** and **NumPy-style docstrings** for all functions
- Output figures as both PDF and PNG to `output/figures/`
- Output LaTeX tables to `output/tables/` using `booktabs` formatting
- Follow PEP 8, use descriptive variable names

### LaTeX
- Use `booktabs` for tables (no vertical lines)
- Beamer slides use `\frametitle` and bullet points
- Include figures via `\includegraphics{output/figures/filename.pdf}`
- Input tables via `\input{output/tables/filename.tex}`

## Key Workflows

### Data Pipeline
```
data/raw/*.csv → scripts/analysis.py → output/ → tex/
```
- Raw data is immutable
- All transformations in Python scripts
- Outputs regenerated via `make all`

### Common Tasks
- **New analysis**: Add to `scripts/analysis.py`, update Makefile target
- **New figure**: Save to `output/figures/`, use `plt.savefig()` for PDF+PNG
- **New table**: Generate LaTeX in `output/tables/`, use `df.to_latex()`
- **Build everything**: Run `make all` from repo root

## Project Structure
- `data/raw/`: Original CSV files (committed)
- `scripts/`: Python analysis code
- `output/`: Generated figures and tables (gitignored, rebuilt)
- `tex/paper/`: Research paper LaTeX source
- `tex/slides/`: Beamer presentation source

## Important Notes
- This is a **teaching template** - prioritize clarity over brevity
- Code should be **well-commented** for students new to these tools
- Always test with `make clean && make all` before committing
- Use issue-driven development: create issue → branch → PR → merge
