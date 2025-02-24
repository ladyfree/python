# 파일에 한줄 쓰기 예제
folder = 'ex_module' # 경로=폴더
file_name = folder + '/' +'sample.txt' #파일명
fd = open(file_name, 'w') # 쓰기모드로 파일을 열기기
fd.write('hello2')
fd.close