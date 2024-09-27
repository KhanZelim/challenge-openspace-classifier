from utils.openspace import Openspace
import pandas as pd
from os import path as p
#/Users/igorafanasIev/Desktop/becode_projects/challenge-openspace-classifier/challenge-openspace-classifier/new_colleagues.csv

def read_from_csv() -> list:
    colleagueslist = []
    while True:
        path = input('Enter file path')
        print(p.exists(path))
        if p.exists(path):
            csvColleagues = pd.read_csv(path, header=None)
            for row in csvColleagues.itertuples():
                colleagueslist.append(row[1])
                print(1)
            break
        else:
            print('Incorrect path,try again')

    return colleagueslist
def ask_filename() -> None:
    filename = input('Enter the name of file you gonna save')
    try:
        classroom.store('filename')
    except:
        print('Something wrong')

classroom = Openspace()
classroom.organize(read_from_csv())
classroom.dysplay()
ask_filename()
