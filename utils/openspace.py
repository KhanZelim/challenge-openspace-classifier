from typing import Self
from .table import Table 
from .file_utils import *
import random
import pandas as pd

class Openspace:
    def __init__(self, number_of_tables: int =6, table_capacity: int =4):
        """
        Constructor of class Openspace.
            
        :param: number_of_tabels: An int that perform number of tables available.
        :param: tabel capacity: An int that performe number of seats per one table available
        """
        self.number_of_tables = number_of_tables
        self.table_capacity = table_capacity
        self.tables = [Table(table_capacity) for _ in range(number_of_tables)]
        self.names = []
        self.capacity = sum([table.capacity for table in self.tables])
        self._flag = False
        
    def __str__(self) -> str:
        """
        String representation of the tables and seats
        
        :return: str representing the tables and the seats 
        """
        final_string = ''
        for index, table in enumerate(self.tables, start=1):
            final_string= final_string + f'Tabel#{index}\n{str(table)}\n'
            for index,seat in enumerate(table.seats, start=1):
                final_string= final_string + f'\t\tChair #{index} {str(seat)}\n'
        return final_string
    
    def has_space(self) -> bool:
        """
        Function that checks if there's a table with a free spot
        
        :return: bool depending on if there are any free spots
        """
        for table in self.tables:
            if table.has_free_spot():
                return True
        else:
            return False
        
    
    def add_table(self) -> None:
        """Function is adding extra table to Openspace"""
        self.tables.append(Table(self.table_capacity))
        self.capacity += self.table_capacity
        self.number_of_tables += 1


    def add_seat_to_all_tables(self) -> None:
        """Function that adds one seat to each table"""
        self.table_capacity += 1
        self.capacity += self.number_of_tables
        for table in self.tables:
            table.add_seat()
            

    
    def add_both(self) -> None:
        """Function that adds one tabel, and one seat to each tabel"""
        self.add_table()
        self.add_seat_to_all_tables()



    def assign_occupants(self, name) -> None:
        """
        Function that assing occupant to the random choised tabel
            
        :param name: str representing the name of the occupant
        """
        min_cap = min([table.capacity for table in self.tables])
        bool_list = [table.capacity == min_cap for table in self.tables]

        while True:
            chosen_tabel = random.choice(self.tables)           
            if chosen_tabel.has_free_spot():
                if chosen_tabel.capacity > min_cap:
                    chosen_tabel.assign_seat(name)
                    break
                elif bool_list.count(True) == self.number_of_tables:
                    chosen_tabel.assign_seat(name)
                    break
                else:
                    continue                   
            else:
                continue

    def avoiding_loneliness(self) -> None:
        """Function that checks if there's a table with a single occupant"""
        for table in self.tables:
            if table.capacity == (self.table_capacity - 1):
                for seat in table.seats:
                    if not seat.free:
                        self.names.append(seat.occupant)
                        seat.remove_occupant()
            else:
                try:
                    table.assign_seat(self.names.pop())
                    self.capacity -= 1
                except:
                    continue
        else:
            while len(self.names) != 0:
                for table in self.tables:
                    if table.capacity == self.table_capacity:
                        [table.assign_seat(self.names.pop()) for i in range(len(self.names))]
                        self.capacity -= 1
  
    def is_enough_space(self, names: list) -> bool:
        """
        Function that checks if there is enough capacity for all
        
        :param names: list of names
        :return: bool depending on of there's enough capacity 
        """
        if self.capacity < len(names):
            return False
        else:
            return True
    
    def implement_decision(self, flag: str, names: list ) -> None:
        """
        Function that implements a decision according to flag returned by file_utils.too_many_quest
        
        :param: flag string, decision flag
        """
        match flag:
            case 'T':
                self.add_table()
            case 'S':
                self.add_seat_to_all_tables()
            case 'N':
                self._flag = True
                self.names = names
            case 'B':
                self.add_both()

    def organize(self, names : list) -> None:
        """
        Function that randomly assigns people to the seats of the tables
        
        :param names: list of employees
        """
        if self.is_enough_space(names):
            for name in names:
                self.assign_occupants(name)
            self.avoiding_loneliness()
        else:
            flag = too_many_quest(names,self.number_of_tables, self.table_capacity)
            self.implement_decision(flag, names)
            if self.capacity > len(names):
                for name in names:
                    self.assign_occupants(name)
                self.avoiding_loneliness()
                                    
    def display(self) -> None:
        """Function that displays the tables and its occupants in a nice and readable way"""
        for index, tabel in enumerate(self.tables, start=1):
            print(f'Tabel#{index}\n{str(tabel)}')
            for index, seat in enumerate(tabel.seats, start=1):
                print(f'Chair #{index} {str(seat)}')

    def store(self, filename: str) -> None:
        """ 
        Function that stores the repartition in an excel file
            
        :param: string that represent files name
        """
        repartition_dict = {f'Table {i + 1}': [f'Seat #{index} {str(seat)}' for index, seat in enumerate(tabel.seats, start=1)] 
                            for i, tabel in enumerate(self.tables)
                            }
        df = pd.DataFrame(repartition_dict.items(), columns = ['Tables', 'Seats'])
        df.to_excel(filename, index= False)