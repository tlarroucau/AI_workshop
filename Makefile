# Makefile for Research Project Template
# This automates the complete workflow from data analysis to document compilation

.PHONY: all clean data analysis figures tables paper slides help

# Python interpreter
PYTHON := python3

# Directories
DATA_DIR := data
SCRIPTS_DIR := scripts
OUTPUT_DIR := output
FIGURES_DIR := $(OUTPUT_DIR)/figures
TABLES_DIR := $(OUTPUT_DIR)/tables
TEX_PAPER_DIR := tex/paper
TEX_SLIDES_DIR := tex/slides

# Scripts
ANALYSIS_SCRIPT := $(SCRIPTS_DIR)/analysis.py

# Output files
FIGURES := $(FIGURES_DIR)/outcome_by_treatment.pdf \
           $(FIGURES_DIR)/scatter_income_outcome.pdf \
           $(FIGURES_DIR)/distributions.pdf

TABLES := $(TABLES_DIR)/summary_statistics.tex \
          $(TABLES_DIR)/balance_table.tex \
          $(TABLES_DIR)/regression_results.tex

# LaTeX files
PAPER_TEX := $(TEX_PAPER_DIR)/paper.tex
SLIDES_TEX := $(TEX_SLIDES_DIR)/workshop_slides.tex
PAPER_PDF := $(TEX_PAPER_DIR)/paper.pdf
SLIDES_PDF := $(TEX_SLIDES_DIR)/workshop_slides.pdf

# Default target
all: analysis paper slides
	@echo "======================================"
	@echo "Complete workflow finished!"
	@echo "======================================"
	@echo "Papers:"
	@echo "  - $(PAPER_PDF)"
	@echo "  - $(SLIDES_PDF)"
	@echo ""

# Help target
help:
	@echo "Available targets:"
	@echo "  make all       - Run complete pipeline (analysis + documents)"
	@echo "  make data      - Generate/check sample data"
	@echo "  make analysis  - Run statistical analysis"
	@echo "  make figures   - Generate figures only"
	@echo "  make tables    - Generate tables only"
	@echo "  make paper     - Compile research paper"
	@echo "  make slides    - Compile presentation slides"
	@echo "  make clean     - Remove all generated files"
	@echo "  make help      - Show this help message"

# Generate/verify data exists
data:
	@echo "Checking data availability..."
	@if [ ! -f "$(DATA_DIR)/raw/sample_data.csv" ]; then \
		echo "Generating sample data..."; \
		cd $(DATA_DIR)/raw && $(PYTHON) generate_data.py; \
	else \
		echo "Sample data already exists."; \
	fi

# Run complete analysis (generates figures and tables)
analysis: data
	@echo "======================================"
	@echo "Running analysis pipeline..."
	@echo "======================================"
	@mkdir -p $(FIGURES_DIR) $(TABLES_DIR)
	@cd $(SCRIPTS_DIR) && $(PYTHON) analysis.py

# Generate figures only
figures: data
	@echo "Generating figures..."
	@mkdir -p $(FIGURES_DIR)
	@cd $(SCRIPTS_DIR) && $(PYTHON) analysis.py

# Generate tables only
tables: data
	@echo "Generating tables..."
	@mkdir -p $(TABLES_DIR)
	@cd $(SCRIPTS_DIR) && $(PYTHON) analysis.py

# Compile research paper
paper: analysis
	@echo "======================================"
	@echo "Compiling research paper..."
	@echo "======================================"
	@cd $(TEX_PAPER_DIR) && \
		pdflatex -interaction=nonstopmode paper.tex > /dev/null && \
		bibtex paper > /dev/null 2>&1 || true && \
		pdflatex -interaction=nonstopmode paper.tex > /dev/null && \
		pdflatex -interaction=nonstopmode paper.tex > /dev/null
	@echo "Paper compiled: $(PAPER_PDF)"

# Compile presentation slides
slides: analysis
	@echo "======================================"
	@echo "Compiling presentation slides..."
	@echo "======================================"
	@cd $(TEX_SLIDES_DIR) && \
		pdflatex -interaction=nonstopmode workshop_slides.tex > /dev/null && \
		pdflatex -interaction=nonstopmode workshop_slides.tex > /dev/null
	@echo "Slides compiled: $(SLIDES_PDF)"

# Clean generated files
clean:
	@echo "Cleaning generated files..."
	@rm -f $(FIGURES_DIR)/*.pdf $(FIGURES_DIR)/*.png
	@rm -f $(TABLES_DIR)/*.tex
	@rm -f $(DATA_DIR)/processed/*
	@cd $(TEX_PAPER_DIR) && rm -f *.aux *.bbl *.blg *.log *.out *.pdf *.synctex.gz *.fls *.fdb_latexmk
	@cd $(TEX_SLIDES_DIR) && rm -f *.aux *.log *.nav *.out *.pdf *.snm *.toc *.vrb *.synctex.gz *.fls *.fdb_latexmk
	@echo "Clean complete!"

# Install Python dependencies
install:
	@echo "Installing Python dependencies..."
	@pip install -r $(SCRIPTS_DIR)/requirements.txt
	@echo "Dependencies installed!"

# Check Python environment
check-env:
	@echo "Checking Python environment..."
	@$(PYTHON) --version
	@echo "Checking required packages..."
	@$(PYTHON) -c "import pandas; print('pandas:', pandas.__version__)"
	@$(PYTHON) -c "import numpy; print('numpy:', numpy.__version__)"
	@$(PYTHON) -c "import matplotlib; print('matplotlib:', matplotlib.__version__)"
	@$(PYTHON) -c "import seaborn; print('seaborn:', seaborn.__version__)"
	@$(PYTHON) -c "import scipy; print('scipy:', scipy.__version__)"
	@$(PYTHON) -c "import statsmodels; print('statsmodels:', statsmodels.__version__)"
	@echo "Environment check complete!"

# Test analysis script without full run
test:
	@echo "Testing analysis script..."
	@cd $(SCRIPTS_DIR) && $(PYTHON) -m py_compile analysis.py utils.py
	@echo "Syntax check passed!"
