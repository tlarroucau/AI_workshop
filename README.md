# Research Project Template: Git, GitHub, and Agentic AI Workshop

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This repository serves as a **template for reproducible research projects** created by **Tomas Larroucau** and accompanies the workshop: *"Git, GitHub, and VS Code: Agentic AI for Project Management and Research Productivity."*

## 🎯 Purpose

This template demonstrates best practices for:
- **Version control** with Git and GitHub
- **Reproducible data analysis** workflows
- **Integration of AI coding agents** (GitHub Copilot, local AI assistants)
- **Collaborative research** through issues, pull requests, and project boards
- **Automated workflows** for analysis and document compilation

## 📁 Repository Structure

```
AI_workshop/
├── AGENTS.md                      # Instructions for AI coding agents
├── Makefile                       # Automation workflow
├── README.md                      # This file
│
├── .github/                       # GitHub-specific files
│   ├── copilot-instructions.md   # Copilot workspace configuration
│   ├── prompts/                  # Reusable prompt files
│   └── skills/                   # Agent skills (e.g., YouTube transcript fetcher)
│
├── data/                          # Raw and processed data
│   ├── raw/                      # Original data files (never modify!)
│   │   ├── generate_data.py      # Data generation script
│   │   └── sample_data.csv       # Sample dataset
│   └── processed/                # Cleaned/transformed data (gitignored)
│
├── scripts/                       # Analysis and processing scripts
│   ├── analysis.py               # Main analysis pipeline
│   ├── utils.py                  # Helper functions
│   └── requirements.txt          # Python dependencies
│
├── output/                        # Generated outputs (gitignored, rebuilt via make)
│   ├── figures/                  # Plots and visualizations
│   │   ├── distributions.png
│   │   ├── outcome_by_treatment.png
│   │   └── scatter_income_outcome.png
│   └── tables/                   # LaTeX-formatted tables
│       ├── balance_table.tex
│       ├── regression_results.tex
│       └── summary_statistics.tex
│
└── tex/                           # LaTeX documents
    ├── paper/                    # Research paper
    │   ├── paper.tex
    │   └── references.bib
    └── slides/                   # Presentation slides
        └── workshop_slides.tex
```

**Key principle:** Everything in `output/` is regenerated from scripts - never edit manually!

## 🚀 Quick Start

### Workshop Prerequisites

To fully participate in the workshop and follow the hands-on exercises, you will need:

**1. Accounts**
- **GitHub Account:** Create a free account at [github.com](https://github.com).
- **GitHub Education (Recommended):** Students and faculty should apply for the [GitHub Student Developer Pack](https://education.github.com/pack) to upgrade to Copilot Pro features. *Note: Copilot is now free, but the Education pack unlocks advanced models and higher limits.*

**2. Software**
- **Visual Studio Code:** Download and install from [code.visualstudio.com](https://code.visualstudio.com).
- **Git:** Download and install from [git-scm.com](https://git-scm.com/downloads).
  - *Windows Users:* We recommend installing "Git for Windows" which includes Git Bash.
  - *Mac Users:* Git often comes pre-installed, or can be installed via Xcode command line tools (`xcode-select --install`).

**3. VS Code Extensions**
- **GitHub Copilot:** Search for "GitHub Copilot" in the VS Code Extensions view (Ctrl+Shift+X) and install. *Required for Module I & II.*
- Sign in to your GitHub account within VS Code to activate.

**4. Module II: Agentic AI Setup**
- **MCP GitHub Server:** We will configure the Model Context Protocol (MCP) to connect AI agents with your GitHub repository. Ensure you have your GitHub credentials ready.

### Project Requirements (For Code Execution)

To run the analysis scripts and compile the documents locally:

- **Python 3.8+** (Anaconda distribution recommended)
- **LaTeX Distribution** (TeXLive, MikTeX, or MacTeX)
- **Make Utility** (Optional, for automation)

### Installation

1. **Clone this repository:**
   ```bash
   git clone <your-repo-url>
   cd AI_workshop
   ```

2. **Install Python dependencies:**
   ```bash
   pip install -r scripts/requirements.txt
   ```

3. **Run the complete workflow:**
   ```bash
   make all
   ```

## 🔧 Makefile Targets

| Target | Description |
|--------|-------------|
| `make data` | Generate/process sample data |
| `make analysis` | Run statistical analysis |
| `make figures` | Generate plots and visualizations |
| `make tables` | Create LaTeX tables |
| `make update-outputs` | Copy analysis outputs to paper/slides directories |
| `make paper` | Compile research paper PDF |
| `make slides` | Compile presentation slides |
| `make all` | Run complete pipeline |
| `make clean` | Remove generated files |

## 📊 Workflow Example

```bash
# 1. Process data
make data

# 2. Run analysis and update outputs
make update-outputs

# 3. Compile paper and slides
make paper slides
```

## 🤖 Working with AI Agents

This repository includes instructions for AI coding agents:

- **`.github/copilot-instructions.md`** - GitHub Copilot workspace instructions
- **`AGENTS.md`** - General AI agent guidelines for this project

These files help AI assistants understand:
- Project structure and conventions
- Code style and patterns
- Common workflows and tasks
- Domain-specific context

## 🎓 Workshop Modules

### Module I: Git, GitHub, and VS Code Fundamentals
- VS Code as an integrated development environment
- Git basics: commits, branches, merges
- GitHub workflows: pull requests, issues, project boards
- Collaborative development practices

### Module II: Agentic AI Integration
- VS Code Chat modes: Ask, Edit, Agent
- GitHub Copilot in the cloud and locally
- AI-assisted code review and refactoring
- Complementary tools: Refine, NotebookLM, Elicit

## 📝 Using This Template

1. **Click "Use this template"** on GitHub to create your own repository
2. **Update** `README.md` with your project details
3. **Replace** sample data with your actual data
4. **Modify** analysis scripts for your research questions
5. **Customize** LaTeX templates for your paper/presentation

## 🤝 Contributing

This is a teaching template. Contributions welcome via:
- **Issues:** Report bugs or suggest improvements
- **Pull Requests:** Submit enhancements
- **Discussions:** Share feedback or use cases

## 📚 Additional Resources

- [Workshop Slides](tex/slides/workshop_slides.pdf) (after compilation)
- [Git Documentation](https://git-scm.com/doc)
- [GitHub Guides](https://guides.github.com/)
- [VS Code Documentation](https://code.visualstudio.com/docs)
- [GitHub Copilot Docs](https://docs.github.com/en/copilot)

## 🧪 Issue-Driven Development Demo

This project demonstrates the use of GitHub issues for managing development tasks. Issue #12 was used to test the workflow during class.

This section was added as part of resolving issue #12.

## 📄 License

MIT License - Feel free to use this template for your research projects.

## 👤 Author

Template created by Tomas Larroucau for ASU's AI Strategic Plan workshop series.

---

**Happy Researching! 🔬**
