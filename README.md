# Research Project Template: Git, GitHub, and Agentic AI Workshop

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This repository serves as a **template for reproducible research projects** and accompanies the ASU workshop: *"Git, GitHub, and VS Code: Agentic AI for Project Management and Research Productivity."*

## 🎯 Purpose

This template demonstrates best practices for:
- **Version control** with Git and GitHub
- **Reproducible data analysis** workflows
- **Integration of AI coding agents** (GitHub Copilot, local AI assistants)
- **Collaborative research** through issues, pull requests, and project boards
- **Automated workflows** for analysis and document compilation

## 📁 Repository Structure

```
.
├── data/                    # Raw and processed data
│   ├── raw/                # Original data files (CSV)
│   └── processed/          # Cleaned/transformed data
├── scripts/                # Analysis and processing scripts
│   ├── analysis.py         # Main analysis script
│   ├── utils.py           # Helper functions
│   └── requirements.txt   # Python dependencies
├── output/                 # Generated outputs
│   ├── figures/           # Plots and visualizations
│   └── tables/            # LaTeX tables
├── tex/                    # LaTeX documents
│   ├── paper/             # Research paper
│   └── slides/            # Presentation slides
├── .github/               # GitHub-specific files
│   └── copilot-instructions.md
├── AGENTS.md              # Instructions for AI coding agents
├── Makefile               # Automation workflow
└── README.md              # This file
```

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- LaTeX distribution (TeXLive, MiKTeX, or MacTeX)
- Make utility

### Installation

1. **Clone this repository:**
   ```bash
   git clone <your-repo-url>
   cd AI_worshop
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
| `make paper` | Compile research paper PDF |
| `make slides` | Compile presentation slides |
| `make all` | Run complete pipeline |
| `make clean` | Remove generated files |

## 📊 Workflow Example

```bash
# 1. Process data
make data

# 2. Run analysis and generate outputs
make analysis

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

## 📄 License

MIT License - Feel free to use this template for your research projects.

## 👤 Author

Template created for ASU's AI Strategic Plan workshop series.

---

**Happy Researching! 🔬**
