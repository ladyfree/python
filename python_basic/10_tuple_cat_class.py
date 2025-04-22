# 클래스
class Cat:
    # 클래스 선언할때 초기값 선언
    def __init__(self, mem):
        self.name = mem[0]
        self.age = mem[1]
        self.sex = mem[2]
        
    def introduce(self):
        print(f"고양이 이름은 {self.name}이고, 나이는 {self.age}이고, {self.sex}야")
        
    def eat(self, food):
        print(f"{self.name}가 {food}을 먹는다")
    
    def eat2(self, food):
        print(f"{self.name}가 {food[0]}을 먹는다")
        
cat1_info = ("냥이", 3, "암컷")
cat2_info = ("나비", 2)
cat3_info = ("콩이", 5, "암컷")

cat1 = Cat(("냥이", 3, "암컷"))
cat1.introduce()
cat1.eat2("생선")

cat2 = Cat(cat2_info)
cat2.eat("참치")