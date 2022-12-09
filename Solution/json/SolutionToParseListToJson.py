
input_list = ['name SP1, status Offline, size 4764771 MB']
output_list = [{key: value for key, value in [item.split() for item in item.split(',')] for item in input_list}]
print(output_list)
# Output: [{"name": "SP1", "status": "Offline", "size": "4764771 MB"}]