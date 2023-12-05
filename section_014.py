#section_014.py

mass = 100
height = 1.7
g = 9.8065

print('질량은', mass)
print('높이는', height)
print('중력상수는', g)
print()

# 여러 변수 출력하기
print(mass, height, mass * height * g)
print()

# 구분자 넣고 출력하기
print(mass, height, mass * height * g, sep=",")
print(mass, height, mass * height * g, sep=" 에헴 ")
