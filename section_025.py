#section_025.py

myStr = 'Hello, My little baby'
print(myStr.upper())
print(myStr.lower())
print(myStr.title())
print()

print(myStr.count('b'))
print(myStr.endswith('y'))
print(myStr.startswith('h'))
print(myStr.lower().startswith('h'))
print()

myStrlist1 = myStr.split()
print(myStrlist1)
myStrlist2 = myStr.split(',')
print(myStrlist2)
print()

myStrfill = myStr.zfill(30)
print(myStrfill)
