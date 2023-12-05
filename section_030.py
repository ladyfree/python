#section_030.py

colors = ['red', 'orange', 'yellow', 'green', 'yellow']
print(colors)

colors.sort()                       # 항목 정렬하기
print(colors)

colors.reverse()                    # 역순 정렬하기
print(colors)
print()

print(colors.pop())                 # 항목 가져오기
print(colors)

colors.remove('red')             # 항목 삭제하기
print(colors)

print(colors.count('yellow'))       # 항목 개수 세기
