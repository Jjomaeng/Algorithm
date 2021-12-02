# 문제 : 문자열 압축
# 범위 꼼꼼하게 하기
input = "xababcdcdababcdcd"
def my_solution(s:str) -> int:
    cnts = []

    
    for i in range(1,len(s)-2):
        lens = 0
        count = 1
        result = ""
        
        for j in range(0,len(s),i):
            if s[j:j+i] == s[j+i:j+(2*i)]:
                
                count += 1
            elif  lens ==  (len(s)//i-1):
                if count == 1:
                    result += s[j:j+i] + s[j+i:]
                else :
                    result += (str(count) +s[j:j+i] + s[j+i:])

            elif lens < (len(s)//i-1):
                if count == 1:
                    result += s[j:j+i]
                else :
                    result += (str(count) +s[j:j+i])
                    count = 1
            lens += 1
            
        cnts.append(len(result))

    return min(cnts)

#solution

def compress(text,tok_len):
    words = [text[i:i+tok_len] for i in range(0,len(text),tok_len)]
    res = []
    cur_word = words[0]
    cur_cnt = 1
    for a,b in zip(words,words[1:]+[""]):
        if a==b :
            cur_cnt += 1
        else :
            res.append([cur_word,cur_cnt])
            cur_word =b
            cur_cnt =1
    return sum(len(word) + (len(str(cnt)) if cnt > 1 else 0) for word,cnt in res)

def solution(text):
    return(min(compress(text,i) for i in list(range(1,len(text)//2 +1))+[len(text)]))


print(solution(input))