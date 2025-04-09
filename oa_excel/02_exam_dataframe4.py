import pandas as pd
import numpy as np

# 3x3의 행렬 데이터를 만들기
col = ['col1','col2','col3']
row = ['row1','row2','row3']
data = np.random.rand(3,3)*100
df = pd.DataFrame(data=data, index=row, columns=col)
print(df)
print("=" * 20)
df = df.mul(1000)
#print(df.mul(1000))
df.to_excel("test_pandas.xlsx")