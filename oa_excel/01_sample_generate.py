"""
Author : pitta
Last Modification : 2024.12.12.
개인정보( : )이름, 생년월일, e-mail, 전화번호, 성별)을 가상으로 생성함함
"""
import time
import random
import os
import shutil

MAX_NUM = 10
OUT_PATH = "personal_info/"

# 이메일 생성에 사용할 샘플 글자들을 정의합니다.
alphabet_samples = "abcdefghizklmnopqrstuvwxyz1234567890"

def random_string(length):
    result = ""
    for i in range(length):
        # alphabet_samples에서 임의로 문자를 추출함
        result += random.choice(alphabet_samples)
    return result

# 작업 시작 메시지를 출력합니다.
print("Process Start ")

# 시작 시점의 시간을 기록합니다.
start_time = time.time()

# 결과물을 저장할 폴더를 생성합니다.
if os.path.exists(OUT_PATH):
    shutil.rmtree(OUT_PATH)

os.mkdir(OUT_PATH)

print(OUT_PATH ,"폴더를 생성했습니다.")

# 개인정보 파일을 자동으로 생성하는 부분입니다.
# MAX_NUM 회수만큼 반복합니다.
# 이를테면, MAX_NUM가 100이면 무작위 개인정보 생성을 100회 반복합니다.
for i in range(MAX_NUM):

    # 결과물 파일의 이름을 정의합니다.
    filename = OUT_PATH  + str(i) + '_'+'personal'+ ".txt"

    # 결과물 파일을 생성합니다. 텅 빈 파일이 생성됩니다.
    # file id 를 outfile, 파일명을 filename, 쓰기 모드로 파일을 지정합니다.
    outfile = open(filename, "w")
    
    # 핸드폰
    outfile.write('telephone : 010-'+ str(time.time())[-4:]+'-'+ str(time.time())[-6:-2]+'\n')
    
    # 나이를 무작위 생성
    outfile.write('age : '+ str(random.randrange(20,100))+'\n')
    
    # 부서명 생성
    division = random_string(4)
    outfile.write('division : '+ division +'\n')
    
    # 결과물 파일에 무작위로 선정된 성별을 기재합니다.
    # outfile에 성별을 write합니다.
    sex = ['male','female']
    outfile.write('sex : '+ random.choice(sex))
    
    # 결과물 파일 수정을 마무리합니다.
    # outfile을 close합니다.
    outfile.close()


# 작업 종료 메세지를 출력합니다.
print("Process Done.")

# 작업에 총 몇 초가 걸렸는지 출력합니다.
end_time = time.time()
print("The Job Took " + str(end_time - start_time) + " seconds.")
