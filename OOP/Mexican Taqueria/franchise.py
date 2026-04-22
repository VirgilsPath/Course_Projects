class Franchise:
    def __init__(self, address, menu):
        self.address = address
        self.menu = menu
    
    def __str__(self):
        return f"Our Taqueria is located at {self.address}."

    def __repr__(self):
        return self.address
    
    def is_it_open(self, current_time):
        if self.menu.start_time <= current_time < self.menu.end_time:
            return True
        else:
            return False