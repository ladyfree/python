#section_117.py

class Robot:
    '''다양한 로봇을 만드는 클래스'''
    def speak(self):
        print('로봇이 말한다.')
        
    def move(self):
        print('로봇이 이동한다.')

    def charge(self):
        print('로봇이 충전한다.')
        
class CleanRobot(Robot):
    def broom(self):
        print('청소로봇이 먼지를 쓸어 담는다.')

robot = Robot()
robot.move()

clean = CleanRobot()
clean.broom()
clean.move()
