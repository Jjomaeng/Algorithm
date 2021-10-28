# 문제 : 로그를 재정렬하라. 기준은 다음과 같다.
#       1. 로그의 가장 앞 부분은 식별자다.
#       2. 문자로 구성된 로그가 숫자 로그보다 앞에 온다.
#       3. 식별자는 순서에 영향을 끼지지 않지만, 문자가 동일한 경우 식별자 순으로 한다.
#       4. 숫자 로그는 입력 순서대로 한다.

# 헷갈린 부분 : sort 2차 정렬/ 리스트 슬라이싱

input = ["dig1 8 1 5 1", " let1 art can", "dig2 3 6","let2 own kit dig","let3 art zero"]

def reorderLog(s : list[str]) -> list[str] :
    dig = []   #dig, let = [],[]
    let = []

    for i in s:
        print(i.split()[1])
        if i.split()[1].isnumeric():
            dig.append(i)
        else :
            let.append(i)
    
    let.sort(key = lambda x : (x.split()[1:],x.split()[0])) # 헷갈린 부분
    return let + dig

print(reorderLog(input))

