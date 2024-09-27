from utils.openspace import Openspace
import pandas as pd

# Declare variables
classroom = Openspace()
colleagueslist = []

# Read the file and append the list with the names
csvColleagues = pd.read_csv("new_colleagues.csv", header=None)
for row in csvColleagues.itertuples():
    colleagueslist.append(row[1])

# Seat everybody, display it and store it
classroom.organize(colleagueslist)
classroom.display()
classroom.store("output.xlsx")