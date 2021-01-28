# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)
# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#             print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")

# Convert a Serie into a list
temp_list = data['temp'].to_list()

# Get data in column
list_of_temp = data['temp']
# Get max value in column
max_temp = data['temp'].max()
# Get average value in column
average_temp = data['temp'].mean()

# Get data in row (by filter)
data_row = data[data['temp'] == data['temp'].max()]

# Create a Dataframe from scratch
data_dict = {
    "students": ["Tom", "Boris", "John"],
    "score": [20, 44, 36]
}
# data_create = pandas.DataFrame(data_dict)
# data_create.to_csv('new_csv.csv')


central_park_data = pandas.read_csv("central_park_data.csv")

list_of_primary_fur_color = central_park_data['Primary Fur Color']

gray_squirrel_counts = len(central_park_data[central_park_data['Primary Fur Color'] == 'Gray'])
cinnamon_squirrel_counts = len(central_park_data[central_park_data['Primary Fur Color'] == 'Cinnamon'])
black_squirrel_counts = len(central_park_data[central_park_data['Primary Fur Color'] == 'Black'])

dict_primary_fur_color = {
    "color": ['Gray', 'Cinnamon', 'Black'],
    "score": [gray_squirrel_counts, cinnamon_squirrel_counts, black_squirrel_counts]
}

create_DF = pandas.DataFrame(dict_primary_fur_color)
create_DF.to_csv('squirren_count.csv')