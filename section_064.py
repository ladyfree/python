#section_064.py

def abs(number):
    if number < 0:
        number = -number
    return number

print('-3의 절대값 구하기:', abs(-3))
print('10의 절대값 구하기:', abs(10))
print()
temp = abs(-9)/3 * abs(20) + 3 + abs(-19) 
print('계산 결과:', temp)

