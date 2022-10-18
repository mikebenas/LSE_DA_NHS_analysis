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

Assignment activity 4: Analyse the data

During this part of our analysis, we plotted visualisations indicating the number of appointments per month for service settings, context types, and national categories(for the studied period between August 2021 until June 2022. The plot of service settings against the sum of count of appointments show that the dominant category is General Practice with all other 4 (which included the unmapped and other) occupying relatively low numbers (all four combined). Possible reason could be that while filling in the appointments correct input is not always inserted (before submitting check again metadata file). Following plot visualization is the context types where there is practically only one category (Care Related Encounter) as the rest two refer to inconsistent mapping or unmapped data so not many conclusions to be drawn apart from possible data accuracy imporovement if data entry utilises the correct context setting. On the third plot, we have to represent 18 categories which make for a very busy plot, that is why we took the liberty to plot just the first 6 top categories. Top result is the general consulation routine category with second in place the general consulation acute. What is worrying on this plot is that the incosistent mapping gathers a high percentage of appointements.Following objective was concentrated on analysing the trends observed on daily appointments observed around 4 seasons. Analysis on August, Decemeber March and June show between them the same pattern with high volume of appointments during the weekdays that falls drastically during the weekends (timeseries forecasting Seasonality refers to fluctuations in the pattern due to seasonal determinants. A time-series has a seasonal component if we can see a recurrent pattern with a fixed and known duration. For example, monthly, weekly, or daily).Trend here might suggest obvious solution for decongestation of servgice by trying to shift workload during weekends  (with all that may implicate)

Assignment activity 5: Analyse the Twitter data

By exploring the twitter trending hashtags related to healthcare in the UK , we found some interesting points where we could offer some insights.
All of the twitter hashtags studies had healthcare related words which means might not be an exact match for the topic of our data analysis but they certainly
provide us with a good general picture of what is trending on the healthline industry on Twitter.
When analysed the retweeted tweets and the favored tweets one would expect that the figures from those columns would go along. Though what is also established in the social media universe is that trends don't always show the real image of the case. Something that may be forwarded/shared multiple times doesn't mean it is also favored as much at the same time. The famous saying :"There is no such thing as bad publicity" unfortunately doesn't have a place in the healthcare industry.
Further plotting our results we can see that using the hashtag "healthcare" will guarantee viewing of our tweeter campain as it is encountered with very big difference from second hashtag in place. In order to make our plot more readable and view that results with count over 10 were not closely related to our study, we also produced a graph basis the top 15 used hashtag from our twitter feeds analysis.

Assignment activity 5: Make recommendations

We analyse the appointments_regional dataset filtered to include dates from Aug 2021 until Jun 2022. Summing up count of appointments per month, we created a new column indicating a daily average. The highest numbers show 1,013,502.3 average count per day on the busiest month . As indicated, the NHS can accommodate a maximum of 1,200,000 appointments per day which clearly answers our first question that from that comparison alone we have no obvious argument to propose increase of staff levels. 
