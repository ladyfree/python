#section_071.py

def print_odd(start, end):
    '''주어진 범위에서 홀수를 리스트로 만들어 주는 함수입니다.
    start: 시작 값을 지정합니다.
    end: 끝 값을 지정합니다.'''
    result = []
    for num in range(start, end+1):
        if num%2 == 0:
            continue
        result.append(num)

    return result

help(print_odd)
print('-' * 50)
print_odd.__doc__ = '''이건 연습삼아서'''
help(print_odd)
print('-' * 50)
print(print_odd(3, 19))
