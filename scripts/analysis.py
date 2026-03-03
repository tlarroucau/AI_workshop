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
    
    # Rename index for LaTeX (escape underscores)
    summary_latex = summary.copy()
    summary_latex.index = summary_latex.index.str.replace('_', '\\_')
    
    # Save summary statistics as LaTeX table
    with open('../output/tables/summary_statistics.tex', 'w') as f:
        f.write("\\begin{table}[htbp]\n")
        f.write("\\centering\n")
        f.write("\\caption{Summary Statistics}\n")
        f.write("\\label{tab:summary}\n")
        f.write(summary_latex.to_latex(escape=False, column_format='lrrrrr'))
        f.write("\\begin{tablenotes}\n")
        f.write("\\small\n")
        f.write("\\item Notes: Sample includes 50 observations.\n")
        f.write("\\end{tablenotes}\n")
        f.write("\\end{table}\n")
    
    print("Saved summary statistics table")
    
    # Step 3: Balance table
    print("\n[3/5] Creating balance table...")
    balance = balance_table(df, 'treatment', ['age', 'income', 'education_years'])
    print("\nBalance Table:")
    print(balance)
    
    # Rename index for LaTeX (escape underscores)
    balance_latex = balance.copy()
    balance_latex.index = balance_latex.index.str.replace('_', '\\_')
    
    # Save balance table
    with open('../output/tables/balance_table.tex', 'w') as f:
        f.write("\\begin{table}[htbp]\n")
        f.write("\\centering\n")
        f.write("\\caption{Balance Table: Treatment vs Control}\n")
        f.write("\\label{tab:balance}\n")
        f.write(balance_latex.to_latex(escape=False))
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
    sns.boxplot(data=df, x='treatment', y='outcome',
                palette=['#8C1D40', '#FFC627'])  # ASU Maroon / ASU Gold
    plt.xlabel('Treatment Group')
    plt.ylabel('Outcome')
    plt.title('Distribution of Outcome by Treatment Status')
    plt.xticks([0, 1], ['Control', 'Treatment'])
    save_plot('outcome_by_treatment')
    plt.close()
    
    # Figure 2: Scatter plot with regression line
    plt.figure(figsize=(10, 6))
    
    # ASU brand colors: Maroon for Control, Gold for Treatment
    colors = {0: '#8C1D40', 1: '#FFC627'}  # ASU Maroon / ASU Gold
    
    sns.scatterplot(data=df, x='income', y='outcome', hue='treatment', 
                    palette=colors, alpha=0.6)
    
    # Add regression lines
    for treatment in [0, 1]:
        subset = df[df['treatment'] == treatment]
        z = np.polyfit(subset['income'], subset['outcome'], 1)
        p = np.poly1d(z)
        x_line = np.linspace(subset['income'].min(), subset['income'].max(), 100)
        plt.plot(x_line, p(x_line), linestyle='--', linewidth=2, color=colors[treatment])
    
    plt.xlabel('Income ($)')
    plt.ylabel('Outcome')
    plt.title('Outcome vs Income by Treatment Status')
    plt.legend(title='Treatment', labels=['Control', 'Treatment'])
    save_plot('scatter_income_outcome')
    plt.close()
    
    # Figure 3: Distribution of key variables
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    
    df['age'].hist(bins=30, ax=axes[0, 0], edgecolor='black', alpha=0.7,
                   color='#8C1D40')  # ASU Maroon
    axes[0, 0].set_title('Age Distribution')
    axes[0, 0].set_xlabel('Age')
    axes[0, 0].set_ylabel('Frequency')
    
    df['income'].hist(bins=30, ax=axes[0, 1], edgecolor='black', alpha=0.7,
                      color='#FFC627')  # ASU Gold
    axes[0, 1].set_title('Income Distribution')
    axes[0, 1].set_xlabel('Income ($)')
    axes[0, 1].set_ylabel('Frequency')
    
    df['education_years'].value_counts().sort_index().plot(kind='bar', ax=axes[1, 0], 
                                                            edgecolor='black', alpha=0.7,
                                                            color='#8C1D40')  # ASU Maroon
    axes[1, 0].set_title('Education Distribution')
    axes[1, 0].set_xlabel('Years of Education')
    axes[1, 0].set_ylabel('Frequency')
    axes[1, 0].tick_params(axis='x', rotation=0)
    
    df['outcome'].hist(bins=30, ax=axes[1, 1], edgecolor='black', alpha=0.7,
                       color='#FFC627')  # ASU Gold
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
    
    # ---- Robustness: Cluster-robust standard errors by region ----
    print("\nRunning cluster-robust SE estimation (clustering by region)...")
    
    # Re-estimate models with cluster-robust SEs
    model1_cluster = smf.ols('outcome ~ treatment', data=df).fit(
        cov_type='cluster', cov_kwds={'groups': df['region_id']}
    )
    model2_cluster = smf.ols('outcome ~ treatment + age + income + education_years', data=df).fit(
        cov_type='cluster', cov_kwds={'groups': df['region_id']}
    )
    
    print("Model 1 (Clustered):")
    print(model1_cluster.summary())
    print("\nModel 2 (Clustered):")
    print(model2_cluster.summary())
    
    # Helper to format coefficient with significance stars
    def _fmt_coef(model, var):
        p = model.pvalues[var]
        stars = '***' if p < 0.01 else ('**' if p < 0.05 else ('*' if p < 0.1 else ''))
        return f"{model.params[var]:.3f}{stars}"
    
    def _fmt_se(model, var):
        return f"({model.bse[var]:.3f})"
    
    # Build robustness table: Treatment coefficient row only, 4 columns
    robustness_vars = ['treatment', 'age', 'income', 'education_years', 'Intercept']
    display_names = ['Treatment', 'Age', 'Income', 'Education Years', 'Constant']
    
    with open('../output/tables/regression_robustness.tex', 'w') as f:
        f.write("\\begin{table}[htbp]\n")
        f.write("\\centering\n")
        f.write("\\caption{Robustness Check: Cluster-Robust Standard Errors}\n")
        f.write("\\label{tab:robustness}\n")
        f.write("\\begin{tabular}{lcccc}\n")
        f.write("\\toprule\n")
        f.write(" & \\multicolumn{2}{c}{Model 1} & \\multicolumn{2}{c}{Model 2} \\\\\n")
        f.write("\\cmidrule(lr){2-3} \\cmidrule(lr){4-5}\n")
        f.write(" & Default & Clustered & Default & Clustered \\\\\n")
        f.write("\\midrule\n")
        
        for var, name in zip(robustness_vars, display_names):
            if var in model1.params.index:
                m1_def = _fmt_coef(model1, var)
                m1_se = _fmt_se(model1, var)
                m1_cl = _fmt_coef(model1_cluster, var)
                m1_cl_se = _fmt_se(model1_cluster, var)
            else:
                m1_def = '-'
                m1_se = ''
                m1_cl = '-'
                m1_cl_se = ''
            
            m2_def = _fmt_coef(model2, var)
            m2_se = _fmt_se(model2, var)
            m2_cl = _fmt_coef(model2_cluster, var)
            m2_cl_se = _fmt_se(model2_cluster, var)
            
            f.write(f"{name} & {m1_def} & {m1_cl} & {m2_def} & {m2_cl} \\\\\n")
            f.write(f" & {m1_se} & {m1_cl_se} & {m2_se} & {m2_cl_se} \\\\\n")
        
        f.write("\\midrule\n")
        f.write(f"N & \\multicolumn{{2}}{{c}}{{{int(model1.nobs)}}} & \\multicolumn{{2}}{{c}}{{{int(model2.nobs)}}} \\\\\n")
        f.write(f"R-squared & \\multicolumn{{2}}{{c}}{{{model1.rsquared:.4f}}} & \\multicolumn{{2}}{{c}}{{{model2.rsquared:.4f}}} \\\\\n")
        f.write("Clustering & No & Region & No & Region \\\\\n")
        f.write("\\bottomrule\n")
        f.write("\\end{tabular}\n")
        f.write("\\begin{tablenotes}\n")
        f.write("\\small\n")
        f.write("\\item Notes: Standard errors in parentheses. Cluster-robust SEs clustered at the region level.\n")
        f.write("\\item Significance: *** p<0.01, ** p<0.05, * p<0.1\n")
        f.write("\\end{tablenotes}\n")
        f.write("\\end{table}\n")
    
    print("Saved robustness table (cluster-robust SEs)")
    
    print("\n" + "=" * 60)
    print("ANALYSIS COMPLETE!")
    print("=" * 60)
    print("\nOutputs saved to:")
    print("  - Figures: output/figures/")
    print("  - Tables: output/tables/")
    print("\nRun 'make paper' or 'make slides' to compile LaTeX documents")


if __name__ == "__main__":
    main()
