#Import Pandas
import pandas as pd

# Create a dictionary.
data = {'Name': ['Thando', 'Divya', 'Simon', 'Peter'],
        'Country': ['South Africa', 'Singapore', 'United Kingdom', 'Australia'],
        'Qualification': ['Phd', 'Diploma', 'BSc', 'MBA'],
        'Age': [29, 20, 25, 23],}
        
# Create a DataFrame from the dictionary.
students = pd.DataFrame(data)

# Print the DataFrame
print (students)