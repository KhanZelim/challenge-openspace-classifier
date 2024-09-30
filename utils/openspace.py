from typing import Self
from .table import Table 
from .file_utils import *
import random
import pandas as pd




class Openspace:
    """
    class Openspace create object of roomspace for users team
    :property:  number_of_tabels An int that perform number of tables available.
                tabel capacity: An int that performe number of seats per one table available
                tables list of Tabel objects
                names team members with no seats
                capacity amount of seats in room, max=34
                _flag flag that is showing if there is people without seats left in the room 
    :methods:   __init__
                __str__
                organize
                dysplay
                store
                has_space
                add_table
                add_seat_to_all_tables
                add_both
                assing_occupants
                avoiding_loneliness
                is_enough_space
                implemnt_decision
                fix_size_loop
    
    """
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
        self.capacity+=self.number_of_tabels
        for table in self.tables:
            table.add_seat()
            

    def add_both(self) -> None:
        """
            Function is adding one tabel, and one seat to each tabel in Openspace
            :return:None

        """
        self.add_table()
        self.add_seat_to_all_tables()


    def assing_occupants(self,name) -> None:
        """
            Function that assing occupant to the random choised tabel
            :param: string, name of occupant
            :return: None.
        """
        min_cap = min([table.capacity for table in self.tables])
        bool_list = [tabel.capacity==min_cap for tabel in self.tables]
        while True:
            choised_tabel = random.choice(self.tables)
            
            if choised_tabel.has_free_spot():
                if choised_tabel.capacity > min_cap:
                    choised_tabel.assign_seat(name)
                    break
                elif bool_list.count(True) == self.number_of_tabels:

                    choised_tabel.assign_seat(name)
                    break
                else:
                    continue
                    
            else:
                continue
    

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
            elif not self._flag:
                try:
                    tabel.assign_seat(self.names.pop())
                    self.capacity-=1
                except:
                    continue
        else:
            while len(self.names) != 0 and not self._flag:
                for tabel in self.tables:
                    if tabel.capacity == self.table_capacity:
                        [tabel.assign_seat(self.names.pop()) for i in range(len(self.names)) ]
                        self.capacity-=1

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
                self.names = names[self.capacity:]
            case 'B':
                self.add_both()

    def fix_size_loop(self, names:list)->tuple:
                """
                    Function that iniciate interaction with user, 
                        about how to fix openspace capasity problem.
                    :param: names list is containing names of сolleagues in string.
                    :return: tuple (int,int) = (self capacity of the Openspace, Quantety of colleagues).
                """
                flag = to_many_quest(names,self.number_of_tabels,self.table_capacity,self.capacity)
                self.implemnt_decision(flag,names)
                if_capasity = (self.capacity >= len(names)) 
                if if_capasity:
                    for name in names:
                        self.assing_occupants(name)
                    self.avoiding_loneliness()
                    return (self.capacity,len(names))
                elif self._flag:
                    for name in names[:self.capacity]:
                        self.assing_occupants(name)
                    self.avoiding_loneliness()
                    return (self.capacity,len(names),self.names)
                else:
                    self.fix_size_loop(names)                    

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
        elif self._flag:
            for name in names[:self.capacity]:
                self.assing_occupants(name)
            self.avoiding_loneliness()
        else:
            self.fix_size_loop(names)
            if not self._flag:
                print("There is still not enough space")
            else:
                return self.names
            
    def adding_latecomers(self) -> None:
        """
        Function that adds people who are not in the file to the tables.
        :return: None
        """
        def internal_seat_assign()-> None:
            'Internal function for seat assignment'
            seat_assigned = False
            for tabel in self.tables:
                if seat_assigned:
                     break
                if tabel.has_free_spot():
                    for seat in tabel.seats:
                        if seat.free:
                            seat.set_occupant(name_input)
                            seat_assigned = True
                            break
            
        while True:
            adding_answ = input('Do you want to add somebody? Y/N')
            match adding_answ:
                case 'Y':
                    while True:
                        name_input = input('Write the names. if all names were added write E')
                        match name_input:
                            case 'E':
                                break
                            case _:
                                if re.fullmatch('^[A-Z]{1}[a-z]*$',name_input):
                                    if self._flag:
                                        print(1)
                                        self.names.append(name_input)
                                    elif self.has_space():
                                       internal_seat_assign()
                                    else:    
                                        print(3)
                                        names = [name_input]
                                        flag = to_many_quest(names,self.number_of_tabels,self.table_capacity,self.capacity)
                                        self.implemnt_decision(flag,names)
                                        internal_seat_assign()
                                    
                                else:
                                    print("It isn't name or E. Please try again ")
                    break
                case 'N':
                    break
                case _:
                    print('Incorrect answer. Try again.')
                
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
        self.adding_latecomers()
        repartition_dict = {f'Tabel #{index_t}': [f'Seat #{index } {str(seat)}' for index,seat in enumerate(tabel.seats,start=1)] 
                            for index_t,tabel in enumerate(self.tables,start=1)
                            }
        if self._flag:
            repartition_dict['Peopel without seats:'] = self.names
        df = pd.DataFrame(repartition_dict.items(), columns = ['tabels','seats'],index = [index for index,val in enumerate(repartition_dict,start=1)])
        while True: 
            answ = input('If you wanna save file in csv press "C", if in xlsx press X. C/X')
            match answ:
                case 'C':
                    df.to_csv(f'{filename}.csv')
                    break
                case 'X':
                    df.to_excel(f'{filename}.xlsx')
                    break
                case _:
                    print('incorrect leter, try again')
                


    

    
    

