class Seat:
    
    def __init__(self):
        self.free = True
        self.occupant = ""

    def set_occupant(self, name):
        self.occupant = name
        self.free = False

    def remove_occupant(self):
        self.occupant = ""
        self.free = True

    def __str__(self):
        if self.free:
            return f"is unoccupied"
        else:
            return f"is occupied by {self.occupant}"

class Table:

    def __init__(self, capacity):
        self.capacity = capacity
        self.seats = [Seat() for i in range(capacity)]

    def has_free_spot(self):
        if self.capacity == 0:
            return False
        else:
            return True

    def assign_seat(self, name):
        for seat in self.seats:
            if seat.free == True:
                seat.set_occupant(name)
                self.capacity -= 1
                break

    def left_capacity(self):
        return self.capacity

    def __str__(self):
        return f"Capacity: {self.capacity}"