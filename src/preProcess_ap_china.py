# Data Pre-Processing for China Air Pollution Analysis
# Steps: [1] Data Cleaning (including splicing by city), [2] Data Transformation
# and Dimensionality Reduction

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Concatenate hour, month, and year columns into
# single datetime column
def cast_to_datetime(df):
    # Create datetime column in each dataframe
    df['Datetime'] = pd.to_datetime(dict(year=df['Year'], month=df['Month'],day=1, hour=df['Hour']))

    # Now with datetime column, drop unneeded year, month, hours columns
    df.drop(columns=['Year', 'Month',  'Hour'], inplace=True)

    # Return datetime transformed dataframe
    return df

# Check for any Air Quality Index (AQI) values that are
# outliers and remove any outliers from dataset
def detect_outlier(df):
    # Use IQR method for detecting outliers
    Q1 = df['AQI'].quantile(0.25)
    Q3 = df['AQI'].quantile(0.75)

    IQR = Q3 - Q1
    
    # Lower and upper bounds for outliers
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    # Remove rows from dataframe if AQI value is outlier in that row
    outliers_removed_df = df[(df['AQI'] >= lower_bound) & (df['AQI'] <= upper_bound)]
    
    # Return dataframe with AQI outliers removed
    return outliers_removed_df

def pre_processing(df):
    # Data Cleaning and DF Splicing by City
    # Print number of data points and number of feature variables
    print(f"The dataset contains {df.shape[0]} data points with {df.shape[1]} columns")

    # Print names of columns of dataset
    print(f"Columns of dataset: {df.columns}")

    # Check for any missing values in the dataset
    if (df.isnull().values.any() == True):
        print("There are missing values in the dataset")
    else:
        print("There are no missing values in the dataset")

    # Check for any duplicate values in the dataset
    if (df.duplicated().values.any() == True):
        print("There are duplicate rows in the dataset")
    else:
        print("There are no duplicate rows in the dataset")
    
    # List unique cities in dataset
    cities = df['City'].unique()
    print(f"The cities contained in the dataset are {cities}")

    # Splice entire dataset into dataframes for each city
    shenzhen = df.loc[df['City'] == 'Shenzhen']
    shanghai = df.loc[df['City'] == 'Shanghai']
    beijing = df.loc[df['City'] == 'Beijing']
    chengdu = df.loc[df['City'] == 'Chengdu']
    guangzhou = df.loc[df['City'] == 'Guangzhou']

    # List of dataframes for each city
    df_cities = [shenzhen, shanghai, beijing, chengdu, guangzhou]
    # Pass each dataframe for each city to detect_outlier function
    i = 0
    while(i < len(df_cities)):
        detect_outlier(df_cities[i])
        i += 1
    
    # Cast year, month, hour columns into single datetime column
    j = 0
    while (j < len(df_cities)):
        cast_to_datetime(df_cities[j])
        j += 1

    return shenzhen, shanghai, beijing, chengdu, guangzhou

def main():
    df = pd.read_csv('air_pollution_china.csv')
    pre_processing(df)

if __name__ == "__main__":
    main()



