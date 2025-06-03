words = [ 'bananana', 'apple', 'che']
# 단어 길이 기준 오름차순 정렬
words.sort(key=lambda s: len(s))
print(words)  # ['apple', 'cherry', 'bananana']