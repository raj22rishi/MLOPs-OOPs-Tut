## getter and setter
class Employee:
    
    def __init__(self):
        self.__name = 'Rishi'
        self.age = 18
    
    def get_name(self):
        return self.__name
    
    def set_name(self, str):
        self.__name = str
        
        
    
obj = Employee()

print(obj.get_name())
obj.set_name("Ananya")
print(obj.get_name())