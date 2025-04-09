# 길이를 알아내는 함수 만들기
def my_len(sequence):
    cnt = 0
    for _ in sequence:
        cnt += 1
    return cnt
        
len1 = my_len("friend")
print(len1)
print(my_len([1,2,3,4,5,6,7]))

print(my_len({1:100, 2:200, 3:300}))