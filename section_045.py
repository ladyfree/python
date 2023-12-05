#section_045.py

my_exo = {1: "수호", 2: "찬열", 3: "카이", 4: "디오"}
viewItems = my_exo.items()
viewKeys = my_exo.keys()
viewValues = my_exo.values()

print(viewItems)
print(viewKeys)
print(viewValues)
print()

my_exo.pop(4)       # 원본에 변화를 줌
print(viewItems)
print(viewKeys)
print(viewValues)
print()

print(list(my_exo.keys()))
print(list(viewValues))
