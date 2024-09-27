from typing import Self
from table import Table 
from file_utils import *
import random
import pandas as pd




class Openspace:
    def __init__(self,number_of_tables: int = 6, table_capacity: int = 4) -> Self:
        """
            Constructor of classs Openspace.
            :param: number_of_tabels: An int that perform number of tables available.
            :param: tabel capacity: An int that performe number of seats per one table available 
            :return: instance of class Openspace 
        """
        self.number_of_tabels = number_of_tables
        self.table_capacity = table_capacity
        self.tables = [Table(table_capacity) for i  in range(number_of_tables)]
        self.names = []
        self.capacity = sum([table.capacity for table in self.tables])
        self._flag = False
        
        

    def __str__(self) -> str:
        """
            Function that print reade
            :param: None
            :return: String
        
        """
        final_string = ''
        for index,tabel in enumerate(self.tables,start=1):
            final_string= final_string + f'Tabel#{index}\n{str(tabel)}\n'
            for index,seat in enumerate(tabel.seats, start=1):
                final_string= final_string + f'\t\tChair #{index} {str(seat)}\n'
        return final_string
    
    def has_space(self) -> bool:
        """
            Function is checking if there is space in openspace available
            :return: bool, True if there is space, Fals if not.
        """
        for tabel in self.tables:
            if tabel.has_free_spot():
                return True
        else:
            return False
        
    
    def add_table(self) -> None:
        """
            Function is adding extra table to Openspace
            :return:None
        """
        self.tables.append(Table(self.table_capacity))
        self.capacity += self.table_capacity
        self.number_of_tabels += 1


    def add_seat_to_all_tables(self) -> None:
        """
            Function is adding one seat to each tabel in Openspace
            :return:None

        """
        self.table_capacity += 1
        for table in self.tables:
            table.add_seat()
            

    
    def add_both(self) -> None:
        """
            Function is adding one tabel, and one seat to each tabel in Openspace
            :return:None

        """
        self.table_capacity +=1
        self.add_table()
        self.add_seat_to_all_tables()



    def assing_occupants(self,name) -> None:
        """
            Function that assing occupant to the random choised tabel
            :param: string, name of occupant
            :return: None.
        """
        min_cap = min([table.capacity for table in self.tables])
        counter = 0
        while counter < len(self.tables):
            counter+=1
            choised_tabel = random.choice(self.tables)
            if choised_tabel.capacity == min_cap or not choised_tabel.has_free_spot():
                continue
            else:
                choised_tabel.assign_seat(name)
                break
        else:
            choised_tabel.assign_seat(name)


    def avoiding_loneliness(self) -> None:
                """
                    Function that does not allow a table with a single employee.
                    :return: None.
                
                """
                for tabel in self.tables:
                    if tabel.capacity == (self.table_capacity - 1):
                        for seat in tabel.seats:
                            if not seat.free:
                                self.names.append(seat.occupant)
                                seat.remove_occupant()
                    else:
                        try:
                            tabel.assign_seat(self.names.pop())
                        except:
                            continue
                else:
                    while len(self.names) != 0:
                        for tabel in self.tables:
                            if tabel.capacity == self.table_capacity:
                                [tabel.assign_seat(self.names.pop()) for i in range(len(self.names)) ]

    
    
    def is_enough_space(self,names : list) -> bool:
        """
            Function that chek if in openspace enough space for all employes
            :param names: List of employees present in the office.
            :return: bool, True if enough, False if not 
        """
        if self.capacity < len(names):
            return False
        else:
            return True
    
    def implemnt_decision(self,flag : str,names : list ) -> None:
        """
            Function implements decision according to flag returned by file_utils.to_many_quest 
            :param: flag string, decision flag
            :return: None      
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


    def organize(self,names : list) -> None:
        """
            Function that randomly assing peopel to Seat objects in the different Table objects .
            :param names: List of employees present in the office.
            :return: Nothing
        """
        if self.is_enough_space(names):
            for name in names:
                self.assing_occupants(name)
                self.avoiding_loneliness()
        else:
            flag = to_many_quest()
            self.implemnt_decision(flag,names)
        
    
        
                    
                
    def dysplay(self) -> None:
        """
            Function that display the different Tables and there occupants in a nice 
            and readable way.
            :param: None.
            :return: Nothing.
        """
        for index,tabel in enumerate(self.tables,start=1):
            print(f'Tabel#{index}\n{str(tabel)}')
            for index,seat in enumerate(tabel.seats, start=1):
                print(f'Chair #{index} {str(seat)}')


    def store(self,filename : str) -> None:
        """
            Function store the repartition in an excel file
            :param: string that represent files name.
            :return: Nothing.
        """
        repartition_dict = {f'{tabel}': [f'Seat #{index } {str(seat)}' for index,seat in enumerate(tabel.seats,start=1)] 
                            for tabel in self.tables
                            }
        df = pd.DataFrame(repartition_dict.items(), columns = ['tabels','seats'],index = [index for index,val in enumerate(repartition_dict,start=1)])
        pd.DataFrame.to_excel(df,f'repartition_file.xlsx')

    
    

