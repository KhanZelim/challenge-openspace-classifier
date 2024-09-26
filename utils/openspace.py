from typing import Self
from table import Table 
import random

class Openspace:
    def __init__(self,number_of_tables: int = 6) -> Self:
        """
            Constructor of classs Openspace.
            :param number_of_tabels: An int that perform number of tabels available.
            
            :return: instance of class Openspace 
        """
        self.number_of_tabels = number_of_tables
        self.tables = [Table(4) for i  in range(number_of_tables)]
        self.names = []
        

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
        

    def organize(self,names : list) -> None:
        """
            Function that randomly assing peopel to Seat objects in the different Table objects .
            :param names: List of employees present in the office.
            :return: Nothing
        """
        self.names += names
        for name in names:
            cap_list =[tabel.capacity for tabel in self.tables]
    
            min_cap = min(cap_list)
            print(min_cap)
            counter = 0
            while counter < len(self.tables):
                counter+=1
                choised_tabel = random.choice(self.tables)
                print(choised_tabel)
                if choised_tabel.capacity == min_cap or not choised_tabel.has_free_spot():
                    continue
                else:
                    choised_tabel.assign_seat(name)
                    break
            else:
                choised_tabel.assign_seat(name)
        self.names = []
        for tabel in self.tables:
            if tabel.capacity == 3:
                for seat in tabel.seats:
                    if not seat.free:
                        self.names.append(seat.occupant)
                        print(self.names)
                        seat.remove_occupant()
            else:
                try:
                    tabel.assign_seat(self.names.pop())
                except:
                    continue
        else:
            while len(self.names) != 0:
                for tabel in self.tables:
                    if tabel.capacity == 4:
                        [tabel.assign_seat(self.names.pop()) for i in range(len(self.names)) ]
            
                    
                
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
            Function 
            :param: None.
            :return: Nothing.
        """

        pass





