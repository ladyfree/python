# 문자열 슬라이싱하기(정방향,역방향)

str1 = 'NATURE'
#       012345 순방향인덱스
print("="*20)
print("정방향 슬라이싱")
print("="*20)

print(str1[0:1+1]) # NA
print(str1[0:5]) # NATUR
print(str1[2:5]) # TUR
print(str1[:]) # NATURE (전체 다나오기)
print(str1[:3]) # NAT  # 시작의 default는 0이다.
print(str1[2:]) # TURE # 끝의 default는 마지막(-1)이다.
print(str1[:6]) # [:6]인덱스가 5까지 있는데 이렇게 표기해도 될까요?
print(str1[:7]) # [:7]인덱스가 5까지 있는데 이렇게 표기해도 될까요?
