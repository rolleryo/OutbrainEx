import json

# read file

status_filter = "Online"
with open("input.json", "r") as myfile:
     lines = myfile.readlines()
    #  for x in lines: 
    #     if (x.find(status_filter)>0):print(x)
#print(lines[1])
print(json.loads(lines[1]))

# # print(json.dumps(lines[1]))

#     input_json=myfile.read()
#     #Transform json input to python objects
#     input_dict = json.loads(input_json)

#     print (json.dumps(input_dict))
#     print(input_dict)
# # # Filter python objects with list comprehensions
# output_dict = [x for x in input_dict if x['status'] == 'Online']

# # Transform python object back into json
# output_json = json.dumps(output_dict)

# # Show json
# print(output_json)





myfile.close
    # # show values
    # print("usd: " + str(obj['usd']))
    # print("eur: " + str(obj['eur']))
    # print("gbp: " + str(obj['gbp']))