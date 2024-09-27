class Seat:
    """Class representing one seat"""

    def __init__(self):
        """Constructor of class Seat"""
        self.free = True
        self.occupant = ""

    def set_occupant(self, name: str) -> None:
        """
        Function that will set the occupant to the given name (in param)
        
        :param name: str representing the occupant's name
        """
        self.occupant = name
        self.free = False

    def remove_occupant(self) -> None:
        """Function that will set the occupant to a blank string and sets the seat free"""
        self.occupant = ""
        self.free = True

    def __str__(self) -> str:
        """
        A string representation of the seat's status
        
        :return: str representing the seat's occupancy and/or occupant
        """
        if self.free:
            return f"is unoccupied"
        else:
            return f"is occupied by {self.occupant}"

class Table:
    """Class representing one table"""

    def __init__(self, capacity: int):
        """
        Constructor of class Table
        
        :param capacity: int representing the capacity of the table
        """
        self.capacity = capacity
        self.seats = [Seat() for _ in range(capacity)]

    def has_free_spot(self)  -> bool:
        """
        Function that will check if there are any free spots
        
        :return: bool depending on the capacity
        """
        if self.capacity == 0:
            return False
        else:
            return True
        
    def add_seat(self) -> None:
        """Function that adds one seat to the table nad increases capacity by one"""
        self.capacity += 1
        self.seats.append(Seat())

    def assign_seat(self, name: str)  -> None:
        """Function that will assign an occupant to an empty seat and decrease capacity by one"""
        for seat in self.seats:
            if seat.free == True:
                seat.set_occupant(name)
                self.capacity -= 1
                break

    def left_capacity(self)  -> int:
        """
        Function that returns the capacity left
        
        :return: int representing capacity
        """
        return self.capacity

    def __str__(self)  -> str:
        """
        A string representation of the table's capacity
        
        :return: str representing the table's capacity
        """
        return f"Capacity: {self.capacity}"
