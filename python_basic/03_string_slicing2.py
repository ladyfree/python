# 문자열 슬라이싱하기(역방향)

str1 = 'NATURE'
#       654321 역방향인덱스
print("="*20)
print("역방향 슬라이싱")
print("="*20)

print(str1[-5:-2]) # ATU
print(str1[-4:-2]) # TU
print(str1[-6:]) # NATURE
print(str1[:-3]) # NAT
print(str1[:-1]) # NATUR
print(str1[1:-2]) # ATU (시작은 정방향, 끝은 역방향)
print(str1[-4:4]) # TU (시작은 역방향, 끝은 정방향)