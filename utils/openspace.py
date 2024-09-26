from typing import Self
from .table import Table 


class Openspace:
    def __init__(self,number_of_tables: int = 6,tables : list = None) -> Self.object:
        """
            Constructor of classs Openspace.
            :param number_of_tabels: An int that perform number of tabels available.
            :param tables: An list that list of instances Tabel.
            :return: instance of class Openspace 
        """
        self.number_of_tabels = number_of_tables
        self.tables = tables

    def __str__(self) -> str:
        """
            Function that print reade
            :param: None
            :return: String
        
        """
        pass

    def organize(self,names : list) -> None:
        """
            Function that randomly assing peopel to Seat objects in the different Table objects .
            :param names: List of employees present in the office.
            :return: Nothing
        """
        pass


    def __repr__(self) -> None:
        """
            Function that display the different Tables and there occupants in a nice and readable way.
            :param: None.
            :return: Nothing.
        """
        pass


    def store(self,filename : str) -> None:
        """
            Function that display the different Tables and there occupants in a nice and readable way.
            :param: None.
            :return: Nothing.
        """

        pass


