#section_080.py

state1 = 'print("I Love Python")'
exec(state1)

state2 = '''
number = 1
for item in [1, 2, 3]:
    number = number + 1
    if item%2:
        break
print(number)
'''
exec(state2)
