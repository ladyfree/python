import random

lotto = []
while True:
    num = random.randrange(1,46)
    if num not in lotto:
        lotto.append(num)
        
    if len(lotto) >= 6:
        break

print(f"로또번호 {lotto}")
    