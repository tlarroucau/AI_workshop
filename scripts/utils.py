"""
Utility Functions for Data Analysis

This module provides helper functions used across the analysis pipeline.
"""

from typing import Dict, List, Tuple
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def load_data(filepath: str) -> pd.DataFrame:
    """
    Load CSV data with error handling.
    
    Parameters
    ----------
    filepath : str
        Path to CSV file
        
    Returns
    -------
    pd.DataFrame
        Loaded data
    """
    try:
        df = pd.read_csv(filepath)
        print(f"Successfully loaded {len(df)} rows from {filepath}")
        return df
    except FileNotFoundError:
        raise FileNotFoundError(f"Data file not found: {filepath}")
    except Exception as e:
        raise Exception(f"Error loading data: {str(e)}")


def summary_statistics(df: pd.DataFrame, columns: List[str] = None) -> pd.DataFrame:
    """
    Compute summary statistics for specified columns.
    
    Parameters
    ----------
    df : pd.DataFrame
        Input dataset
    columns : List[str], optional
        Columns to summarize. If None, uses all numeric columns.
        
    Returns
    -------
    pd.DataFrame
        Summary statistics table
    """
    if columns is None:
        columns = df.select_dtypes(include=[np.number]).columns.tolist()
    
    stats = df[columns].describe().T
    stats['median'] = df[columns].median()
    stats = stats[['mean', 'median', 'std', 'min', 'max']]
    stats.columns = ['Mean', 'Median', 'Std Dev', 'Min', 'Max']
    
    return stats.round(2)


def balance_table(df: pd.DataFrame, treatment_col: str, 
                  variables: List[str]) -> pd.DataFrame:
    """
    Create a balance table comparing treatment and control groups.
    
    Parameters
    ----------
    df : pd.DataFrame
        Input dataset
    treatment_col : str
        Name of treatment indicator column
    variables : List[str]
        List of variables to compare
        
    Returns
    -------
    pd.DataFrame
        Balance table with means for each group and difference
    """
    balance = pd.DataFrame(index=variables, 
                          columns=['Control Mean', 'Treatment Mean', 'Difference', 'Std. Error'])
    
    for var in variables:
        control_mean = df[df[treatment_col] == 0][var].mean()
        treatment_mean = df[df[treatment_col] == 1][var].mean()
        difference = treatment_mean - control_mean
        
        # Calculate standard error of difference
        control_std = df[df[treatment_col] == 0][var].std()
        treatment_std = df[df[treatment_col] == 1][var].std()
        n_control = (df[treatment_col] == 0).sum()
        n_treatment = (df[treatment_col] == 1).sum()
        
        se = np.sqrt((control_std**2 / n_control) + (treatment_std**2 / n_treatment))
        
        balance.loc[var] = [control_mean, treatment_mean, difference, se]
    
    return balance.round(3)


def format_regression_table(results, output_path: str, 
                           caption: str, label: str) -> None:
    """
    Format and save regression results as LaTeX table.
    
    Parameters
    ----------
    results : statsmodels regression results object
        Fitted model results
    output_path : str
        Path to save the .tex file
    caption : str
        Table caption
    label : str
        LaTeX label for cross-referencing
    """
    # Extract coefficients and statistics
    summary = results.summary2().tables[1]
    summary = summary.round(4)
    
    # Rename columns for clarity
    summary.columns = ['Coefficient', 'Std. Error', 't-statistic', 'p-value']
    
    # Add significance stars
    def add_stars(row):
        if row['p-value'] < 0.01:
            return f"{row['Coefficient']:.4f}***"
        elif row['p-value'] < 0.05:
            return f"{row['Coefficient']:.4f}**"
        elif row['p-value'] < 0.1:
            return f"{row['Coefficient']:.4f}*"
        else:
            return f"{row['Coefficient']:.4f}"
    
    summary['Coefficient'] = summary.apply(add_stars, axis=1)
    summary['Std. Error'] = summary['Std. Error'].apply(lambda x: f"({x:.4f})")
    
    # Keep only coefficient and std error for table
    table_df = summary[['Coefficient', 'Std. Error']]
    
    # Generate LaTeX
    latex_table = table_df.to_latex(escape=False)
    
    # Wrap in table environment
    full_latex = f"""\\begin{{table}}[htbp]
\\centering
\\caption{{{caption}}}
\\label{{{label}}}
{latex_table}
\\begin{{tablenotes}}
\\small
\\item Notes: Significance levels: *** p<0.01, ** p<0.05, * p<0.1
\\item N = {int(results.nobs)}, R-squared = {results.rsquared:.4f}
\\end{{tablenotes}}
\\end{{table}}"""
    
    with open(output_path, 'w') as f:
        f.write(full_latex)
    
    print(f"Saved regression table to {output_path}")


def set_plot_style():
    """Configure matplotlib style for consistent plots."""
    sns.set_style("whitegrid")
    sns.set_context("paper", font_scale=1.5)
    sns.set_palette("colorblind")
    plt.rcParams['figure.figsize'] = (10, 6)
    plt.rcParams['savefig.dpi'] = 300
    plt.rcParams['savefig.bbox'] = 'tight'


def save_plot(filename: str, formats: List[str] = ['pdf', 'png']):
    """
    Save current plot in multiple formats.
    
    Parameters
    ----------
    filename : str
        Base filename (without extension)
    formats : List[str]
        List of formats to save ('pdf', 'png', etc.)
    """
    for fmt in formats:
        output_path = f'../output/figures/{filename}.{fmt}'
        plt.savefig(output_path, bbox_inches='tight')
        print(f"Saved figure to {output_path}")
