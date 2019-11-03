import requests, json
#
# key = ""
#
# g = f"{key}"
#
# #CMU: 40.4432° N, 79.9439° W
# north = 40.4432
# west = -79.9439
#
# response = requests.get(f"https://api.darksky.net/forecast/{key}/{north},{west}")
#
# print(response.status_code)
# print(response.json())
# print(type(response.json()))
#
# weather_dict = response.json()
#
#
#
#
# with open('/Users/rohanmjha/Desktop/caliBoyWeather/weather.json', 'w') as json_file:
#     json.dump(weather_dict, json_file)
weatherPath = '/Users/rohanmjha/Desktop/caliBoyWeather/weather.json'

def weatherAPICall(key, latitude, longitude, save=True, weatherPath = weatherPath):
# takes in darksky API key, and coordinates of city
# (+ is north/east, - is south/east)
# returns currently and hourly dicts of data, as well as weatherDict which is
# the all of the data from the call
# see https://darksky.net/dev/docs for specifics on parsing the dics
# saves new call to json unless otherwise specified
	apiURL = f"https://api.darksky.net/forecast/{key}/{latitude},{longitude}"
	response = requests.get(apiURL)
	weatherDict = response.json()
	currently = weatherDict["currently"]
	hourly = weatherDict["hourly"]
	if save:
		saveWeatherData(weatherPath, weatherDict)
	return (currently, hourly, weatherDict)

key = None
#YOUR DARKSKY API KEY HERE

#DONT CALL THIS FRIVILOUSLY
# weather_dict = weatherAPICall(key, 40.4432, -79.9439)
#
# with open('/Users/rohanmjha/Desktop/caliBoyWeather/weather.json', 'w') as json_file:
#     json.dump(weather_dict, json_file)
#
# print(weather_dict[2]["currently"])




def saveWeatherData(weatherPath, weatherData):
	with open(weatherpath, 'w+') as json_file:
	    json.dump(weatherData, json_file)


def loadWeatherData(weatherpath):
	with open(weatherpath, 'r') as json_file:
	    data = json.load(json_file)
	print(data)
	return (data)

def caliBoyWinterStringify(currently):
	temp = currently["temperature"]
	out = f"It is currently {temp} degrees out"
	return out

print(caliBoyWinterStringify(loadWeatherData(weatherPath)[0]))
# with open('/Users/rohanmjha/Desktop/caliBoyWeather/weather.json', 'r') as json_file:
#     data = json.load(json_file)
#
# print(type(data))
# for key in data:
# 	print(key)
#
# print(type(data["hourly"]))
# # print(data["currently"])
# print(data["currently"]["summary"])
# print(data["currently"]["precipProbability"])
# print(data["currently"]["precipType"])
# print(data["currently"]["temperature"])
# print(data["currently"]["apparentTemperature"])
# print(data["currently"]["windSpeed"])
