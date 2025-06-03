funcs = [
    lambda x: x + 1,
    lambda x,y: y + x,
    lambda z: z + 3
]
print(funcs[0](5))  # 6
print(funcs[1](5,6))  # 7
print(funcs[2](5))  # 8

