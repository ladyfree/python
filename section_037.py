#section_037.py

my_set = {1, 2, 3}
print(my_set)
print(type(my_set))

my_set = {"hello", 1.0, (1,2,3)}
print(my_set)
#my_set = {1, 2, [4, 5]}    # 오류 발생

my_set = {1, 2, 3, 3, 4, 2}
print(my_set)

#print(my_set[0])           # 오류 발생

# 빈 집합 만들 때 주의할 것
my_set = {}
print(type(my_set))
my_set = set()
print(type(my_set))
