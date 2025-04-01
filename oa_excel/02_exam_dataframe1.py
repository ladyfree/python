import pandas as pd

data = {'이름':['철수', '영희', '민수'],
        '나이':[12,13,12],
        '성별':['남','여','남'],
        '점수':[88, 92, 75]}

# 데이타프레임
df = pd.DataFrame(data)
print(df)

df.to_excel('df_sample.xlsx', index=False)