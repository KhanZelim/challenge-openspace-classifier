class Seat:
    """Class representing one seat"""

    def __init__(self):
        """Consructor of our class"""
        self.free = True
        self.occupant = ""

    def set_occupant(self, name):
        """
        Function that will set the occupant to the given name (in param)
        
        :param name: A string
        """
        self.occupant = name
        self.free = False

    def remove_occupant(self):
        """Function that will set the occupant to a blank string"""
        self.occupant = ""
        self.free = True

    def __str__(self):
        """"""
        if self.free:
            return f"is unoccupied"
        else:
            return f"is occupied by {self.occupant}"

class Table:
    """Class representing one table"""

    def __init__(self, capacity):
        """
        Constructor of our class
        
        :param capacity: An int representing the capacity
        """
        self.capacity = capacity
        self.seats = [Seat() for i in range(capacity)]

    def has_free_spot(self):
        """Function that will check if there are any free spots"""
        if self.capacity == 0:
            return False
        else:
            return True
        
    def add_seat(self) -> None:
        """
            Function is adding one seat  Table
            :return:None
        """
        self.capacity+=1
        self.seats.append(Seat())

    def assign_seat(self, name):
        """Function that will assign an occupant to an empty seat"""
        for seat in self.seats:
            if seat.free == True:
                seat.set_occupant(name)
                self.capacity -= 1
                break

    def left_capacity(self):
        """Function that checks the capacity left"""
        return self.capacity

    def __str__(self):
        """"""
        return f"Capacity: {self.capacity}"