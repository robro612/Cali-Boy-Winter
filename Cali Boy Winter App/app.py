from flask import Flask, render_template, redirect, request, url_for
import requests

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
	return out



app = Flask(__name__)

@app.route('/')
def index(city=None):
    if(city == None):

    citiesDict = citiesLoadFromJSON("./cities.json")
    if city in citiesDict:
        finalString =
        return render_template('index.html', )


        return render_template('index.html')
    else:
        # do actual stuff here
        return render_template('index.html', **locals())

@app.route('/', methods=['POST'])
def indexPost():
    city = request.form["citydropdown"]



    return index(city)

if __name__ == "__main__":
	app.run(port="8001")
