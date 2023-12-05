#section_073.py

var = '전역변수'
 
def scope():
    var = '지역변수'
    print(var)
     
scope() # scope() 함수 실행

print()
print(var)
