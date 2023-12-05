#section_040.py

A = {1, 2, 3, 4, 5, 6}
B = {1, 2, 3, 7, 8, 9}

# 합집합
print(A | B, '-> A | B')
print(A.union(B), '-> A.union(B)')
print(B.union(A), '-> B.union(A)')
print(A, '-> A')
print()

# 교집합
print(A & B, '-> A & B')
print(A.intersection(B), '-> A.intersection(B)')
print()

# 차집합
print(A - B, '-> A - B')
print(A.difference(B), '-> A.difference(B)')
print()

# 대칭차집합
print(A ^ B, '-> A ^ B')
print(A.symmetric_difference(B), '-> A.symmetric_difference(B)')
print()

# 부분집합
print({4, 5, 6} <= A)
print({4, 5, 6}.issubset(A))
print({1, 2, 3, 4, 5, 6} >= A)
print({1, 2, 3, 4, 5, 6}.issuperset(A))
