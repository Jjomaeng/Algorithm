def solution(time,n):
    answer = 0
    time.sort()
    count = list(range(n))
    for d,c in zip(time,count):
        print(d,c)
        answer += d * (n-c)
        
    return answer


time = [3,1,4,3,2]
num = 5
solution(time,num)