import json

# read the json file 
with open("input.json",'r') as myfile:
  data = myfile.read()
# data = {
#   "SP 0": "name SP1, status Offline, size 4764771 MB",
# "SP 1": "name SP2, status Online, size 4764771 MB",
# "SP 2": "name SP3, status Online, size 4764771 MB"
# }

# lets extract the value only from input.json
# print(data)
y = json.loads(data)
input_list = list(y.values())

print(input_list)
# input_list = ['name SP1, status Offline, size 4764771 MB']

for x in input_list:  
    output_list = [{key: value for key, value in [item.split() for item in item.split(',')] for item in x}]
    print(output_list)
# Output: [{"name": "SP1", "status": "Offline", "size": "4764771 MB"}]