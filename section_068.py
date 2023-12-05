#section_068.py

def turnNone(value):
    x = value

def turnValue(value):
    x = value * 10
    return x

def turnSet(value):
    x = {value, value+1, value+2}
    return x

def turnTuple(value):
    return value, value-1, value-2

print(turnNone(10))
print(turnValue(10))
print(turnSet(10))
print(turnTuple(10))
