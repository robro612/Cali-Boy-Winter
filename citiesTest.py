
import os, json
from datetime import datetime, time
ts = int("1572798640")

print(datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S'))


cities = "./citiesCoords.txt"

def createCitiesJSON(citiestxt):
    #
    processed = []

    with open(citiestxt, "r") as citiesRaw:
        cityLines = citiesRaw.readlines()
        cityLines = cityLines[1:]

    for line in cityLines:
        line = line.strip()
        line = line.replace("\t",",")
        line = line.split(",")
        if "" in line:
            line.remove("")
        for i in range(1, len(line)):
            line[i] = int(line[i])
        lat = round(line[1] + line[2]/60, 4)
        long = round(line[3] + line[4]/60, 4)
        line = [line[0], lat, long]
        processed.append(line)

    citiesDict = dict()
    for line in processed:
        citiesDict[line[0]] = (line[1],line[2])

    citiesJSON = json.dumps(citiesDict)
    citiesJSONDirectory = "/".join((citiestxt.split("/")[:-1])) + "/cities.json"
    print(citiesJSONDirectory)
    with open(citiesJSONDirectory, "w+") as file:
        file.write(citiesJSON)
    return citiesDict

def citiesLoadFromJSON(citiesJSON):
    with open(citiesJSON, "r") as file:
        citiesDict = json.load(file)
        print(citiesDict)
    return citiesDict

citiesLoadFromJSON("/Users/rohanmjha/Desktop/caliBoyWeather/cities.json")

createCitiesJSON(cities)
