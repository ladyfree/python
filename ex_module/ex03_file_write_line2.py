# 파일에 한줄 쓰기 예제2
folder = 'ex_module' # 경로=폴더
file_name = folder + '/' +'sample2.txt' #파일명
with open(file_name, 'w') as fd:
    # 쓰기모드로 파일을 열기기
    fd.write('hello2')
    fd.write('hello2')

    
