#section_070.py

def select_even(*arg):
    result = []
    for num in arg:
        if num%2 == 1:
            continue
        result.append(num)
    return result

print(select_even(1,2,3,4))
print(select_even(-12, 2, 81, 99, 48, 20))

