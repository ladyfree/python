class   Wizard:
    # 초기 생성
    def  __init__(self, nm, lvl, hp, ap):
        self.name = nm
        self.level = lvl
        self.hp = hp
        self.attack_power = ap
        
    def attack(self, y):
        print(f"{self.name}가 {y.name}를 공격합니다.")
        y.hp -= self.attack_power
        print(f"{y.name}의 체력이 {y.hp}이 되었습니다.")
        
    def heal(self, amount):
        self.hp += amount
        print(f"{self.name}의 체력이 {self.hp}로 회복되었습니다.")
        
hero = Wizard("원더우먼", 10, 100, 7)
monster = Wizard("윤", 10, 5, 2)

hero.attack(monster)
hero.heal(1)
        
