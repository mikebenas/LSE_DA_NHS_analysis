# LSE_DA_NHS_analysis
Public Repo for LSE activities

Assignment activity 2: Import and explore the data

Running the shape attribute, we observe that the 'national_categories' dataframe is the biggest from all 3, holding 8 columns and almost 820k entries.
From an initial exploratory analysis, we can witness that the top 5 appointment centers hold a significantly large
number of appointment which as per desbribe function run on dataframes seams to be 10ply compared to the dataframe's mean values. 
We understand from the metadata.txt file that the data has been cleaned before presented to us,
and same can be verified by running info function on each dataframe and verifying that the columns contain the correct data type.
All 3 dataframes share the ICB code which makes it easier when we will proceed to merging for further analysis.