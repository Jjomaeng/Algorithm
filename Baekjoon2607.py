def counting(ar,word):
    for w in word :
        i = ord(w) - ord('A')
        ar[i] += 1


def solution(n,words):
    answer = 0
    diff = 0
    freq_firstword = [0]* 26
    length = len(words[0])

    counting(freq_firstword,words[0])

    for i in range(1,n):
        diff = 0
        freq_other = [0] * 26
        counting(freq_other,words[i])

        for freq1,freq2 in zip(freq_other,freq_firstword):
            diff += abs(freq1 - freq2)

        if (diff == 0 or diff == 1 or (diff == 2 and (len(words[i]) == length))) : 
            answer += 1

    return answer

n = 4
words = ['DOG','GOD','GOOD','DOLL']

print(solution(n,words))
