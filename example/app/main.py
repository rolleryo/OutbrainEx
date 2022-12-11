### OutRain Exercise ###
import requests #http://docs.python-requests.org/en/latest/
from requests import get
import ipinfo # get ip based location
import json
from flask import *
import logging

# Get a logger instance
logger = logging.getLogger()

# Set the logging level to output error messages
logger.setLevel(logging.ERROR)
# logging.basicConfig(level=logging.INFO)



def getTemp(req_city):
    if req_city == None:       
        try:
            # get external ip using http request from ipify
            external_ip = get('https://api.ipify.org').content.decode('utf8')
        except requests.exceptions.RequestException as e:
            # app.logger.error("fail to get external ip. error %s",e)         
            app.logger.info("apploger: external ip:"+external_ip)
            logger.error("external ip:"+external_ip)
            raise SystemExit(e)
        
        try:
            # get city & country according to external ip using ipinfo library
            ipinfo_token = 'd5a13af3bebba0'
            handler = ipinfo.getHandler(ipinfo_token) # create object handler 
            ipinfo_details = handler.getDetails(external_ip) # use getDetails property
            city = ipinfo_details.city
            country = ipinfo_details.country
        except requests.exceptions.RequestException as e:
            app.logger.error("apploger: fail to use ipinfo lib to get location by ip. error %s",e) 
            logger.error("failed to locate city, error "+e)
            raise SystemExit(e)
    else: 
        city = req_city
        country = "IL" # see if that is nessecary ? 
    
    ### get temp with respect to city & country 
    weatherReq = requests.get('http://api.openweathermap.org/data/2.5/weather?units=metric&q='+city+','+country+'&APPID=c766a39d9c387c7527524122df20c77f').text
    
    ### parse response using json
    data = json.loads(weatherReq)
    temp = data['main']['temp']
    ### format response as json 
    value = {
            "city": city,
            "country": country,
            "temp": temp,
            }
    jsonString = json.dumps(value)       
    return (jsonString)

def getTemp2(req_city):
    if req_city == None:
        # get external ip using http request from ipify
        external_ip = get('https://api.ipify.org').content.decode('utf8')
        print("found this external ip"+external_ip)            
        logger.info("external ip:"+external_ip)
        # get city & country according to external ip using ipinfo library
        ipinfo_token = 'd5a13af3bebba0'
        handler = ipinfo.getHandler(ipinfo_token) # create object handler 
        ipinfo_details = handler.getDetails(external_ip) # use getDetails property
        city = ipinfo_details.city
        country = ipinfo_details.country
        print("using ipinfo found the city"+city)
    else: 
        city = req_city
        country = "IL"  

    ### get temp with respect to city & country 
    weatherReq = requests.get('http://api.openweathermap.org/data/2.5/weather?units=metric&q='+city+','+country+'&APPID=c766a39d9c387c7527524122df20c77f').text

    ### parse response using json
    data = json.loads(weatherReq)
    temp = data['main']['temp']
    ### format response as json 
    value = {"city": city,"country": country,"temp": temp}
    jsonString = json.dumps(value)       
    return (jsonString)


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
app.debug = True

@app.route('/v1/api/checkCurrentWeather',methods=['GET']) # get weatheer by ip
def request_weather_by_ip(): # funcion annotation
    return getTemp2(None)

@app.route('/v1/api/checkCityWeather',methods=['GET']) # get weather by city
def request_weather_by_city(): # funcion annotation
    req_city = str(request.args.get('city')) #/?city=Haifa
    # if no city is specified it will return local ip city be default
    return getTemp(req_city) 

@app.route('/v1/api/driveStatus',methods=['POST']) # post json
def send_json(): # funcion annotation
    receivedJson = request.get_json(force=True) 
    # writeFileToDisk("input.json",receivedJson) // tried to implement with function and had issues
    try: 
        with open('input.json', 'w') as outfile:
            json.dump(receivedJson, outfile)
    except Exception as e:
        logging.error("an error occured writing the file", e)
        status = 'failure'
    else:
        status = 'success'    
    statusMessage = {
            "message": status         
            }
    return(json.dumps(statusMessage))
    

@app.route('/v1/api/driveStatus',methods=['GET']) # get drives status
def request_status(): # funcion annotation
    statusFilter = str(request.args.get('status')) 
    return (getDriveStatus(statusFilter))
    #return("status requested:"+statusFilter) 

@app.route('/',methods=['GET']) # debug method
def home():    
    return("hello, welcome to the out-rain module, please send proper endpoinst")
    # create nice html welcome 
 
if __name__ == '__main__':
    app.run(debug=True,port=7777,host='0.0.0.0') #run local server
    app.logger.info("status filter %s",request.args.get('status'))

 