
# 딕셔너리 변수 선언
student = {'이름':'홍길동', '나이':20, '학과':'컴퓨터', '1':'순위', '나이':30, '나이':40}

# key값만 반복 호출
for i in student:
    print(i)
    print(student[i]) # key를 사용하여 value를 출력
    
# 모든 키(key)와 value를 반복 가져오기
for i in student.items():
    print(i[0]) # key값만 출력할 수 있음
    print(i[1]) # value값만 출력할 수 있음
    
# 모든 키(key)와 value를 반복 가져오기
for i, j in student.items():
    print(i)
    print(j)

for i in student.items():
    for j in i:
        print(j)
        
print('-'*20)

for i in student.keys(): # 딕셔너리의 key값만 반환하는 메소드
    print(i)
    
# value만 반환하는 메소드
for i in student.values():
    print(i)

if '홍길동' in student.items():
    print('yes')