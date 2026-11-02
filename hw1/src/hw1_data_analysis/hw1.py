from pathlib import Path
import pandas as pd

## 1. Read the CSV file into a pandas dataframe.
DATA_PATH = Path(__file__).parent / "bicycle_data.csv"
df = pd.read_csv(DATA_PATH)

## 2. In a comment, describe the columns in the dataframe and what data types they should be. 
## If the data types in the dataframe do not match what you think they should be, update them.

# Date: observation date and hour; should be datetime.
# ... south of N 34th St Total: hourly bicycle count across both sidewalks; should be Int64.
# ... south of N 34th St Cyclist West Sidewalk: hourly west-side bicycle count; should be Int64.
# ... south of N 34th St Cyclist East Sidewalk: hourly east-side bicycle count; should be Int64.

# Show current data types
print(df.dtypes)

# Convert Date from strings to datetime.
df["Date"] = pd.to_datetime(df["Date"], format="%m/%d/%Y %I:%M:%S %p")

# Convert the three count columns from float64 to Int64.
for column in df.columns[1:]:
    df[column] = df[column].astype("Int64")
print(df.dtypes)

## 3. Add columns to the dataframe containing:
## The total (East + West) bicycle count.
## The hour of the day.
## The year.
df["Total"] = (
    df["Fremont Bridge Sidewalks, south of N 34th St Cyclist East Sidewalk"]
    + df["Fremont Bridge Sidewalks, south of N 34th St Cyclist West Sidewalk"]
)
df["Hour"] = df["Date"].dt.hour
df["Year"] = df["Date"].dt.year

## 4. Create a new dataframe with the subset of data from the year 2016.
df_2016 = df[df["Year"] == 2016]

## 5. For the dataframe you created in 4, are there any time points with missing data? 
## If so, do something to make sure missing data does not impact parts 6 and 7. 
## In a comment in the code write out the number of points with missing data.
missing_values = df_2016.isna()
missing_rows = missing_values.any(axis=1)
missing_count = missing_rows.sum() # There is 1 time point with missing data in 2016.
df_2016 = df_2016.dropna()

## 6. For the dataframe you created in 4, use pandas + matplotlib to plot the counts by hour (i.e. hour of the day on the x-axis, total daily counts on the y-axis).
## Add an appropriate title and name the axes and save the image to a file called counts_by_hour.png.
import matplotlib.pyplot as plt

hourly_counts = df_2016.groupby("Hour")["Total"].sum()

hourly_counts.plot()
plt.title("2016 Bicycle Counts by Hour")
plt.xlabel("Hour of Day")
plt.ylabel("Total Bicycle Count")
plt.savefig("counts_by_hour.png", bbox_inches="tight")

## 7. For the dataframe you created in 4, use python (and pandas) programming to computationally determine what is (on average) the busiest hour of the day.
## In a comment in the code write out the busiest hour
hourly_average = df_2016.groupby("Hour")["Total"].mean()
busiest_hour = hourly_average.idxmax()
# The busiest hour on average is 17:00.