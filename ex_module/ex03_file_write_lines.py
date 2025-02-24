# 여러 줄 파일 쓰기
# 파일 쓰기 (모드 : w)

DIRECTORY = 'ex_module' # 경로로
file_name = DIRECTORY + '/'+'sample_poem2.txt' # 파일명명
lines = ["별을 노래하는 마음으로", "모든 죽어가는 것을 사랑해야지", "그리고 나한테 주어진 길을"]
#lines2 = ["별을 노래하는 마음으로\n", "모든 죽어가는 것을 사랑해야지\n", "그리고 나한테 주어진 길을\n"]

with open(file_name, "w", encoding="utf-8") as fd:  # 파일 열기 (쓰기 모드, "w")
    fd.writelines(x +'\n' for x in lines)  # 리스트의 각 요소를 파일에 한 줄씩 씀
