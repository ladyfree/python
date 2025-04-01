attendance = {
    "민수": True,
    "지연": False,
    "철수": True
}

for i, j in attendance.items():
    if j == True :
        print(i, '출석')
    else:
        print(i, '결석')