#section_116.py

class Robot:
    '''다양한 로봇을 만드는 클래스'''
    def __init__(self, name, build_year):
        self.name = name
        self.__build_year = build_year
        self.xpos = 0
        self.ypos = 0

    def getYear(self):
        return self.__build_year
        
hubo = Robot('shane', 2016)

hubo.name = 'albert'
print(hubo.name)
#print(hubo.__build_year)
print(hubo.getYear())

print()
print(dir(hubo))
