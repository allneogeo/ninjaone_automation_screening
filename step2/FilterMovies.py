import os
import sys
import json
from pathlib import Path

def readMovieFile():
    print("Reading data from file")
    data = None
    with open("../data/movies.json", encoding='utf-8', errors='ignore') as json_data:
        data = json.load(json_data, strict=False)
    return data

def filterMovies(movies, decade):
    startFilter = decade + 1900
    endFilter = decade + 1900 + 9
    print("Filtering data using the start year: "+str(startFilter)+" and end year: "+str(endFilter))
    #import pdb; pdb.set_trace()
    return [
        x for x in movies if x['year'] >= startFilter and x['year'] <= endFilter
    ]

def writeFilteredFile(movies, decade):
    print("Creating file")
    path_id = str(os.path.join(os.path.dirname(__file__), r"..\\data"))
    file_name = str(decade)+"s-movies.json"
    #import pdb; pdb.set_trace()
    output_file = Path(path_id + r"\\" + file_name)
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(movies, f, ensure_ascii=False, indent=4)
    
    print("File created")

if __name__ == '__main__':
    decade = int(input("Decade for search: "))
    movies = readMovieFile()
    moviesFiltered = filterMovies(movies,decade)
    writeFilteredFile(moviesFiltered, decade)
    #for run file py .\FilterMovies.py