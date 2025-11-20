#!/usr/bin/env python3
"""
Script to read and process fake/sample data

This script demonstrates:
- Reading CSV data from data/raw/
- Generating fake data for testing
- Basic data processing and validation
- Saving processed data to data/processed/

Author: Tomas Larroucau (ASU Workshop)
Created: November 2025
"""

import os
import sys
from pathlib import Path
from typing import Dict, List

import numpy as np
import pandas as pd


def read_sample_data(filepath: str = "data/raw/sample_data.csv") -> pd.DataFrame:
    """
    Read sample data from CSV file.
    
    Parameters
    ----------
    filepath : str
        Path to the CSV file
        
    Returns
    -------
    pd.DataFrame
        Loaded data
        
    Raises
    ------
    FileNotFoundError
        If the file doesn't exist
    """
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Data file not found: {filepath}")
    
    print(f"Reading data from {filepath}...")
    df = pd.read_csv(filepath)
    print(f"Loaded {len(df)} rows and {len(df.columns)} columns")
    
    return df


def generate_fake_data(n_rows: int = 1000, seed: int = 42) -> pd.DataFrame:
    """
    Generate fake dataset for testing and demonstration.
    
    Parameters
    ----------
    n_rows : int
        Number of rows to generate
    seed : int
        Random seed for reproducibility
        
    Returns
    -------
    pd.DataFrame
        Fake dataset with multiple variables
    """
    np.random.seed(seed)
    
    print(f"Generating fake dataset with {n_rows} observations...")
    
    # Generate fake data
    data = {
        'id': range(1, n_rows + 1),
        'treatment': np.random.binomial(1, 0.5, n_rows),
        'age': np.random.normal(35, 10, n_rows).clip(18, 80).astype(int),
        'income': np.random.lognormal(10.5, 0.5, n_rows),
        'education': np.random.choice(['High School', 'Bachelor', 'Master', 'PhD'], 
                                     n_rows, 
                                     p=[0.3, 0.4, 0.2, 0.1]),
        'satisfaction': np.random.randint(1, 11, n_rows),
    }
    
    # Create outcome variable with treatment effect
    treatment_effect = 5.0
    data['outcome'] = (
        50 + 
        data['treatment'] * treatment_effect + 
        (data['age'] - 35) * 0.2 + 
        np.random.normal(0, 10, n_rows)
    )
    
    df = pd.DataFrame(data)
    
    print(f"Generated {len(df)} rows with {len(df.columns)} columns")
    print(f"Columns: {', '.join(df.columns)}")
    
    return df


def display_summary_statistics(df: pd.DataFrame) -> None:
    """
    Display summary statistics for the dataset.
    
    Parameters
    ----------
    df : pd.DataFrame
        Dataset to summarize
    """
    print("\n" + "=" * 60)
    print("SUMMARY STATISTICS")
    print("=" * 60)
    
    print(f"\nDataset shape: {df.shape[0]} rows × {df.shape[1]} columns")
    
    print("\nColumn types:")
    print(df.dtypes)
    
    print("\nNumerical variables:")
    print(df.describe().round(2))
    
    # Check for missing values
    missing = df.isnull().sum()
    if missing.any():
        print("\nMissing values:")
        print(missing[missing > 0])
    else:
        print("\nNo missing values detected")
    
    # Treatment balance (if applicable)
    if 'treatment' in df.columns:
        print("\nTreatment distribution:")
        print(df['treatment'].value_counts())
        
        if 'outcome' in df.columns:
            print("\nMean outcome by treatment:")
            print(df.groupby('treatment')['outcome'].mean().round(2))
    
    print("=" * 60 + "\n")


def validate_data(df: pd.DataFrame) -> bool:
    """
    Validate dataset for common issues.
    
    Parameters
    ----------
    df : pd.DataFrame
        Dataset to validate
        
    Returns
    -------
    bool
        True if validation passes, False otherwise
    """
    print("Validating data...")
    
    issues = []
    
    # Check for empty dataframe
    if df.empty:
        issues.append("Dataset is empty")
    
    # Check for duplicated rows
    duplicates = df.duplicated().sum()
    if duplicates > 0:
        issues.append(f"Found {duplicates} duplicated rows")
    
    # Check for suspicious values
    for col in df.select_dtypes(include=[np.number]).columns:
        if df[col].isnull().any():
            issues.append(f"Column '{col}' has missing values")
        
        # Check for infinite values
        if np.isinf(df[col]).any():
            issues.append(f"Column '{col}' has infinite values")
    
    if issues:
        print("⚠️  Validation warnings:")
        for issue in issues:
            print(f"  - {issue}")
        return False
    else:
        print("✅ Data validation passed")
        return True


def save_processed_data(df: pd.DataFrame, filename: str = "processed_data.csv") -> None:
    """
    Save processed data to data/processed/ directory.
    
    Parameters
    ----------
    df : pd.DataFrame
        Data to save
    filename : str
        Name of the output file
    """
    output_dir = Path("data/processed")
    output_dir.mkdir(parents=True, exist_ok=True)
    
    output_path = output_dir / filename
    
    print(f"Saving processed data to {output_path}...")
    df.to_csv(output_path, index=False)
    print(f"✅ Saved {len(df)} rows to {output_path}")


def main():
    """Main execution function."""
    print("\n" + "=" * 60)
    print("DATA READING AND PROCESSING SCRIPT")
    print("=" * 60 + "\n")
    
    # Try to read existing sample data first
    try:
        df = read_sample_data("data/raw/sample_data.csv")
        print("Using existing sample data")
    except FileNotFoundError:
        print("Sample data not found, generating fake data instead")
        df = generate_fake_data(n_rows=1000)
        
        # Optionally save the generated data
        save_dir = Path("data/raw")
        save_dir.mkdir(parents=True, exist_ok=True)
        df.to_csv("data/raw/generated_fake_data.csv", index=False)
        print("Saved generated data to data/raw/generated_fake_data.csv")
    
    # Display summary statistics
    display_summary_statistics(df)
    
    # Validate data
    validate_data(df)
    
    # Process data (example: create some derived variables)
    print("\nProcessing data...")
    df_processed = df.copy()
    
    if 'age' in df.columns:
        df_processed['age_group'] = pd.cut(
            df['age'], 
            bins=[0, 25, 35, 50, 100],
            labels=['Young', 'Adult', 'Middle-aged', 'Senior']
        )
    
    if 'income' in df.columns:
        df_processed['log_income'] = np.log(df['income'])
        df_processed['income_quartile'] = pd.qcut(
            df['income'], 
            q=4, 
            labels=['Q1', 'Q2', 'Q3', 'Q4']
        )
    
    print(f"Added {len(df_processed.columns) - len(df.columns)} new variables")
    print(f"New columns: {', '.join([col for col in df_processed.columns if col not in df.columns])}")
    
    # Save processed data
    save_processed_data(df_processed, "processed_data.csv")
    
    print("\n✅ Script completed successfully!\n")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"\n❌ Error: {e}", file=sys.stderr)
        sys.exit(1)
