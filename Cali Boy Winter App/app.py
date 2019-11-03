from flask import Flask, render_template, redirect, request, url_for
import requests

# UNCOMMENT THIS WITH API KEY WHEN RUNNING FR
key = ""

def weatherAPICall(key, latitude, longitude, save=False, weatherPath=None):
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

def citiesLoadFromJSON(citiesJSON):
    # loads cities dictionary
    with open(citiesJSON, "r") as file:
        citiesDict = json.load(file)
        print(citiesDict)
        return citiesDict

def caliBoyWinterStringify(currently):
    #takes in the currently weather data dictionary and outputs our final string
    temp = currently["temperature"]
    precipChance = currently["precipProbability"]
    windSpeed = currently["windSpeed"]
    precipType = "rain" if temp > 32 else "snow"
    out = f"It is currently {temp} degrees out. "
    out += f"There is a {precipChance} percent chance of "
    out += f"{precipType}, "
    out += f"with wind speeds of {windSpeed} miles per hour."
    qZips = int((70 - temp) // 10)

    skiGear = True if temp <= 32 else False
    rainGear = True if precipType == "rain" else False
    out += "\n Based on this we reccomend:\n"
    out += f"{qZips} Patagonia Quarter-Zips for warmth\n"
    if skiGear:
        out += "Parka, gloves, and thermals under your skinny jeans for the frigid temperature\n"
    if rainGear:
        out += "Doc Martens and a baseball cap for the rain (cause who needs unbrellas)\n"
    return out

def wrapper(key, city):
    citiesDict = citiesLoadFromJSON("./cities.json")
    lat = citiesDict[city][0]
    long = citiesDict[city][1]
    currently = weatherAPICall(key, lat, long)[0]
    caliString = caliBoyWinterStringify(currently)
    return caliString


app = Flask(__name__)

@app.route('/')
def index(city=None):
    if(city == None):
        return render_template('index.html', )
    else:
        caliString = wrapper(key, city)
        return render_template('index.html', city=city, caliString=caliString)

@app.route('/', methods=['POST'])
def indexPost():
    city = request.form["citydropdown"]



    return index(city)

if __name__ == "__main__":
	app.run(port="8001")
