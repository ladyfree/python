import pandas as pd

# 2중 리스트 데이타
data = [['철수', '영희', '민수'],
        [12, 13, 12],
        ['남', '여', '남'],
        [88, 92, 75]]

df = pd.DataFrame(data, index=['이름','나이', '성별', '점수']).T
print(df)
out_excel = 'oa_excel/output'+'/'+'df_sample2.xlsx'
df.to_excel(out_excel)

# 특정한 컬럼(열) 읽기= 반환
# '이름'열 읽기
# for i in df['점수']>80:
#     print(i)

# df = df[df['점수']>80]
# print(df)

# 평균
print(df['점수'].mean())