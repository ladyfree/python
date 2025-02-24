# 파일 줄 단위로 읽기
DIRECTORY = 'ex_module'
file_name = DIRECTORY + '/'+'sample_poem.txt'
n = 1
with open(file_name , "r", encoding="utf-8") as fd:
    for line in fd:  # 파일을 한 줄씩 읽음
        print(n, line.strip())
        n += 1
        #print(line.strip())  # 각 줄의 양끝 공백 제거 후 출력
