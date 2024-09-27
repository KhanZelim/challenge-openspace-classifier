from utils.openspace import Openspace
import pandas as pd

classroom = Openspace()
colleagueslist = []

csvColleagues = pd.read_csv("/Users/igorafanasIev/Desktop/becode_projects/challenge-openspace-classifier/challenge-openspace-classifier/new_colleagues.csv", header=None)
for row in csvColleagues.itertuples():
    colleagueslist.append(row[1])
print(colleagueslist)

classroom.organize(colleagueslist)
classroom.dysplay()