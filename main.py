from utils.openspace import Openspace
import pandas as pd
from os import path as p
#"/Users/igorafanasIev/Desktop/becode_projects/challenge-openspace-classifier/challenge-openspace-classifier/new_colleagues.csv"

classroom = Openspace()
colleagueslist = []
while True:
    path = input('Enter file path')
    if p.exists(path):
        csvColleagues = pd.read_csv(path, header=None)
        for row in csvColleagues.itertuples():
            colleagueslist.append(row[1])
        break
    else:
        print('Incorrect path,try again')

classroom.organize(colleagueslist)
classroom.dysplay()
filename = input('Enter the name of file you gonna save')
try:
    classroom.store(f'{filename}')
except:
    print('Something wrong')