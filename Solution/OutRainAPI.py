### OutRain Exercise ###

import requests #http://docs.python-requests.org/en/latest/
from requests import get
import ipinfo # get ip based location
import json
from flask import *

def getTemp(req_city):
    if req_city == None: 
        # get external ip using http request from ipify
        external_ip = get('https://api.ipify.org').content.decode('utf8')
        # get city & country according to external ip using ipinfo library
        ipinfo_token = 'd5a13af3bebba0'
        handler = ipinfo.getHandler(ipinfo_token) # create object handler 
        ipinfo_details = handler.getDetails(external_ip) # use getDetails property
        city = ipinfo_details.city
        country = ipinfo_details.country
    else: 
        city = req_city
        country = "IL"
    try:
        ### get temp with respect to city & country 
        weatherReq = requests.get('http://api.openweathermap.org/data/2.5/weather?units=metric&q='+city+','+country+'&APPID=0a1e14ce198f208c5665f1b1a6bb4879').text
    except requests.exceptions.RequestException as e:  # This is the correct syntax
        raise SystemExit(e)
    
    ### parse response using json
    data = json.loads(weatherReq)
    temp=data['main']['temp']

    ### format response as json 
    value = {
            "city": city,
            "country": country,
            "temp": temp,
            }
    jsonString = json.dumps(value)
    
    return (jsonString)
    # is process aborted when exception ? is the exception raise enought or need return ? 

#   Drive Status
def getDriveStatus(statusFilter):
    with open("input.json", "r") as myfile:
     lines = myfile.readlines()
     statusCount = (' '.join(lines)).count(statusFilter)
     result = ""
     for eachDrive in lines: 
        if (eachDrive.find(statusFilter)>0):
            print(eachDrive)
            result += eachDrive 
     return("found "+str(statusCount)+" "+statusFilter+" drives\n" +result) 
     # fix capital letters depentend statusFilter  
     
#  API service
app = Flask (__name__)  # creat the flask app with project name
# app.debug = True

@app.route('/v1/api/checkCurrentWeather',methods=['GET']) # create the endpoint
def request_weather(): # funcion annotation
    return getTemp(None)

@app.route('/v1/api/checkCityWeather',methods=['GET']) # create the endpoint
def request_weather_by_city(): # funcion annotation
    req_city = str(request.args.get('city')) #/?city=Haifa
    # insert validity check....if argument exist...
    return getTemp(req_city) 

@app.route('/v1/api/driveStatus',methods=['POST']) # create the endpoint
def send_json(): # funcion annotation
    receivedJson = request.get_json(force=True) 
    # writeFileToDisk("input.json",receivedJson) // tried to implement with function and had issues
    try: 
        with open('input.json', 'w') as outfile:
            json.dump(receivedJson, outfile)
    except Exception as e:
        print("an error occured writing the file", e)
        status = 'failure'
    else:
        status = 'success'    
    statusMessage = {
            "message": status         
            }
    return(json.dumps(statusMessage))
    

@app.route('/v1/api/driveStatus',methods=['GET']) # create the endpoint
def request_status(): # funcion annotation
    statusFilter = str(request.args.get('status')) 
    return (getDriveStatus(statusFilter))
    #return("status requested:"+statusFilter) 
 
if __name__ == '__main__':
    app.run(port=7777) #run local server
    # app.run(debug=True, host='0.0.0.0', port=7777)
    
    app.logger.info("status filter %s",request.args.get('status'))
