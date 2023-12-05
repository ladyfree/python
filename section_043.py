#section_043.py

my_idol = {"name": "쯔위", "age": 18, "job": "singer"}
print(my_idol['name'])       # 값 가져오기
print(my_idol.get('age'))
print(my_idol.get('birth'))
# print(my_idol['birth'])    # 오류 발생
print()

my_idol['name'] = '수지'           # 항목 수정하기
print(my_idol)
print()

my_idol['birth'] = '1994-10-10'    # 항목 추가하기
my_idol['manager'] = 'JYP'
print(my_idol)
