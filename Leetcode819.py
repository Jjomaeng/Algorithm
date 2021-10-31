# 금지된 단어를 제외한 가장 흔하게 등장하는 단어를 출력하라. 대소문자 구분을 하지 않으며, 구두점(마침표,쉼표 등) 또한 무시한다.

# 헷갈린 부분 : defalultdict() - collection/collections 둘 다 있음

paragraph = "Bob hit a ball , the hit BALL flew far after it was hit"
banned = ["hit"]


import collections
import re
from collections import defaultdict

def mostCommonWord(p : str , b : list[str]) -> str:
    p = re.sub('[,.]','',p.lower()).split()

    counts = defaultdict(int)

    for char in p:
        if char not in banned:
            counts[char] += 1
    return max(counts,key=counts.get)



#solution = counter 객체 사용

def solution(p : str,banned : list[str]) -> str:
    words = [word for word in re.sub(r'[^\w]',' ',p).lower().split() if word not in banned]

    counts = collections.Counter(words)

    return counts.most_common(1)[0][0] # 첫번째로 흔한 단어 출력 /[('ball',2)][0][0]

print(solution(paragraph,banned))