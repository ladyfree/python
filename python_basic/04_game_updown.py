# 1~10임의의 숫자 맞추기
import random

com_num = random.randrange(1,11)
user_num = 0 
print(com_num)

# c = 0
while com_num != user_num:
    user_num = int(input("1~10사이의 숫자를 입력하세요 : "))
    