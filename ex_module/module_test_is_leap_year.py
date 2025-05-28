import ex06_is_leap_year as my

for i in [2000,2100, 2400,2003,2004]:
    if my.is_leap_year(i):
        print(f"🎉 {i}년은 윤년입니다!")
    else:
        print(f"😌 {i}년은 평년입니다.")



