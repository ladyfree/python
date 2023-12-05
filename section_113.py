#section_113.py

class Robot:
    '''다양한 로봇을 만드는 클래스'''
    def __init__(self, name, build_year):
        self.maker = 'KAIST'
        self.isWalking = True
        self.name = name
        self.build_year = build_year
        self.xpos = 0
        self.ypos = 0

    def move(self):
        if self.isWalking:
            self.xpos += 1
            self.ypos += 1

    def curPosition(self):
        print('현재 좌표: ({}, {})'.format(self.xpos, self.ypos))

hubo = Robot('shane', 2016)
hubo.move()
hubo.move()
hubo.move()
hubo.curPosition()
