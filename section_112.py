#section_112.py

class Robot:
    '''다양한 로봇을 만드는 클래스'''
    def __init__(self, name, build_year):
        self.maker = 'KAIST'
        self.isWalking = True
        self.name = name
        self.build_year = build_year
        
hubo1 = Robot('shane', 2016)
print(hubo1.maker, hubo1.isWalking, hubo1.name, hubo1.build_year)

hubo2 = Robot('albert', 2018)
print(hubo2.maker, hubo2.isWalking, hubo2.name, hubo2.build_year)
