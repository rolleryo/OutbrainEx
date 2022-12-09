import json

# read file

# status_filter = "Online"
# with open("input.json", "r") as myfile:
#     lines = myfile.readlines()
#     s1 = "hello"
#     for x in lines: 
#             s1 = s1 + x
#             print (s1)
#     print((' '.join(lines)).count("Offline"))
  
csv_file_path = input.json
json_file_path = output.json

with open(csv_file_path, encoding = 'utf-8') as csv_file_handler:

    with open(json_file_path, 'w', encoding = 'utf-8') as json_file_handler:
    
        json_file_handler.write(json.dumps(data_dict, indent = 4))


  
    #  for x in lines: 
    #     if (x.find(status_filter)>0):print(x)
#print(lines[1])
#print(json.loads(lines[1]))

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