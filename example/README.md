Hello, 

these are the file included in the solution folder

app\main.py
dockerfile
input.json'
.dockerignore


to build the docker image please 
navigate to the example folder and type in the terminal

	docker build -t or-api .


to run the container please type

	docker run -it -p 7777:7777 --name outrain-api or-api

	docker run -it -p 7777:7777 or-api

to query the service you may use the following

127.0.0.1:7777/v1/api/checkCityWeather
127.0.0.1:7777/v1/api/checkCityWeather?city=Haifa
127.0.0.1:7777/v1/api/driveStatus?status=Offline
127.0.0.1:7777/v1/api/driveStatus?status=Online
127.0.0.1:7777/v1/api/driveStatus (must include a json file in the body) 

for your conveniencce, you may import the import the "Outbrain API postman collection" to the postman app. 