# Stata/MATLAB Integration

Working with Stata and MATLAB in the VS Code environment.

## Overview

While Stata and MATLAB don't have native VS Code integration like Python or R, you can still use them effectively within the VS Code workflow.

## Stata Integration

### Running Stata Code

#### Option 1: Integrated Terminal

```bash
# Windows
"C:\Program Files\Stata17\StataMP-64.exe" /e do scripts/analysis.do

# Mac
/Applications/Stata/StataMP.app/Contents/MacOS/StataMP -b do scripts/analysis.do

# Linux
stata-mp -b do scripts/analysis.do
```

#### Option 2: Stata Extension

Install the Stata Enhanced extension:
1. Open VS Code Extensions (Ctrl+Shift+X)
2. Search for "Stata Enhanced"
3. Install

Features:
- Syntax highlighting
- Code snippets
- Run selection in Stata (with setup)

### VS Code Setup for Stata

**Create keyboard shortcut:**

1. File → Preferences → Keyboard Shortcuts
2. Search for "Run Selection"
3. Add custom keybinding to run Stata command

**Example task in `tasks.json`:**

```json
{
    "label": "Run Stata Do File",
    "type": "shell",
    "command": "stata-mp",
    "args": [
        "-b",
        "do",
        "${file}"
    ],
    "group": "build",
    "presentation": {
        "reveal": "always",
        "panel": "new"
    }
}
```

### Makefile Integration

Add Stata to your Makefile:

```makefile
# Run Stata analysis
stata-analysis:
	stata-mp -b do scripts/stata_analysis.do
	
# Move Stata outputs to output directory
stata-outputs:
	mv *.log output/
	mv *.tex output/tables/
	
# Complete Stata workflow
stata: stata-analysis stata-outputs
```

### Exporting Stata Tables to LaTeX

In your Stata do-file:

```stata
* Load data
use data/processed/analysis_data.dta, clear

* Run regression
regress outcome treatment controls

* Export to LaTeX
esttab using "output/tables/stata_results.tex", ///
    replace ///
    label ///
    booktabs ///
    alignment(D{.}{.}{-1}) ///
    title("Regression Results") ///
    nomtitles
```

### Workflow Example

```bash
# Complete research pipeline with Stata
make clean
make data          # Python: process raw data
make stata         # Stata: run regressions
make figures       # Python: create plots
make paper         # LaTeX: compile paper
```

## MATLAB Integration

### Running MATLAB Code

#### Option 1: Integrated Terminal

```bash
# Windows
matlab -batch "run('scripts/analysis.m')"

# Mac/Linux
matlab -nodisplay -nosplash -nodesktop -r "run('scripts/analysis.m'); exit;"
```

#### Option 2: MATLAB Extension

Install MATLAB extension:
1. Open Extensions (Ctrl+Shift+X)
2. Search for "MATLAB"
3. Install official MathWorks extension

Features:
- Syntax highlighting
- Code navigation
- Linting
- Run selection (requires MATLAB Engine)

### VS Code Setup for MATLAB

**Create task for MATLAB:**

```json
{
    "label": "Run MATLAB Script",
    "type": "shell",
    "command": "matlab",
    "args": [
        "-batch",
        "run('${file}')"
    ],
    "group": "build",
    "problemMatcher": []
}
```

**Keyboard shortcut:**
- Bind F5 or Ctrl+Enter to run current file

### Makefile Integration

```makefile
# Run MATLAB analysis
matlab-analysis:
	matlab -batch "run('scripts/matlab_analysis.m')"
	
# Export MATLAB figures
matlab-figures:
	matlab -batch "addpath('scripts'); export_figures"
	
# Complete MATLAB workflow  
matlab: matlab-analysis matlab-figures
```

### Exporting MATLAB Figures

Create a MATLAB function to export figures:

```matlab
% scripts/export_figure.m
function export_figure(fig, filename)
    % Export figure as PDF and PNG
    
    % PDF for paper (vector graphics)
    exportgraphics(fig, ['output/figures/' filename '.pdf'], ...
        'ContentType', 'vector');
    
    % PNG for preview
    exportgraphics(fig, ['output/figures/' filename '.png'], ...
        'Resolution', 300);
end
```

Usage:

```matlab
% Create plot
fig = figure;
plot(x, y);
title('My Results');

% Export
export_figure(fig, 'matlab_plot');
```

### Exporting MATLAB Tables to LaTeX

```matlab
% Create table
T = table(variable1, variable2, ...
    'VariableNames', {'Var1', 'Var2'});

% Export to LaTeX
writetable(T, 'output/tables/matlab_table.tex', ...
    'FileType', 'text', ...
    'Delimiter', '&', ...
    'WriteRowNames', true);

% Or use custom function for booktabs formatting
matlab2latex(T, 'output/tables/formatted_table.tex');
```

## Mixed Workflow Example

Combining Python, Stata, and MATLAB:

```makefile
# Complete multi-language pipeline
all: clean data python-analysis stata-analysis matlab-analysis figures paper

data:
	python scripts/prepare_data.py
	
python-analysis:
	python scripts/python_analysis.py
	
stata-analysis:
	stata-mp -b do scripts/stata_regressions.do
	
matlab-analysis:
	matlab -batch "run('scripts/matlab_simulations.m')"
	
figures:
	python scripts/create_plots.py
	
tables: stata-analysis matlab-analysis
	# Tables created by individual programs
	
paper:
	cd tex/paper && pdflatex paper.tex && bibtex paper && pdflatex paper.tex && pdflatex paper.tex
	
clean:
	rm -rf output/*
```

## Common Issues and Solutions

### Issue: MATLAB not in PATH

**Solution:** Add MATLAB to your PATH or use full path in Makefile:

```makefile
# Windows
MATLAB = "C:\Program Files\MATLAB\R2023a\bin\matlab.exe"

# Mac
MATLAB = /Applications/MATLAB_R2023a.app/bin/matlab

# Use in commands
matlab-analysis:
	$(MATLAB) -batch "run('scripts/analysis.m')"
```

### Issue: Stata license server

**Solution:** Ensure Stata is properly licensed and network accessible.

### Issue: File paths in Stata/MATLAB

**Solution:** Use relative paths from project root:

```stata
* Stata
cd "`c(pwd)'"  // Project root
use "data/processed/data.dta"
```

```matlab
% MATLAB
cd(fileparts(mfilename('fullpath')));  % Script directory
cd('..');  % Project root
load('data/processed/data.mat');
```

## Best Practices

### ✅ DO
- Use integrated terminal for execution
- Export outputs to standardized directories
- Include all steps in Makefile
- Use batch/headless mode for automation
- Document software versions in README

### ❌ DON'T
- Run GUIs during automated workflows
- Hardcode absolute paths
- Manually copy-paste results
- Forget to export intermediate outputs
- Mix manual and automated steps

## Alternative: R Integration

If you also use R, it has better VS Code integration:

```bash
# Install R extension
code --install-extension REditorSupport.r

# Run R scripts
Rscript scripts/analysis.R
```

Add to Makefile:
```makefile
r-analysis:
	Rscript scripts/r_analysis.R
```

## Next Steps

- Review [Makefile Automation](Makefile-Automation)
- Learn about [Tables and Figures](Tables-and-Figures)
- Explore [Overleaf Integration](Overleaf-Integration)
- Check [Troubleshooting](Troubleshooting) for common issues
