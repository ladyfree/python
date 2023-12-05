#section_047.py

print('%s, %s'  % ('하나','둘'))
print('%d, %d, %d' % (1, 2, 3))
print()

print('작품번호: %5d, 작품선호도: %6.2f' % (365, 9.228))
print('작품번호: %5d, 작품선호도: %6.2f' % (468, 8.124))
print()

print('체질량지수(BMI)를 계산해 보아요')

weight = int(input('체중을 입력하세요: '))
height = float(input('키를 입력하세요: '))
bmi = weight/(height*height)
comment = 'BMI는 %d/(%.2f * %.2f)이므로 %6.2f이다.'

print(comment % (weight, height, height, bmi))
