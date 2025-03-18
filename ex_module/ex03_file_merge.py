# in directory에 있는 텍스트 파일을 읽어서 txt파일로 저장하기
import os

IN_DIRECTORY = 'ex_module/output' 
# 폴더의 내용물을 열람해 목록을 생성합니다.
input_files = os.listdir(IN_DIRECTORY)
#print(input_files)
for fn in input_files:
    # print(fn)
    #파일명 만들기
    in_fname = IN_DIRECTORY + '/' + fn
    # 파일열기
    in_fd = open(in_fname, 'r', encoding='utf-8')
    txt = in_fd.read()
    print(txt)
    in_fd.close()