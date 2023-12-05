#section_017.py

comp1 = 2 + 5j
print("변수 comp1의 자료형은", type(comp1))
print()

comp2 = complex(3, -6)
print("복소수 comp2의 값은", comp2)
print("실수 부분은", comp2.real)
print("허수 부분은", comp2.imag)
print("켤레 복소수는", comp2.conjugate())
