# LSE_DA_NHS_analysis
Public Repo for LSE activities

Assignment activity 2: Import and explore the data

Running the shape attribute, we observe that the 'national_categories' dataframe is the biggest from all 3, holding 8 columns and 
almost 820k entries.
From an initial exploratory analysis, we can witness that the top 5 appointment centers hold a significantly large
number of appointment which as per desbribe function run on dataframes seams to be 10ply compared to the dataframe's mean values. 
We understand from the metadata.txt file that the data has been cleaned before presented to us,
and same can be verified by running info function on each dataframe and verifying that the columns contain the correct data type.
All 3 dataframes share the ICB code which makes it easier when we will proceed to merging for further analysis.

Assignment activity 3: Analyse the data

Drilling further down on the datasets , we checked their datatypes and transformed the date fields with datetime function allowing us 
to get min and max values or the periods of our sample. We therefore discovered that the 'AR' dataset contains appointments from December
2021 until June 2022 the 'NC' dataset contains data fromo August 2021 until June 2022. During the examed period of January to June 2022, 
we established that the amount of appointments GP service receives is 4 times higher compared to all other 4 categories combimed (as per 
our calculations GP occupies 87% of all appointments). November of 2011 was the month that recevied the biggest sum of appoinmnet per month
with last month in comparison to receive about 1.5 mil less appointments from top month. Last point discovered is that per month total records 
remain stable for the 10 months period we examined.
