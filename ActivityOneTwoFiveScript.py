# Write a program to analyse real estate data
#Put all columns in lists
#For Property Price list missing an item we have inserted missing value (ie PropertyPrice=SalesPrice-Commission)
PropertyID=['A','B','C','D','E']
SalesPrice=[45000,23400,67000,34600,12900]
Comm=[5000,3400,6500,4000,1500]
PropertyPrice=[40000,2000,60500,30600,11400]


#Function to get average of a list
def Average(PropertyPrice):
    return sum(PropertyPrice) / len(PropertyPrice)
  
# Driver Code
average = Average(PropertyPrice)
  
# Printing average of the Sales Price
print("Average of the Property Price is $", round(average, 2))
# Printing Total sales
print ("Total sales for the month is $" , sum(SalesPrice),)