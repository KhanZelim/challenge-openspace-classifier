from utils.openspace import Openspace
import pandas as pd
from os import path as p
import tkinter as tk
from tkinter.filedialog import askopenfile

def read_from_csv() -> list:
    """
        Function read csv file with names of colleagues and returns list of colleagues.
        :return:colleagueslist list of colleagues.
    
    """
    root = tk.Tk()
    root.withdraw()

    colleagueslist = []
    path = askopenfile(mode ='r', filetypes =[('CSV Files', '*.csv')])
    csvColleagues = pd.read_csv(path, header=None)
    for row in csvColleagues.itertuples():
        colleagueslist.append(row[1])
    return colleagueslist

def ask_filename() -> None:
    """
    Function asks user about name of file with seatmap of openspace,
        and about format of file.
    :return: None
    """
    filename = input('Enter the name of file you gonna save')
    try:
        classroom.store(filename)
    except:
        print('Something wrong')

def ask_about_size() -> Openspace:
    """
        Function allows user to set up quantity of tables en seats per each table.
        :return: Openspace created instance of class Openspace.

    """
    while True:
        set_up_classroom_in = input("""
                                You want set up the size of Classroom or run with default size, 6 tabels X 4 seats?
                                D : for default
                                S : set up size

                                """)
        match set_up_classroom_in:
            case 'D':
                classroom = Openspace()
                return classroom
            case 'S':
                while True:
                    try:
                        t_size_input = input('Please,set quantity of tabels in the room. Maximal size is 10')
                        if int(t_size_input) <= 10:
                            s_size_input = input('Please,set quantity of seats per one tabel.Tabel can fit  8 seats only')
                            if int(s_size_input) <= 8:
                                classroom = Openspace(number_of_tables=int(t_size_input),table_capacity=int(s_size_input))
                                return classroom
                            else:
                                print("You've entered to big number for seats.\nTry again.")
                        else:
                            print("You've entered to big number for tables.\nTry again.")

                    except:
                        print('This isn\'t number, try again')
            case _:
                print('You write wrong leter, try again.')

classroom = ask_about_size()
classroom.organize(read_from_csv())
#classroom.dysplay()
ask_filename()
