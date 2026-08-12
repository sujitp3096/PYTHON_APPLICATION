"""
CSV Data Analyzer - Python console application

Loads a CSV file and lets you explore it interactively:
 - Summary statistics (mean, median, std, min, max) for numeric columns
 - Missing value report
 - Value counts for a chosen column
 - Filter rows by a condition
 - Export a quick bar/line chart for a numeric column

Requires: pandas, matplotlib
Install with: pip install pandas matplotlib
"""

import os
import sys

try:
    import pandas as pd
except ImportError:
    print("This tool requires pandas. Install it with: pip install pandas")
    sys.exit(1)


def load_csv():
    path = input("Enter path to CSV file: ").strip()
    if not os.path.exists(path):
        print(f"File not found: {path}")
        return None

    try:
        df = pd.read_csv(path)
        print(f"\nLoaded '{path}' — {df.shape[0]} rows, {df.shape[1]} columns.")
        print("Columns:", list(df.columns))
        return df
    except Exception as e:
        print(f"Error reading CSV: {e}")
        return None


def show_summary(df):
    numeric_df = df.select_dtypes(include="number")
    if numeric_df.empty:
        print("No numeric columns found in this dataset.")
        return

    print("\nSummary statistics (numeric columns):")
    print(numeric_df.describe().round(2).to_string())


def show_missing_values(df):
    missing = df.isnull().sum()
    missing = missing[missing > 0]

    if missing.empty:
        print("\nNo missing values found. Dataset is complete.")
        return

    print("\nMissing values per column:")
    for col, count in missing.items():
        pct = (count / len(df)) * 100
        print(f"  {col}: {count} missing ({pct:.1f}%)")


def show_value_counts(df):
    print("\nColumns:", list(df.columns))
    col = input("Enter column name to see value counts: ").strip()

    if col not in df.columns:
        print(f"Column '{col}' not found.")
        return

    counts = df[col].value_counts().head(20)
    print(f"\nTop values in '{col}':")
    print(counts.to_string())


def filter_rows(df):
    print("\nColumns:", list(df.columns))
    col = input("Enter column name to filter on: ").strip()

    if col not in df.columns:
        print(f"Column '{col}' not found.")
        return

    print("Available operators: == != > >= < <= contains")
    op = input("Enter operator: ").strip()
    value = input("Enter value to compare against: ").strip()

    try:
        if op == "contains":
            result = df[df[col].astype(str).str.contains(value, case=False, na=False)]
        else:
            # Try to interpret value as a number if the column is numeric
            if pd.api.types.is_numeric_dtype(df[col]):
                value_cast = float(value)
            else:
                value_cast = value

            if op == "==":
                result = df[df[col] == value_cast]
            elif op == "!=":
                result = df[df[col] != value_cast]
            elif op == ">":
                result = df[df[col] > value_cast]
            elif op == ">=":
                result = df[df[col] >= value_cast]
            elif op == "<":
                result = df[df[col] < value_cast]
            elif op == "<=":
                result = df[df[col] <= value_cast]
            else:
                print("Unknown operator.")
                return

        print(f"\n{len(result)} matching row(s):")
        print(result.head(20).to_string(index=False))
        if len(result) > 20:
            print(f"... and {len(result) - 20} more row(s) not shown.")

    except Exception as e:
        print(f"Error applying filter: {e}")


def export_chart(df):
    try:
        import matplotlib
        matplotlib.use("Agg")  # no GUI needed, saves straight to file
        import matplotlib.pyplot as plt
    except ImportError:
        print("This feature requires matplotlib. Install it with: pip install matplotlib")
        return

    numeric_cols = list(df.select_dtypes(include="number").columns)
    if not numeric_cols:
        print("No numeric columns available to chart.")
        return

    print("\nNumeric columns:", numeric_cols)
    col = input("Enter numeric column to chart: ").strip()

    if col not in numeric_cols:
        print(f"'{col}' is not a valid numeric column.")
        return

    chart_type = input("Chart type - histogram or line? [histogram]: ").strip().lower() or "histogram"
    output_path = input("Output image filename [chart.png]: ").strip() or "chart.png"

    plt.figure(figsize=(8, 5))
    if chart_type == "line":
        df[col].plot(kind="line", title=f"{col} over row index")
    else:
        df[col].plot(kind="hist", bins=20, title=f"Distribution of {col}")

    plt.xlabel(col)
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()

    print(f"Chart saved to: {output_path}")


def print_menu():
    print("\n--------------------------------")
    print("1. Show summary statistics")
    print("2. Show missing value report")
    print("3. Show value counts for a column")
    print("4. Filter rows")
    print("5. Export a chart (histogram/line)")
    print("6. Load a different CSV file")
    print("7. Exit")
    print("--------------------------------")


def main():
    print("===== CSV Data Analyzer =====\n")
    df = load_csv()

    while df is None:
        retry = input("Try another file? (y/n): ").strip().lower()
        if retry != "y":
            print("Goodbye!")
            return
        df = load_csv()

    while True:
        print_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            show_summary(df)
        elif choice == "2":
            show_missing_values(df)
        elif choice == "3":
            show_value_counts(df)
        elif choice == "4":
            filter_rows(df)
        elif choice == "5":
            export_chart(df)
        elif choice == "6":
            new_df = load_csv()
            if new_df is not None:
                df = new_df
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
