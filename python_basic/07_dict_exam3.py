attendance = {
    "민수": [100,200,300],
    "지연": {'a':'apple','b':'banana', 'c':'orange'},
    "철수": (0,2,34,5, 6)
}

for i in attendance.values():
    for j in i:
        print(j)