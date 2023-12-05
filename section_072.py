#section_072.py

global_var = '전역변수'
 
def scope():
    local_var = '지역변수'
    print(global_var)
    print(local_var)
     
scope() # scope() 함수 실행

print()
print(global_var)
print(local_var)




