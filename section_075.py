#section_075.py

var = '전역변수'
 
def scope():
    var = 'scope() 지역변수'
    print(var, '\t[ scope() 함수에서 출력 ]')

    if True:
        print(var, '\t[ if문에서 출력 ]')

    for i in range(3):
        var = 'for 지역변수'
        print(var, '\t[ for문에서 출력 ]')   
 
scope()     # scope() 함수 실행

print(var, '\t\t[ scope() 함수 밖에서 출력 ]')
