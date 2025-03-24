import pandas as pd

in_excel = r"oa_excel/output/" + "exam_pandas1.xlsx"

df = pd.read_excel(in_excel, sheet_name='학생데이타')
# print(df.head()) #상위 5줄
# print(df.tail()) #하위 5줄

# shape
# print(df.shape)

# 컬럼명 출력하기
# print(df.columns)

# print(df[["나이","영어",'이름']])

# 특정한 행 출력하기
# print(df.iloc[0]) # 첫번째
# print(df.iloc[1:4]) # 두번째부터 4번째까지

df["총점"] = df["국어"] + df["영어"] + df["수학"]
print(df)

out_excel = r"oa_excel/output/" + "out_exam_pandas1.xlsx"
df.to_excel(in_excel, index= False )