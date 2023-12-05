#section_119.py

class Robot:
    '''다양한 로봇을 만드는 클래스'''      
    def move(self):
        print('로봇이 이동한다.')

    def charge(self):
        print('로봇이 충전한다.')
        
class CleanRobot(Robot):
    def move(self):
        print('청소 로봇이 이동한다.')

    def charge(self):
        print('청소 로봇이 충전한다.')

robot = Robot()
robot.move()
robot.charge()

clean = CleanRobot()
clean.move()
clean.charge()
