L = [[9, 1, 3,4,5,7 ], [8, 2], [7, 3], [6, 4]]

max1 = max(L, key=lambda x: x[0])
max2 = max(L, key=lambda x: x[1])
min1 = min(L, key=lambda x: x[0])
min2 = min(L, key=lambda x: x[1])

print(max1)  #[9, 1]
print(max2)  #[6, 4]
print(min1)  #[6, 4]
print(min2)  #[9, 1]