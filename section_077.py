#section_077.py

num0 = 0
num1 = 1
empty_list = []
full_list = [1, 2, 3]
empty_str = ""
full_str = "파이썬"

print(bool(num0))
print(bool(empty_list))
print(bool(empty_str))
print(bool(num1))
print(bool(full_list))
print(bool(full_str))

color = input('좋아하는 색을 입력하세요: ')
if not bool(color):
    print('색을 반드시 입력해야 합니다.')
else:
    print(color + '색을 좋아하는 군요.')
