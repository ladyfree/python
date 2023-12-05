#section_118.py

class Robot:
    '''다양한 로봇을 만드는 클래스'''
    def __init__(self, name, pos):
        self.name = name
        self.pos = pos
        
    def move(self):
        print('로봇이 이동한다.')

    def charge(self):
        print('로봇이 충전한다.')
        
class CleanRobot(Robot):
    def __init__(self, name, pos, filtertype):
        super().__init__(name, pos)
        self.filtertype = filtertype
        
    def broom(self):
        print('청소로봇이 먼지를 쓸어 담는다.')

    def __str__(self):
        word = '{}를 장착한 {}, {}에서 시작'\
               .format(self.filtertype, self.name, self.pos)
        return word

clean = CleanRobot('깔끔이로봇', (20, 45), '먼지필터')
print(clean) 
clean.move()
clean.broom()
