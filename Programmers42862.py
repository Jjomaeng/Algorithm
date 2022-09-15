
def solution(n,lost,reverse):
    answer = n - len(lost)

    for i in lost:
        if ( i-1 in reverse ) :
            reverse.remove(i-1)
            answer += 1
        elif (i + 1  in reverse) :
            reverse.remove(i+1)
            answer += 1
    return answer

print(solution(3,[3],[1])) 