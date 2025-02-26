#문자열 관련 메서드

str1 = "Hello, My little baby"
cnt = str1.count
print(len(str1))
print(str1.count('My'))
print(str1.upper()) # 대문자 반환
print(str1.lower()) # 소문자 반환
print(str1.title()) # 단어의 첫글자는 대문자로 반환
print()
print(str1.count('b')) # 문자열내 'b'문자의 갯수 반환
print(str1.startswith('h')) # 문자열의 시작문자가 'h'인지 여부 반환
print(str1.endswith('y')) # 문자열의 끝문자가 'y'인지 여부 반환
print()
print(str1.split()) # 문자열을 공백을 기준으로 분리해서 리스트로 반환
print(str1.split(',')) # 문자열을 ','을 기준으로 분리해서 리스트로 반환
print(str1.zfill(30)) # 문자열을 30으로 기준으로 남는 자리만큼 zero로 채우
print(str1.replace('little','big')) # 문자열중 'e'문자을 'a'로 바꾸기