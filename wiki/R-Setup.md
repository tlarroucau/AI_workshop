# R Setup with Radian in VS Code

This guide explains how to set up R programming in VS Code with radian, a modern R console that provides better interactive experience than the default R terminal.

## Table of Contents

- [Why R with Radian?](#why-r-with-radian)
- [Prerequisites](#prerequisites)
- [Installation Steps](#installation-steps)
- [VS Code Configuration](#vs-code-configuration)
- [Testing Your Setup](#testing-your-setup)
- [Integration with This Project](#integration-with-this-project)
- [Common Tasks](#common-tasks)
- [Troubleshooting](#troubleshooting)
- [Additional Resources](#additional-resources)

## Why R with Radian?

**Radian** is a modern R console with several advantages over the default R terminal:

- ✅ **Syntax highlighting** in the console
- ✅ **Multiline editing** with automatic indentation
- ✅ **Improved autocomplete** with fuzzy matching
- ✅ **Vi/Emacs keybindings** support
- ✅ **Better history search** (Ctrl+R)
- ✅ **Works seamlessly** with VS Code's R extension

**Default R Console:**
```r
> x <- 1:10
> # No syntax highlighting, basic editing
```

**Radian Console:**
```r
r$> x <- 1:10  # Syntax highlighted
r$> # Advanced editing, autocomplete, multiline support
```

## Prerequisites

Before installing R and radian, ensure you have:

- [ ] **Python 3.8+** installed (for radian)
- [ ] **VS Code** installed
- [ ] **Git** (if integrating with this project's workflow)
- [ ] **Administrative privileges** (for installing R)

Check Python version:
```bash
python --version
# or
python3 --version
```

## Installation Steps

### Step 1: Install R

#### On Linux (Ubuntu/Debian)

```bash
# Add CRAN repository
sudo apt update -qq
sudo apt install --no-install-recommends software-properties-common dirmngr
wget -qO- https://cloud.r-project.org/bin/linux/ubuntu/marutter_pubkey.asc | sudo tee -a /etc/apt/trusted.gpg.d/cran_ubuntu_key.asc
sudo add-apt-repository "deb https://cloud.r-project.org/bin/linux/ubuntu $(lsb_release -cs)-cran40/"

# Install R
sudo apt install r-base r-base-dev

# Verify installation
R --version
```

#### On macOS

Using Homebrew:
```bash
# Install Homebrew if not already installed
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install R
brew install r

# Verify installation
R --version
```

Or download from [CRAN](https://cran.r-project.org/bin/macosx/).

#### On Windows

1. Download R from [CRAN](https://cran.r-project.org/bin/windows/base/)
2. Run the installer (use default settings)
3. Add R to PATH (installer option) or manually:
   - Search for "Environment Variables" in Windows
   - Edit System PATH
   - Add `C:\Program Files\R\R-4.x.x\bin` (adjust version number)

Verify installation in PowerShell:
```powershell
R --version
```

### Step 2: Install Radian

Radian requires Python, so ensure Python is installed first.

#### Using pip (Recommended)

```bash
# Install radian globally
pip install -U radian

# Or using pip3
pip3 install -U radian

# Verify installation
radian --version
```

#### Using conda

```bash
# Create a separate environment (optional)
conda create -n r-env python=3.11
conda activate r-env

# Install radian
conda install -c conda-forge radian

# Verify installation
radian --version
```

### Step 3: Install VS Code R Extension

1. Open VS Code
2. Go to Extensions (Ctrl+Shift+X)
3. Search for "R" by REditorSupport
4. Click "Install"

**Extension ID:** `REditorSupport.r`

Alternative (command line):
```bash
code --install-extension REditorSupport.r
```

### Step 4: Install Essential R Packages

Open radian and install recommended packages:

```bash
radian
```

In the R console:
```r
# Package management
install.packages("languageserver")  # Required for VS Code R extension
install.packages("httpgd")          # For plot viewing in VS Code

# Data manipulation and visualization
install.packages("tidyverse")       # dplyr, ggplot2, tidyr, etc.
install.packages("data.table")      # Fast data manipulation

# Statistical packages
install.packages("lmtest")          # Linear model diagnostics
install.packages("sandwich")        # Robust standard errors
install.packages("plm")             # Panel data models

# LaTeX table output (for this project)
install.packages("stargazer")       # Publication-ready tables
install.packages("xtable")          # LaTeX/HTML tables
install.packages("knitr")           # Dynamic reports
install.packages("kableExtra")      # Enhanced tables

# Development tools
install.packages("devtools")        # Package development
install.packages("usethis")         # Project setup utilities
```

## VS Code Configuration

### Configure R Extension to Use Radian

1. Open VS Code Settings (Ctrl+,)
2. Search for "r.rterm"
3. Set the following options:

**For Linux/macOS:**

Add to `settings.json`:
```json
{
    "r.rterm.linux": "/usr/local/bin/radian",
    "r.rterm.mac": "/usr/local/bin/radian",
    "r.rpath.linux": "/usr/bin/R",
    "r.rpath.mac": "/usr/local/bin/R",
    "r.bracketedPaste": true,
    "r.plot.useHttpgd": true
}
```

**For Windows:**

```json
{
    "r.rterm.windows": "C:\\Users\\YourUsername\\AppData\\Local\\Programs\\Python\\Python311\\Scripts\\radian.exe",
    "r.rpath.windows": "C:\\Program Files\\R\\R-4.3.2\\bin\\x64\\R.exe",
    "r.bracketedPaste": true,
    "r.plot.useHttpgd": true
}
```

**Finding radian path:**

```bash
# Linux/macOS
which radian

# Windows (PowerShell)
where.exe radian
```

**Finding R path:**

```bash
# Linux/macOS
which R

# Windows (PowerShell)
where.exe R
```

### Additional Recommended Settings

Add to `settings.json`:

```json
{
    // R extension settings
    "r.rterm.option": [
        "--no-save",
        "--no-restore",
        "--quiet"
    ],
    "r.sessionWatcher": true,
    "r.rtermSendDelay": 0,
    
    // Radian-specific
    "r.bracketedPaste": true,
    
    // Plotting
    "r.plot.useHttpgd": true,
    "r.plot.width": 800,
    "r.plot.height": 600,
    
    // Linting and formatting
    "r.lsp.diagnostics": true,
    "r.lsp.debug": false,
    
    // File associations
    "[r]": {
        "editor.defaultFormatter": "REditorSupport.r",
        "editor.formatOnSave": true,
        "editor.rulers": [80]
    },
    
    // R Markdown
    "[rmd]": {
        "editor.wordWrap": "on",
        "editor.quickSuggestions": true
    }
}
```

### Radian Configuration (Optional)

Create `~/.radian_profile` (Linux/macOS) or `%USERPROFILE%\.radian_profile` (Windows):

```python
# Radian configuration
import os

# Prompt
options(prompt = "r$> ")
options(continue = "... ")

# CRAN mirror
options(repos = c(CRAN = "https://cloud.r-project.org"))

# Editor
options(editor = "code")

# Disable startup message
options(radian.quiet = True)

# Color scheme (requires colorout package)
if (interactive()) {
    options(radian.color_scheme = "native")
    options(radian.editing_mode = "emacs")  # or "vi"
}

# Autocomplete settings
options(radian.complete_while_typing = True)
options(radian.completion_adding_spaces_around_equals = True)

# History
options(radian.history_search_no_duplicates = True)
options(radian.history_size = 10000)
```

## Testing Your Setup

### Test 1: Launch Radian from VS Code

1. Create a new R file: `test.R`
2. Add simple code:
   ```r
   x <- 1:10
   print(x)
   ```
3. Press **Ctrl+Enter** to send line to R console
4. Radian should open and execute the code

### Test 2: Interactive Console Features

In radian console, test:

```r
# Multiline editing (press Enter mid-expression)
x <- c(
  1, 2, 3,
  4, 5, 6
)

# Autocomplete (type and press Tab)
mtc<Tab>  # Should suggest mtcars

# History search (Ctrl+R)
# Type to search previous commands
```

### Test 3: Plotting

```r
# Install httpgd if not already
install.packages("httpgd")

# Test plot
library(ggplot2)
ggplot(mtcars, aes(x = wt, y = mpg)) +
  geom_point() +
  theme_minimal()
```

Plot should appear in VS Code's plot viewer.

### Test 4: R Markdown

Create `test.Rmd`:

```markdown
---
title: "Test Document"
output: html_document
---

## Test Code Chunk

```{r}
summary(cars)
```
```

Click "Knit" button or use VS Code command palette: "R: Knit".

## Integration with This Project

### Adding R to the Analysis Pipeline

If you want to include R analysis alongside Python/Stata/MATLAB:

#### Update Makefile

Add R targets to `Makefile`:

```makefile
# R analysis
R_SCRIPT := Rscript
R_FILES := scripts/analysis.R

.PHONY: r-analysis
r-analysis: $(R_FILES)
	@echo "Running R analysis..."
	$(R_SCRIPT) scripts/analysis.R

# Update main target
all: data analysis r-analysis figures tables paper slides
```

#### Create R Analysis Script

`scripts/analysis.R`:

```r
#!/usr/bin/env Rscript

# Load libraries
library(tidyverse)
library(stargazer)

# Set output directory
output_dir <- "output"
dir.create(file.path(output_dir, "figures"), showWarnings = FALSE, recursive = TRUE)
dir.create(file.path(output_dir, "tables"), showWarnings = FALSE, recursive = TRUE)

# Load data
data <- read.csv("data/raw/sample_data.csv")

# Analysis
model <- lm(outcome ~ treatment + control_var, data = data)

# Save regression table
stargazer(model,
          type = "latex",
          out = "output/tables/r_regression_results.tex",
          title = "Regression Results from R",
          label = "tab:r_results",
          header = FALSE,
          float = TRUE,
          table.placement = "htbp")

# Create and save plot
p <- ggplot(data, aes(x = treatment, y = outcome)) +
  geom_boxplot() +
  theme_minimal() +
  labs(title = "Treatment Effects",
       x = "Treatment",
       y = "Outcome")

ggsave("output/figures/r_treatment_effects.pdf", plot = p, width = 8, height = 6)
ggsave("output/figures/r_treatment_effects.png", plot = p, width = 8, height = 6, dpi = 300)

cat("R analysis complete!\n")
```

Make it executable:
```bash
chmod +x scripts/analysis.R
```

### Update requirements

Create `scripts/r_requirements.R`:

```r
# Required R packages for this project
packages <- c(
  "tidyverse",
  "stargazer",
  "xtable",
  "data.table",
  "lmtest",
  "sandwich",
  "plm",
  "knitr",
  "languageserver",
  "httpgd"
)

# Install missing packages
install_if_missing <- function(pkg) {
  if (!require(pkg, character.only = TRUE)) {
    install.packages(pkg, repos = "https://cloud.r-project.org")
  }
}

invisible(lapply(packages, install_if_missing))
cat("All required R packages are installed!\n")
```

Run once to install dependencies:
```bash
Rscript scripts/r_requirements.R
```

## Common Tasks

### Running R Scripts

**From terminal:**
```bash
Rscript scripts/analysis.R
```

**From VS Code:**
- Open R file
- Press **Ctrl+Shift+S** (Source entire file)
- Or select code and press **Ctrl+Enter** (Run selection)

### Creating Publication Tables

**Using stargazer:**

```r
library(stargazer)

# Estimate models
model1 <- lm(mpg ~ wt, data = mtcars)
model2 <- lm(mpg ~ wt + hp, data = mtcars)

# Create LaTeX table
stargazer(model1, model2,
          type = "latex",
          out = "output/tables/regression.tex",
          title = "Regression Results",
          label = "tab:regression",
          covariate.labels = c("Weight", "Horsepower"),
          dep.var.labels = "Miles per Gallon",
          header = FALSE,
          float = TRUE,
          table.placement = "htbp",
          notes = "Standard errors in parentheses.",
          notes.align = "l")
```

**Using xtable:**

```r
library(xtable)

# Summary statistics table
summary_stats <- data.frame(
  Variable = c("Treatment", "Control", "Outcome"),
  Mean = c(0.5, 10.2, 25.3),
  SD = c(0.5, 2.1, 5.4),
  Min = c(0, 5, 10),
  Max = c(1, 15, 40)
)

print(xtable(summary_stats,
             caption = "Summary Statistics",
             label = "tab:summary",
             align = c("l", "l", "r", "r", "r", "r")),
      file = "output/tables/summary_stats.tex",
      include.rownames = FALSE,
      floating = TRUE,
      table.placement = "htbp",
      booktabs = TRUE)
```

### Creating Figures

**Using ggplot2:**

```r
library(ggplot2)

# Scatter plot with regression line
p <- ggplot(mtcars, aes(x = wt, y = mpg)) +
  geom_point(size = 3, alpha = 0.6) +
  geom_smooth(method = "lm", se = TRUE, color = "blue") +
  theme_minimal(base_size = 14) +
  labs(title = "Fuel Efficiency vs. Weight",
       x = "Weight (1000 lbs)",
       y = "Miles per Gallon")

# Save for LaTeX
ggsave("output/figures/scatter.pdf", plot = p, width = 8, height = 6)
ggsave("output/figures/scatter.png", plot = p, width = 8, height = 6, dpi = 300)
```

**Using base R:**

```r
# Save as PDF
pdf("output/figures/histogram.pdf", width = 8, height = 6)
hist(mtcars$mpg, 
     main = "Distribution of MPG",
     xlab = "Miles per Gallon",
     col = "lightblue",
     border = "white")
dev.off()

# Save as PNG
png("output/figures/histogram.png", width = 800, height = 600, res = 300)
hist(mtcars$mpg, 
     main = "Distribution of MPG",
     xlab = "Miles per Gallon",
     col = "lightblue",
     border = "white")
dev.off()
```

### Working with Data

**Reading data:**

```r
# CSV
data <- read.csv("data/raw/sample_data.csv")

# Using readr (tidyverse)
library(readr)
data <- read_csv("data/raw/sample_data.csv")

# Stata files
library(haven)
data <- read_dta("data/raw/data.dta")

# Excel files
library(readxl)
data <- read_excel("data/raw/data.xlsx")
```

**Saving data:**

```r
# Processed data as CSV
write.csv(data, "data/processed/cleaned_data.csv", row.names = FALSE)

# As R data file
saveRDS(data, "data/processed/cleaned_data.rds")

# As Stata file
library(haven)
write_dta(data, "data/processed/cleaned_data.dta")
```

### R Markdown Reports

Create `reports/analysis_report.Rmd`:

```markdown
---
title: "Analysis Report"
author: "Your Name"
date: "`r Sys.Date()`"
output:
  pdf_document:
    toc: true
    number_sections: true
  html_document:
    toc: true
    toc_float: true
bibliography: ../tex/paper/references.bib
---

## Introduction

This report presents the results of our analysis.

## Data

```{r load-data}
library(tidyverse)
data <- read_csv("../data/raw/sample_data.csv")
summary(data)
```

## Analysis

```{r regression}
model <- lm(outcome ~ treatment, data = data)
summary(model)
```

## Visualization

```{r plot, fig.cap="Treatment Effects"}
ggplot(data, aes(x = treatment, y = outcome)) +
  geom_boxplot() +
  theme_minimal()
```

## Conclusion

The results show...
```

Render:
```r
rmarkdown::render("reports/analysis_report.Rmd")
```

## Troubleshooting

### Radian Not Found

**Problem:** VS Code can't find radian

**Solution:**
```bash
# Find radian location
which radian  # Linux/macOS
where.exe radian  # Windows

# Update VS Code settings with full path
# Settings > R: Rterm > Edit in settings.json
```

### R Extension Not Working

**Problem:** IntelliSense, code completion not working

**Solution:**
```r
# Install/reinstall languageserver
install.packages("languageserver", dependencies = TRUE)

# Restart R session in VS Code
# Command Palette > R: Create R Terminal
```

### Plots Not Showing

**Problem:** Plots don't appear in VS Code

**Solution:**
```r
# Install httpgd
install.packages("httpgd")

# Enable in VS Code settings
"r.plot.useHttpgd": true

# Restart R session
```

### Permission Denied on Linux

**Problem:** Can't install packages, permission errors

**Solution:**
```bash
# Create user library directory
mkdir -p ~/R/library

# Set in .Rprofile
echo 'options(repos = c(CRAN = "https://cloud.r-project.org"))' >> ~/.Rprofile
echo '.libPaths("~/R/library")' >> ~/.Rprofile

# Or install with sudo (not recommended for user packages)
sudo R
# Then install packages
```

### Radian Crashes or Freezes

**Problem:** Radian becomes unresponsive

**Solution:**
```bash
# Update radian
pip install -U radian

# Check Python version (needs 3.8+)
python --version

# Reset radian config
rm ~/.radian_profile

# Use vanilla R temporarily
"r.rterm.linux": "/usr/bin/R"
```

### LaTeX Tables Look Wrong

**Problem:** Tables generated by stargazer/xtable have formatting issues

**Solution:**
```r
# For stargazer, disable header
stargazer(model,
          type = "latex",
          header = FALSE,  # Important
          float = TRUE,
          table.placement = "htbp")

# For xtable, use booktabs
print(xtable(df),
      booktabs = TRUE,  # Better formatting
      include.rownames = FALSE)

# Ensure LaTeX has booktabs package
# In your .tex file: \usepackage{booktabs}
```

### Encoding Issues with Data

**Problem:** Special characters not displaying correctly

**Solution:**
```r
# Specify encoding when reading
data <- read.csv("data.csv", fileEncoding = "UTF-8")

# Or using readr
library(readr)
data <- read_csv("data.csv", locale = locale(encoding = "UTF-8"))

# Check current encoding
Sys.getlocale()

# Set UTF-8
Sys.setlocale("LC_ALL", "en_US.UTF-8")
```

### Package Installation Fails

**Problem:** Package won't install, compilation errors

**Solution:**
```bash
# Linux: Install development tools
sudo apt install build-essential libcurl4-openssl-dev libssl-dev libxml2-dev

# macOS: Install Xcode Command Line Tools
xcode-select --install

# Windows: Install Rtools
# Download from: https://cran.r-project.org/bin/windows/Rtools/

# Then retry installation
install.packages("package_name")
```

### Git Integration Issues

**Problem:** Can't commit from R, git commands fail

**Solution:**
```r
# Set git editor
options(editor = "code")

# Or use usethis package
library(usethis)
use_git()
use_github()

# From terminal instead
system("git add .")
system("git commit -m 'Update analysis'")
```

## Additional Resources

### Documentation

- **Radian:** https://github.com/randy3k/radian
- **VS Code R Extension:** https://github.com/REditorSupport/vscode-R
- **R for Data Science:** https://r4ds.had.co.nz/
- **Advanced R:** https://adv-r.hadley.nz/

### Useful Packages

**Data Manipulation:**
- `dplyr` - Data transformation
- `tidyr` - Data tidying
- `data.table` - Fast data manipulation

**Visualization:**
- `ggplot2` - Grammar of graphics
- `plotly` - Interactive plots
- `patchwork` - Combine plots

**Statistical Analysis:**
- `lmtest` - Linear model diagnostics
- `sandwich` - Robust standard errors
- `plm` - Panel data models
- `fixest` - Fast fixed effects estimation

**Tables:**
- `stargazer` - Publication tables
- `modelsummary` - Modern regression tables
- `gt` - Customizable tables
- `kableExtra` - Enhanced knitr tables

**Reproducibility:**
- `renv` - Package version management
- `targets` - Pipeline management
- `here` - Project-relative paths

### Learning Resources

- **R Cheat Sheets:** https://www.rstudio.com/resources/cheatsheets/
- **Tidyverse:** https://www.tidyverse.org/
- **R Weekly:** https://rweekly.org/
- **Stack Overflow:** Tag [r] for questions

### Community

- **R4DS Learning Community:** https://www.rfordatasci.com/
- **RStudio Community:** https://community.rstudio.com/
- **r/rstats (Reddit):** https://www.reddit.com/r/rstats/

---

## Quick Reference

### VS Code Keyboard Shortcuts for R

| Action | Shortcut |
|--------|----------|
| Send line to R | `Ctrl+Enter` |
| Send selection to R | `Ctrl+Enter` |
| Source file | `Ctrl+Shift+S` |
| New R terminal | `Ctrl+Shift+` ` |
| Run all code | `Ctrl+Alt+R` |
| Insert pipe `%>%` | `Ctrl+Shift+M` |
| Insert assignment `<-` | `Alt+-` |

### Radian Keyboard Shortcuts

| Action | Shortcut |
|--------|----------|
| History search | `Ctrl+R` |
| Clear screen | `Ctrl+L` |
| Interrupt | `Ctrl+C` |
| Exit | `Ctrl+D` or `q()` |
| Autocomplete | `Tab` |
| Multiline edit | `Enter` (mid-expression) |

### Common R Commands

```r
# Session info
sessionInfo()
.libPaths()  # Library paths

# Package management
install.packages("pkg")
remove.packages("pkg")
update.packages()

# Help
?function_name
help("function_name")
??search_term

# Working directory
getwd()
setwd("path")

# List objects
ls()
rm(list = ls())  # Clear workspace

# Save/load workspace
save.image("workspace.RData")
load("workspace.RData")
```

---

**Last updated:** November 2025
