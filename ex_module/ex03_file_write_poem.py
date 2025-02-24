# 파일에 여러줄 쓰기 예제
folder = 'ex_module' # 경로=폴더
file_name = folder + '/' +'sample_poem.txt' #파일명
with open(file_name, 'w', encoding="utf-8") as fd:
    fd.write("서시\n\n")         # 파일에 내용 쓰기
    fd.write("죽는 날까지 하늘을 우러러\n")         # 파일에 내용 쓰기
    fd.write("한 점 부끄럼이 없기를,\n")         # 파일에 내용 쓰기
    fd.write("잎새에 이는 바람에도\n")         # 파일에 내용 쓰기    
    fd.write("나는 괴로와했다.\n")         # 파일에 내용 쓰기  
    