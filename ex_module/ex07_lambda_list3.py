# 할인율 계산 전략들
discount_strategies = [
    lambda price: price * 0.95,   # 5% 할인
    lambda price: price - 1000,   # 고정 1,000원 할인
    lambda price: price * 0.90 if price > 50000 else price
]

def apply_discount(price, strategy_idx):
    return discount_strategies[strategy_idx](price)

print(apply_discount(60000, 0))  # 57000 (5% 할인)
print(apply_discount(20000, 1))  # 19000 (고정 할인)
print(apply_discount(60000, 2))  # 54000 (조건부 10% 할인)
