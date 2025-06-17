from tkinter import messagebox
response = messagebox.askyesnocancel("질문", "삭제하시겠습니까?")
print(response)
if response == True:
    print("삭제되었습니다111.")
elif response == None :
    print("삭제되었습니다222.")
else:
    print("삭제 취소하였습니다")