def solution(n,name,kor,eng,math):
    arr = [(name[i],kor[i],eng[i],math[i]) for i in range(n)]

    arr.sort(key = lambda x : (-x[1],x[2],-x[3],x[0]))

    answer = []

    for n in arr:
        answer.append(n[0][0])

    return answer

n = 6
name = ['A','B','C',"D",'E','F']
kor = [50,80,80,50,50,60]
eng = [60,60,70,60,60,80]
math = [100,50,100,90,100,100]

print(solution(n,name,kor,eng,math))