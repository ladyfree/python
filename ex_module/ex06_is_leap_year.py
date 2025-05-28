def is_leap_year(year: int) -> bool:
    
    # 4의 배수이고 (100의 배수가 아니거나 400의 배수)이면 True
    if year % 4 == 0 and (year % 100 !=0 or year % 400 == 0):
        return True
   
    return False

# if __name__ == "__main__":
#     year_input = int(input("년도를 입력하세요 : "))
#     if is_leap_year(year_input):
#         print(f"🎉 {year_input}년은 윤년입니다!")
#     else:
#         print(f"😌 {year_input}년은 평년입니다.")

year_input = int(input("년도를 입력하세요 : "))
if is_leap_year(year_input):
    print(f"🎉 {year_input}년은 윤년입니다!")
else:
    print(f"😌 {year_input}년은 평년입니다.")