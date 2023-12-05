#section_111.py

class Robot:
    '''다양한 로봇을 만드는 클래스'''
    def __init__(self):
        self.name = 'pybot'
        self.weight = '45kg'
        
hubo1 = Robot()
hubo2 = Robot()
print(hubo1.name, hubo1.weight)
print(hubo2.name, hubo2.weight)

print()
hubo1.name = 'minibot'
hubo2.weight = '60kg'
print(hubo1.name, hubo1.weight)
print(hubo2.name, hubo2.weight)
