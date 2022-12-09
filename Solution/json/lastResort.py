#last resort
# create key = "message", value = the disks status
# create temp_data --> 
# get the json
# extract the values only as list
# scan each row , and for every list item in the row, create key for 1st value and value for the 2nd
# if this is disk then create a list 


# creat key "data" , value = temp_data


import json

# data = {
#     "name": "Bob",
#     "age": "25",
#     "location": "NYC"
# }

# data = {
#     "sp 0": "yoav",
#     "sp 1": "eilat"
#     }

with open ("input.json",'r') as myfile:
    data = myfile.read()
    print (data)

# values = list(data.values())
# print(values)
