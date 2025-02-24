# 파일에 한줄 읽기 예제2
folder = 'ex_module' # 경로=폴더
file_name = folder + '/' +'sample.txt' #파일명
with open(file_name, 'r') as fd: # 읽기모드로 파일을 열기
    fl = fd.read()
    print(fl)
