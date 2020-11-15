import pandas as pd

# denote spreadsheets
excel_file_1 = 'Workbook_1.xlsx'
excel_file_2 = 'Workbook_2.xlsx'

#read in spreadsheets
df1 = pd.read_excel(excel_file_1)
df2 = pd.read_excel(excel_file_2)

# Filter by conditions
#Filtering by the names of the second sheet to find the names corresponding values on the second.
filtered_frame_1 = df1.loc[(df1['Name'].isin(df2['Name']))] # Based on another sheet

#Same logic applied here but the inverse is applied using the squiggle
filtered_frame_2 = df1.loc[~(df1['Name'].isin(df2['Name']))] # Inverse

#Here we are applying multiple search criteria across both workbooks.
filtered_frame_3 = df1.loc[(df1['Name'].isin(df2['Name'])) & (df1['Interview Score'] == 4) | (df1['YR Experience'] == 3)] # Multiple Filters

#This function simply merges both the dataframes together into one dataframe
all_frames = [df1, df2]
all_df = pd.merge(df1, df2, on='Name')

#This filter is simply retrieving two features with the desired parameters
filtered_frame_4 = all_df.loc[(all_df['YR Experience'] == 5) & (all_df['Group Interview Score'] == 4)]
