# HW1: Python Data Analysis Basics

## Process
I upgraded Python in my `cse583` Conda environment from 3.12 to 3.13 because the assignment requires Python 3.13 or later. I used VS Code to create the required folders and files. I downloaded the dataset and renamed it `bicycle_data.csv`.
I loaded the CSV with pandas, checked the column types, and converted dates to datetime and counts to nullable integers. I added total count, hour, and year columns, then selected the 2016 data. I removed one record with missing data, plotted the total counts grouped by hour, and saved the figure as `counts_by_hour.png`. I calculated hourly averages and found that 17:00 was the busiest hour.
I used `.gitignore` to exclude the CSV file.

## Bonus
Python's `datetime.datetime` represents a single date and time. NumPy's `datetime64` supports datetime arrays with selectable precision. pandas provides datetime columns and `.dt` operations, which I used to extract hours and years.

## AI Assistance
After finishing the homework, I used Claude code to review my work against the assignment requirements. It suggested three changes:

- **Data path:** Use `Path(__file__).parent / "bicycle_data.csv"` instead of a hard-coded relative path, so `hw1.py` can run from any directory.
- **Plot label:** Save the figure with `bbox_inches="tight"` so the y-axis label is not cut off in `counts_by_hour.png`.
- **Git cleanup:** Add `.DS_Store` (macOS Finder metadata) and `.vscode/` (VS Code settings) to `.gitignore` so they are not pushed to GitHub.

I applied these suggestions myself.