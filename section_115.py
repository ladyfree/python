#section_115.py

class Robot:
    '''다양한 로봇을 만드는 클래스'''
    population = 0
    maker = 'KAIST'
    
    def __init__(self, name, build_year):
        self.isWalking = True
        self.name = name
        self.build_year = build_year
        self.xpos = 0
        self.ypos = 0
        Robot.population += 1
        
hubo1 = Robot('shane', 2016)
hubo2 = Robot('albert', 2018)
hubo3 = Robot('sol', 2018)
print(Robot.maker, Robot.population, hubo1.population)

Robot.maker = 'POSTECH'
print(hubo2.maker, hubo2.population)

