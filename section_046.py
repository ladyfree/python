#section_046.py

# 숫자와 문자열 사이의 형변환
iNumber = int('7')
print(iNumber, type(iNumber))

fNumber = float(iNumber)
print(fNumber, type(fNumber))

sNumber = str(iNumber)
print(sNumber, type(sNumber))
#print(sNumber + 1)     #오류 발생

print('-' * 20)
# 리스트와 튜플 사이의 형변환
myList = [1, 2, 3]
print(myList, type(myList))

myTuple = tuple(myList)
print(myTuple, type(myTuple))
 
