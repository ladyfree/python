#section_032.py

myTuple = ()
myTuple = (1, 2, 3)
myTuple = (1, "python", 3.14)
myTuple = ("문자열도 넣고", (1,2,3), [4,5,6])

myTuple = 1, 2, "number"  
print(myTuple)
a, b, c = myTuple
print(a, b, c)
print()

# 튜플 선언시 한 가지 유의점
myTuple = ("hello")
print(type(myTuple))  # myTuple는 문자열 변수
myTuple = ("hello", )
print(type(myTuple))  # myTuple는 튜플 변수

myTuple = (1, 2, 3)
# myTuple[0] = 10   # 오류 발생
