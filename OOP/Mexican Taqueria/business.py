class Business:
    def __init__(self, name, franchises):
        self.name = name
        self.franchises = franchises
    
    def __str__(self):
        return f"Business Name: {self.name} | Locations: {self.franchises}"
    
    def find_store(self, address):
        for store in self.franchises:
            if store.address == address:
                return store
        return "Store not found."