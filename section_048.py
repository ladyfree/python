#section_048.py

print('{0}, {1}'.format('하나','둘'))
print('{0}, {1}, {2}'.format(1, 2, [3,4,5]))
print('칸이 비어도 {}, {}, {}'.format('하나', '둘', '셋'))  
print()

print('{2}, {1}, {0}'.format('a', 'b', 'c'))
print('{0}{1}{0}'.format('오렌지', '를 먹은 지 얼마나 '))   
print()

print('체질량지수(BMI)를 계산해 보아요')

weight = int(input('체중을 입력하세요: '))
height = float(input('키를 입력하세요: '))
bmi = weight/(height*height)
comment = 'BMI는 {0}/({1}*{1})이므로 {2:6.2f}이다.'

print(comment.format(weight, height, bmi))
