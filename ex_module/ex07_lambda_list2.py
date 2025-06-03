# 예: 문자열 전처리 함수들
transforms = [
    lambda s: s.strip(),                       # 양쪽 공백 제거
    lambda s: s.lower(),                       # 모두 소문자로
    lambda s: s.replace('-', ' '),             # 하이픈 → 공백
    lambda s: ''.join(ch for ch in s if ch.isalnum() or ch.isspace())
]

def preprocess(text):
    for func in transforms:
        text = func(text) # transforms[0](text)
    return text

raw = "  Hello-World!!23  "
print(preprocess(raw))  # "hello world"
