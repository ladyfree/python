#section_081.py

number = 0

exp = 'number + 1'
code1 = compile(exp, '<string>', 'eval')
for h in range(100):
    number = eval(code1)
print('1', number)


state1 = 'number = number + 1'
code2 = compile(state1, '<string>', 'single')
for h in range(100):
    exec(code2)
print('2', number)


state2 = '''
for item in [1, 2, 3]:
    number = number + 1
    if item == 2:
        break;
print('3', number)
'''
code3 = compile(state2, '<string>', 'exec')
exec(code3)

