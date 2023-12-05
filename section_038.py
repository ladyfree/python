#section_038.py

s_nature = {'sky', 'sea'}
print(s_nature)
print()

# 항목 추가하기
s_nature.add('earth')
print(s_nature)
s_nature.update({1, 2}, [2, 3])
print(s_nature)
print()

# 항목 가져오기
print(s_nature.pop())
print(s_nature)
print(s_nature.pop())
