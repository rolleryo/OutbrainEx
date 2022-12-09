import json

# # [1,2,3],[4,5,6].,

# data = [[1,2,3],[4,5,6],[7,8,9]]
# # for x in data: print(x)

# for i in range(len(data)):
#     for j in range(len(data[i])):
#         # print(data[i][j],end=" ")



# myList = [{name'a': 54}, {'b': 41, 'c':87}]
# jsonString = json.dumps(myList, indent=4)
# # print(jsonString)


x = '{ "name":"John", "city":"New York"}'

new = json.loads(x)
print(new)