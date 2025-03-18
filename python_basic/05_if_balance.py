balance = 5000 #잔액
withdraw = 3000 #청구금액

if balance >= withdraw :
    balance -= withdraw
    print(f"{withdraw}를 지급합니다.")
    print(f"잔액은 {balance}입니다")
else:
    print("잔액 부족입니다.")
    print(f"잔액은 {balance}입니다")