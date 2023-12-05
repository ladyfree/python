#section_044.py

my_idol = {'job': 'singer', 'age': 18, 'name': '수지', 'birth': '1994-10-10'}
print(my_idol)
print()

print(my_idol.pop('birth')) # 항목 가져오면서 삭제하기
print(my_idol)
print()

del my_idol['age']          # 항목 삭제하기
print(my_idol)
print()

print(my_idol.popitem())    # 임의의 항목 가져오면서 삭제하기
print(my_idol)
print()

my_idol.clear()             # 사전 비우기
print(my_idol)

del my_idol
#print(my_idol)
