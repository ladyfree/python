#section_049.py

print('햄버거를 만들어보자.')

basemat = ('빵', '토마토', '야채', '소스')
coremat = ('새우', '불고기', '한우', '치즈')

print('''{food}의 기본재료는 {base}이고,
핵심재료에 따라 이름이 달라져.'''.format(food='햄버거', base=basemat))
print()

for item in coremat:
    print('핵심재료가 {core}면 {core}버거'.format(core=item))
