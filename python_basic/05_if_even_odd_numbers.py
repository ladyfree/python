number = 'a'
while True:
    if number == 'q':
        break
    
    number = (input("숫자를 입력하세요 :"))
    
    number = int(number)
    if number % 2 == 0:
        print("짝수")
    else:
        print("홀수 ")