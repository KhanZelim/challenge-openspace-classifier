from utils.openspace import Openspace
import pandas as pd

classroom = Openspace()
colleagueslist = []

csvColleagues = pd.read_csv("new_colleagues.csv", header=None)
for row in csvColleagues.itertuples():
    colleagueslist.append(row[1])

classroom.organize(colleagueslist)
classroom.dysplay()