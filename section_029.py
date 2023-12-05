#section_029.py

colors = ['red', 'orange', 'yellow']
print(colors)

print('red의 위치:', colors.index('red')) # 위치 가져오기
print('orange의 위치:', colors.index('orange'))
print()

colors.append('purple')             # 항목 추가하기1
print(colors)

colors.insert(3, 'green')            # 항목 추가하기2
print(colors)

colors.extend(['black', 'white'])   # 항목 추가하기3
print(colors)

