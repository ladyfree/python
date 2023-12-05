#section_033.py

# 인덱싱
myTuple = ('a', 'b', 'c')
print(myTuple[0])
#print(myTuple[3])     # 오류 발생
#print(myTuple[2.0])   # 오류 발생
print()

myTuple = ("tuple", (1, 2, 3), [4, 5, 6])
print(myTuple[0])
print(myTuple[0][1])
print(myTuple[2][0])
print(myTuple[-1])
print(myTuple[-1][0])
print()

# 슬라이싱
myTuple = ('p', 'y', 't', 'h', 'o', 'n')
print(myTuple[1:4])
print(myTuple[ :-2])
print(myTuple[ : ])
