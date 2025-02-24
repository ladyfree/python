# 파일 줄 단위로 읽기
DIRECTORY = 'ex_module'
file_name = DIRECTORY + '/'+'sample_poem.txt'
with open(file_name , "r", encoding="utf-8") as fd:
    fl = fd.read()
    print(fl)
