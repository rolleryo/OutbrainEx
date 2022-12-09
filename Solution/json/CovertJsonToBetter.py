
import json

myjson = {"SP 3": "name SP4, status Offline, size 4764771 MB, free 2333948 MB, path /dev/sdk, log 0 MB, port 5660, guid db53cc9f02524622005b30b0eb0947e3, clusterUuid -8650609094877646407--116798096584060989, disks /dev/sdk /dev/sdl /dev/sdm, dare 1"}

mydict = {}

for k,v in myjson.items():
  lst = v.split(',')
  for item in lst:
    key,val = item.split(' ')
    if key == 'disks':
      mydict[key] = [x.strip() for x in val.split(' ')]
    elif key == 'dare':
      mydict[key] = int(val)
    else:
      mydict[key] = val

newjson = json.dumps(mydict)

print(newjson)