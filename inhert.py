

class Animal:
    
    def __init__(self):
        self.name = "Jojo"
        
    def speak(self):
        print(f'{self.name} makes a sound')
        

class Dog(Animal):
    
    def __init__(self,breed):
        super().__init__()
        self.breed = breed
    def speak1(self):
        # super().speak()
        print(f'{self.name} barks and is of {self.breed} breed.')

dog = Dog("Shihtzu")
dog.speak()  