import openpyxl as op
QUESTIONS = []
wb = op.load_workbook("인생태도_체크리스트.xlsx")
ws = wb.active

for q, c in ws.iter_rows(min_row=3, min_col=2, max_col=3, max_row=5, values_only=True):
    QUESTIONS.append((q,c))
    
print(QUESTIONS)

# 합산하는 dictionary
score = {"CP":0, "NP":0, "FC":0, "AC":0}

for idx,(question, category) in enumerate(QUESTIONS, start=1):
    # print(question, category)
    txt = f"질문{idx}: {question} "
    ans = ""
    while(True):
        if ans.isnumeric():
            if int(ans) >= 1 and int(ans) <= 5:
                break
        
        ans = input(txt)
    print(ans)
    
    score[category] += int(ans)
    
print(score)
