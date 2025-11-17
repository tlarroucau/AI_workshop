"""
Main Analysis Script

This script performs the complete analysis pipeline:
1. Load and clean data
2. Generate summary statistics
3. Create visualizations
4. Run regression analysis
5. Export results for LaTeX documents
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import statsmodels.api as sm
import statsmodels.formula.api as smf
import os

# Import utility functions
from utils import (
    load_data, 
    summary_statistics, 
    balance_table,
    format_regression_table,
    set_plot_style,
    save_plot
)


def main():
    """Execute the complete analysis pipeline."""
    
    print("=" * 60)
    print("RESEARCH ANALYSIS PIPELINE")
    print("=" * 60)
    
    # Create output directories if they don't exist
    os.makedirs('../output/figures', exist_ok=True)
    os.makedirs('../output/tables', exist_ok=True)
    
    # Step 1: Load data
    print("\n[1/5] Loading data...")
    df = load_data('../data/raw/sample_data.csv')
    
    # Step 2: Summary statistics
    print("\n[2/5] Generating summary statistics...")
    variables = ['age', 'income', 'education_years', 'outcome']
    summary = summary_statistics(df, variables)
    print("\nSummary Statistics:")
    print(summary)
    
    # Save summary statistics as LaTeX table
    latex_summary = summary.to_latex(
        caption='Summary Statistics',
        label='tab:summary',
        escape=False
    )
    
    with open('../output/tables/summary_statistics.tex', 'w') as f:
        f.write("\\begin{table}[htbp]\n")
        f.write("\\centering\n")
        f.write("\\caption{Summary Statistics}\n")
        f.write("\\label{tab:summary}\n")
        f.write(summary.to_latex(escape=False, column_format='lrrrrr'))
        f.write("\\begin{tablenotes}\n")
        f.write("\\small\n")
        f.write("\\item Notes: Sample includes 500 observations.\n")
        f.write("\\end{tablenotes}\n")
        f.write("\\end{table}\n")
    
    print("Saved summary statistics table")
    
    # Step 3: Balance table
    print("\n[3/5] Creating balance table...")
    balance = balance_table(df, 'treatment', ['age', 'income', 'education_years'])
    print("\nBalance Table:")
    print(balance)
    
    # Save balance table
    with open('../output/tables/balance_table.tex', 'w') as f:
        f.write("\\begin{table}[htbp]\n")
        f.write("\\centering\n")
        f.write("\\caption{Balance Table: Treatment vs Control}\n")
        f.write("\\label{tab:balance}\n")
        f.write(balance.to_latex(escape=False))
        f.write("\\begin{tablenotes}\n")
        f.write("\\small\n")
        f.write("\\item Notes: Standard errors in parentheses.\n")
        f.write("\\end{tablenotes}\n")
        f.write("\\end{table}\n")
    
    print("Saved balance table")
    
    # Step 4: Visualizations
    print("\n[4/5] Creating visualizations...")
    set_plot_style()
    
    # Figure 1: Distribution of outcome by treatment
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=df, x='treatment', y='outcome', palette='Set2')
    plt.xlabel('Treatment Group')
    plt.ylabel('Outcome')
    plt.title('Distribution of Outcome by Treatment Status')
    plt.xticks([0, 1], ['Control', 'Treatment'])
    save_plot('outcome_by_treatment')
    plt.close()
    
    # Figure 2: Scatter plot with regression line
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=df, x='income', y='outcome', hue='treatment', 
                    palette='Set1', alpha=0.6)
    
    # Add regression lines
    for treatment in [0, 1]:
        subset = df[df['treatment'] == treatment]
        z = np.polyfit(subset['income'], subset['outcome'], 1)
        p = np.poly1d(z)
        x_line = np.linspace(subset['income'].min(), subset['income'].max(), 100)
        plt.plot(x_line, p(x_line), linestyle='--', linewidth=2)
    
    plt.xlabel('Income ($)')
    plt.ylabel('Outcome')
    plt.title('Outcome vs Income by Treatment Status')
    plt.legend(title='Treatment', labels=['Control', 'Treatment'])
    save_plot('scatter_income_outcome')
    plt.close()
    
    # Figure 3: Distribution of key variables
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    
    df['age'].hist(bins=30, ax=axes[0, 0], edgecolor='black', alpha=0.7)
    axes[0, 0].set_title('Age Distribution')
    axes[0, 0].set_xlabel('Age')
    axes[0, 0].set_ylabel('Frequency')
    
    df['income'].hist(bins=30, ax=axes[0, 1], edgecolor='black', alpha=0.7, color='green')
    axes[0, 1].set_title('Income Distribution')
    axes[0, 1].set_xlabel('Income ($)')
    axes[0, 1].set_ylabel('Frequency')
    
    df['education_years'].value_counts().sort_index().plot(kind='bar', ax=axes[1, 0], 
                                                            edgecolor='black', alpha=0.7, color='orange')
    axes[1, 0].set_title('Education Distribution')
    axes[1, 0].set_xlabel('Years of Education')
    axes[1, 0].set_ylabel('Frequency')
    axes[1, 0].tick_params(axis='x', rotation=0)
    
    df['outcome'].hist(bins=30, ax=axes[1, 1], edgecolor='black', alpha=0.7, color='red')
    axes[1, 1].set_title('Outcome Distribution')
    axes[1, 1].set_xlabel('Outcome')
    axes[1, 1].set_ylabel('Frequency')
    
    plt.tight_layout()
    save_plot('distributions')
    plt.close()
    
    print("Saved all figures")
    
    # Step 5: Regression analysis
    print("\n[5/5] Running regression analysis...")
    
    # Model 1: Simple treatment effect
    model1 = smf.ols('outcome ~ treatment', data=df).fit()
    print("\nModel 1: Simple Treatment Effect")
    print(model1.summary())
    
    # Model 2: With controls
    model2 = smf.ols('outcome ~ treatment + age + income + education_years', data=df).fit()
    print("\nModel 2: Treatment Effect with Controls")
    print(model2.summary())
    
    # Create regression table
    results_df = pd.DataFrame({
        'Variable': ['Treatment', 'Age', 'Income', 'Education Years', 'Constant'],
        'Model 1': [
            f"{model1.params['treatment']:.3f}***" if model1.pvalues['treatment'] < 0.01 else f"{model1.params['treatment']:.3f}",
            '-', '-', '-',
            f"{model1.params['Intercept']:.3f}"
        ],
        'Model 1 SE': [
            f"({model1.bse['treatment']:.3f})",
            '-', '-', '-',
            f"({model1.bse['Intercept']:.3f})"
        ],
        'Model 2': [
            f"{model2.params['treatment']:.3f}***" if model2.pvalues['treatment'] < 0.01 else f"{model2.params['treatment']:.3f}",
            f"{model2.params['age']:.3f}",
            f"{model2.params['income']:.6f}",
            f"{model2.params['education_years']:.3f}",
            f"{model2.params['Intercept']:.3f}"
        ],
        'Model 2 SE': [
            f"({model2.bse['treatment']:.3f})",
            f"({model2.bse['age']:.3f})",
            f"({model2.bse['income']:.6f})",
            f"({model2.bse['education_years']:.3f})",
            f"({model2.bse['Intercept']:.3f})"
        ]
    })
    
    # Save regression table
    with open('../output/tables/regression_results.tex', 'w') as f:
        f.write("\\begin{table}[htbp]\n")
        f.write("\\centering\n")
        f.write("\\caption{Regression Results: Treatment Effects}\n")
        f.write("\\label{tab:regression}\n")
        f.write("\\begin{tabular}{lcccc}\n")
        f.write("\\toprule\n")
        f.write("Variable & Model 1 & (SE) & Model 2 & (SE) \\\\\n")
        f.write("\\midrule\n")
        
        for _, row in results_df.iterrows():
            f.write(f"{row['Variable']} & {row['Model 1']} & {row['Model 1 SE']} & {row['Model 2']} & {row['Model 2 SE']} \\\\\n")
        
        f.write("\\midrule\n")
        f.write(f"N & \\multicolumn{{2}}{{c}}{{{int(model1.nobs)}}} & \\multicolumn{{2}}{{c}}{{{int(model2.nobs)}}} \\\\\n")
        f.write(f"R-squared & \\multicolumn{{2}}{{c}}{{{model1.rsquared:.4f}}} & \\multicolumn{{2}}{{c}}{{{model2.rsquared:.4f}}} \\\\\n")
        f.write("\\bottomrule\n")
        f.write("\\end{tabular}\n")
        f.write("\\begin{tablenotes}\n")
        f.write("\\small\n")
        f.write("\\item Notes: Standard errors in parentheses. Significance: *** p<0.01, ** p<0.05, * p<0.1\n")
        f.write("\\end{tablenotes}\n")
        f.write("\\end{table}\n")
    
    print("Saved regression results table")
    
    print("\n" + "=" * 60)
    print("ANALYSIS COMPLETE!")
    print("=" * 60)
    print("\nOutputs saved to:")
    print("  - Figures: output/figures/")
    print("  - Tables: output/tables/")
    print("\nRun 'make paper' or 'make slides' to compile LaTeX documents")


if __name__ == "__main__":
    main()
