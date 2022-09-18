def solution(N):
    answer = 0
    for i in range(1,N):
        sum_num = i
        sum_num += sum(map(int,str(i)))
        if sum_num == N:
            answer = i
            break

    return answer

N = 216
print(solution(N))
