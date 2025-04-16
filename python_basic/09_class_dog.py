class Dog:
    
    def __init__(self, nm, age):
        self.name = nm
        self.age = age
    
    def bark(self):
        print(f"{self.name}이 멍멍!!!")
        
    def info(self):
        print(f"이름은 {self.name}, 나이는 {self.age} 이다")
        

dog1 = Dog('초코', 3)
dog1.bark()

dog2 = Dog("쫑", 5)
dog2.bark()

print(dog1.name)
dog1.info()
dog2.info()