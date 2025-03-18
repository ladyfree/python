"""
Author : 정재순
Last Modification : 2024.12.12.
"""
# input파일을 읽어서 여러개의 output파일로 만들기
OUT_DIRECTORY = 'ex_module/output'

# 반복하기
for i in range(1,30+1):

    out_fname = OUT_DIRECTORY + '/' + 'ullim_'+ str(i).zfill(3) +'.txt'

    # out file을 쓰기 모드로 열기
    out_fd = open(out_fname, 'w', encoding='utf-8')
    # out file에 내용 쓰기
    out_fd.write("하늘을 우러러 한점 부끄러움 없기를")

    # out파일 닫기
    out_fd.close()