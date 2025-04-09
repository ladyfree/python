# 함수에 매개변수를 전달할 수 있다.
def say_hello(p): # p:문자열
    print(p + "안녕하세요")

say_hello("jim")
say_hello("jenny")

# 함수를 정의하는 기본 구조
def say_hello2(p): # p : 반복 횟수
    for _ in range(p):
        print( "안녕하세요2222")
        
say_hello2(4)

# 함수를 정의하는 기본 구조
def say_hello3(p, n): # p : 사람이름, n : 반복횟수
        print( f"{n}님, 안녕하세요")
        
say_hello3("young", 3)
