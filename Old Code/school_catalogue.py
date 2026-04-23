class School:
    def __init__(self, name, level, numberOfStudents):
        self.name = name
        self.level = level
        self.numberOfStudents = numberOfStudents

    def get_name(self):
        return self.name
    
    def get_level(self):
        return self.level
    
    def get_num_of_students(self):
        return self.numberOfStudents
    
    def set_num_of_students(self, newNumOfStudents):
        self.numberOfStudents = newNumOfStudents
    
    def __repr__(self):
        return f"A {self.level} school named {self.name} with {self.numberOfStudents} students."
    
class PrimarySchool(School):
    def __init__(self, name, numberOfStudents, pickupPolicy):
        super().__init__(name, 'primary', numberOfStudents)
        self.pickupPolicy = pickupPolicy

    def get_pickupPolicy(self):
        return self.pickupPolicy

    def __repr__(self):
        parentRepr = super().__repr__()
        return f"{parentRepr} The pickup policy is {self.pickupPolicy}"

class HighSchool(School):
    def __init__(self, name, numberOfStudents, sportsTeams):
        super().__init__(name, 'high', numberOfStudents)
        self.sportsTeams = sportsTeams

    def get_sports(self):
        return self.sportsTeams
    
    def __repr__(self):
        parentRepr = super().__repr__()
        return f"{parentRepr} The sports teams are: {', '.join(self.sportsTeams)}"

sportsTeams = ['basketball', 'football', 'soccer', 'tennis']

a = School('St. Joseph', 'high', 200)
b = PrimarySchool('St. Leonard', 50, "Pickup Allowed")
c = HighSchool('Morton', 400, sportsTeams)

print(a)
print(a.get_name())
print(a.get_level())
print(a.get_num_of_students())

print(b)
print(b.get_name())
print(b.get_level())
print(b.get_num_of_students())
print(b.get_pickupPolicy())

print(c)
print(c.get_name())
print(c.get_level())
print(c.get_num_of_students())
print(c.get_sports())