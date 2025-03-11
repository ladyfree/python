# 1개의 파일을 읽어서 여러개로 저장하기.
# input파일명 
in_directory = 'ex_module'
in_fname = in_directory + '/'+ 'sample_poem.txt'
out_directory = 'ex_module/output'
#out_fname = out_directory + '/'+ 'poem.txt'

# in file로 파일 열기
with open(in_fname, 'r', encoding='utf-8') as in_fd:
    # in file파일을 읽기
    txt = in_fd.read()
    # 읽은 내용 써보기

for i in range(1,20+1):
    # 파일 쓰기모드로 열기
    #out_fname = out_fname + str(i)
    out_fd = open(out_directory + '/'+ 'poem_'+ str(i).zfill(3)+'.txt', 'w', encoding='utf-8' )
    # 파일 쓰기
    out_fd.write(txt)
    # 파일 닫기
    out_fd.close()

    