import os
import sys
import json
from pathlib import Path

def getDataFromFile():
    allData = None
    with open("../data/80s-movies.json", encoding='utf-8', errors='ignore') as json_data:
        allData = json.load(json_data, strict=False)
    for data in allData:
        for i in range(len(data['cast'])):
            data['cast'][i] = data['cast'][i].lower()
    return allData

def listActorsInMovie(movie, array):
    for actor in movie['cast']:
        if actor not in array:
            array.append(actor.lower())

def startProcess(array, allData, allNames, target):
    if (len(array) > 9):
        return None
    else:
        namesOfLevel = []
        for actor in array[len(array) - 1]:
            movies = [
                x for x in allData if actor in x['cast']
            ]
            for movie in movies:
                listActorsInMovie(movie,namesOfLevel)
        if target.lower() in namesOfLevel:
            print("Degrees of Separation: "+str(len(array) + 1))
            return len(array)
        else:
            temp3 = [item for item in namesOfLevel if item not in allNames]
            for name in temp3:
                allNames.append(name)
            array.append(temp3)
            startProcess(array,allData,allNames,target)

def valideIfPersonExists(actorName, allData):
    result = None
    temp_array = [
        x for x in allData if actorName.lower() in x['cast']
    ]
    if len(temp_array) > 0:
        result = actorName.lower()
    return result

def main():
    print("Loading data...")
    allData = getDataFromFile()
    print("Data loaded.")
    # source = "Robert Hays"
    # target = "William Hurt"
    source = valideIfPersonExists(input("Actor 1: "),allData)
    if source is None:
        sys.exit("Person not found.")
    target = valideIfPersonExists(input("Actor 2: "),allData)
    if target is None:
        sys.exit("Person not found.")
    a = [[source.lower()]]
    b = [source.lower()]
    startProcess(a,allData,b,target)
    print("There are "+str(len(a))+" degrees of separation between "+source+" and "+target)

if __name__ == "__main__":
    main() 