from utils.openspace import Openspace
import csv

classroom = Openspace()
myfile = "./new_colleagues.csv"

with open(myfile, "r") as colleagues:
    csvColleagues = csv.reader(colleagues)
    for name in csvColleagues:
        print(name)