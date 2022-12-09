#convert comma delimited to json in python
import json

# sample comma delimited string
data = "Name,Age,Gender,Location \n John,32,Male,USA \n Jane,25,Female,Canada"

# convert comma delimited string to list
data_list = [x.split(",") for x in data.split("\n")]

for i in data_list: print(i)
# create a list of dictionaries
data_dict = [{data_list[0][i] : data_list[j][i] for i in range(len(data_list[0]))} for j in range(1,len(data_list))]

for i in data_dict:print(i)


# for i in range(len(data_dict)):
#     for j in range(len(data_dict[i])):
#         print(data_dict[i][j],end=" ")
# print('now look at this')
# for x in data_dict[0][x]:print(x)

# convert list of dictionaries to json

data_json = json.dumps(data_dict)

# print(data_json)

# Output:
# [{"Name": "John", "Age": "32", "Gender": "Male", "Location": "USA"}, {"Name": "Jane", "Age": "25", "Gender": "Female", "Location": "Canada"}]