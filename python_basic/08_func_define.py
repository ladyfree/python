
def make_kimbab():
        
    print("김 깔기")
    print("밥 올리기")
    print("재료 넣기")
    print("말기")
print("먹자")

for _ in range(5): 
    make_kimbab()

# 함수를 정의하는 기본 구조
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
