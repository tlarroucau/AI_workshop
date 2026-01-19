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
- Include figures via `\includegraphics{figures/filename.pdf}`
- Input tables via `\input{tables/filename.tex}`
- Note: figures and tables are copied to `tex/{paper,slides}/{figures,tables}` by `make update-outputs`

## Key Workflows

### Data Pipeline
```
data/raw/*.csv → scripts/analysis.py → output/ → tex/{paper,slides}/
```
- Raw data is immutable
- All transformations in Python scripts
- Outputs regenerated and copied via `make update-outputs` or `make all`

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
- `.github/prompts/`: Reusable prompt files (e.g., summarization)
- `.github/skills/`: Agent skills (e.g., YouTube transcript fetcher)

## Agent Capabilities
- **Skills**: This repo includes a `youtube-transcript` skill. You can ask "Fetch the transcript for [video_id]" to retrieve content from YouTube videos.
- **Prompts**: Use prompt files in `.github/prompts/` for common tasks like "Summarize Text".

## Important Notes
- This is a **teaching template** - prioritize clarity over brevity
- Code should be **well-commented** for students new to these tools
- Always test with `make clean && make all` before committing
- Use issue-driven development: create issue → branch → PR → merge
