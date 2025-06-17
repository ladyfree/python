QUESTIONS = [
    ('남의 말을 곧이 곧대로 잘 믿는다.', 'NP'),
    ('자신의 생활에 충실하다.', 'FC'),
    ('다른 사람에게서 "당신과 있으면 안심이야"라는 소리를 자주 듣는다.', 'NP'),
    ('개인적인 비밀을 남에게 거의 얘기하지 않는다.', 'CP'),
    ('남의 얘기에 상처를 잘 받는다.', 'AC'),
    ('상대의 무신경함에 화내는 일이 자주 있다.', 'CP')
]

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
