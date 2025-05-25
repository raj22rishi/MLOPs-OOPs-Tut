## getter and setter
class Employee:
    __user_id = 1
    
    def __init__(self):
        self.id = Employee.__user_id
        Employee.__user_id += 1
        self.__name = 'Rishi'
        self.age = 18
    
    @staticmethod
    def get_id():
        return Employee.__user_id
    
    @staticmethod
    def set_id(val):
        Employee.__user_id = val
    
    
    def get_name(self):
        return self.__name
    
    def set_name(self, str):
        self.__name = str
        
        
    
obj1 = Employee()
print(obj1.id)

Employee.set_id(10)

obj2 = Employee()
print(obj2.id)


obj3 = Employee()
print(obj3.id)



