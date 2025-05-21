import os

# 현재 디렉토리 위치 확

# 디렉토리 변경
os.chdir(r"c:\workspace\oa_excel\output")

# 현재 디렉토리 위치 확인
print(os.getcwd())

# # 디렉토리 생성
# os.mkdir(r"c:\new_folder")

# # 디렉토리들을 생성
# os.makedirs(r"c:\new_folder\a\b\c")

# # 폴더 존재 여부 확인
# if(os.path.exists(r"c:\new_folder\f")):
#     print("있어")
# else:
#     for i in 'cdefg':
#         os.makedirs(f"c:/new_folder/{i}")
#     print("다 만들었어")

os.rmdir(r"c:\new_folder\a\b\c")
