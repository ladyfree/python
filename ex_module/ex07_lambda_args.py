f = lambda *x: max(x)*2
print(f(1,2,3,4,5,8))
print(f(1,12,3,214))

f2 = lambda y, *x: max(x)*y
print(f2(2,3,4,5,8))
print(f2(3,12,3,214))