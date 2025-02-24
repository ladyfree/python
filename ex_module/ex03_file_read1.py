# 파일에 한줄 읽기기 예제
folder = 'ex_module' # 경로=폴더
file_name = folder + '/' +'sample.txt' #파일명
fd = open(file_name, 'r') # 읽기모드로 파일을 열기
fl = fd.read()
print(fl)
fd.close