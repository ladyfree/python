#section_035.py

my_tuple = (1, 2, 3)
your_tuple = (4, 5, 6)

# 튜플 연산
our_tuple = my_tuple + your_tuple
print(our_tuple)

multiply_tuple = my_tuple * 3
print(multiply_tuple)

#del our_tuple
#print(our_tuple)

# 튜플 멤버십 테스트
print(1 in my_tuple)
print(4 in my_tuple)
print(3 not in my_tuple)

# 튜플 관련 메서드
print(multiply_tuple.count(1))
print(multiply_tuple.index(2))
