# with open('wether_data.csv') as data:
#     report = data.readlines()
#     print(report)


# import csv 

# with open('wether_data.csv') as data:
#     report = csv.reader(data)
#     for row in report:
#         if row[1] != "temp":
#             print(row[1])
        

#? pandas data analysis library to handle tabular data

import pandas 

data = pandas.read_csv('wether_data.csv')
# print(data['temp'])

temp_list = data['temp'].to_list()
count = len(temp_list)

total = 0
for val in temp_list:
    total = total + val 

print(total/count)


print(data['temp'].max())

#? getting data in pandas has 2 way data['temp'] or data.temp