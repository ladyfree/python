
# 딕셔너리 변수 선언
student = {'이름':'홍길동', '나이':20, '학과':'컴퓨터', '1':'순위', '나이':30, '나이':40}

print(student)

# 값 변경
student['나이'] = 30
print(student)

# 값 추가
student['주소'] = '안산시'
print(student)

# 값 삭제
del student['1']
print(student)

# 값 중복 추가
student['나이'] = 21
print(student)