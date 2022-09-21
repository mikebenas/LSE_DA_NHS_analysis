#Import Pandas
import pandas as pd

# Create a dictionary.
data = {'Name': ['Shen Lee', 'Leon Buhle', 'Tracy Adams', 
                'Lebo Sinuka', 'Lauren Pierce', 'Monica Bond',
                'Natahs Allsopp', 'Nicholas Winter', 'Christopher Eckson', 
                'Siobhan O\' Malley'],
        'Annual': [23, 20, 15, 19, 21, 21, 10, 15, 16, 23],
        'Sick': [10, 8, 10, 9, 7, 10, 9, 10, 8, 5],
        'Personal': [5, 4, 5, 0, 5, 2, 5, 4, 2, 5],
        'Bonus': [3, 0, 0, 3, 3, 6, 0, 3, 6, 3],
        'Total Leave Taken': [0, 3, 5, 10, 5, 8, 11, 9, 15, 5],
        'Total Leave Available': [38, 32, 30, 28, 33, 33, 24, 29, 26, 33],
        'Annual Total': [38, 35, 35, 38, 38, 41, 35, 38, 41, 38],
        }


#Create list with the row labels
row_labels = [215, 216, 217, 218, 219, 220, 221, 222, 223, 224]

#Create Dataframe
leave_cycle=pd.DataFrame (data,columns=['Name', 'Annual', 'Sick', 
                                        'Personal', 'Bonus', 
                                        'Total Leave Taken',
                                        'Total Leave Available'],
                                        index = row_labels)

# Specify index name
leave_cycle.index.name = 'Personnel_ID'

# Print the DataFrame
print (leave_cycle)