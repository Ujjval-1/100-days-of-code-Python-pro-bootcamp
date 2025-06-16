# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)



# import csv
#
# with open ("weather_data.csv") as data_file:
#     data= csv.reader(data_file)
#     temp = []
#     for row in data:
#         if row[1]!="temp":
#             temp.append(int(row[1]))
#     print(temp)


import pandas

data= pandas.read_csv("weather_data.csv")
# print(type(data))         # Dataframe(whole sheet)
# print(data["temp"])
# print(type(data["temp"]))         # Series(a column in sheet is called series)

# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(temp_list)
#
# print(data["temp"].mean())
# print(data["temp"].max())

# Get data in columns
# print(data["condition"])
# print(data.condition)

# get data in rows

# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])
#
# monday = data[data.day == "Monday"]
# monday_temp = monday.temp[0]
# monday_temp_f = monday_temp * 9/5 +32
# print(monday_temp_f)

# Create a dataframe from scratch
# data_dict = {"students":["lappu","tappu","pappu"],
#              "scores":[80,60,87]}
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")

