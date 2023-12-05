#section_074.py

var = '전역변수'
 
def scope():
    global var
    var = 'global 명령어의 역할'
    print('함수 안 var: ', var)
     
scope() # scope() 함수 실행

print()
print('함수 밖 var: ', var)
