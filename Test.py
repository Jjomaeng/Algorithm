def solution(input):
    input.sort()
    answer = 0
    for i in range(len(input)//2):
        answer += min(input[i*2],input[(i*2)+1])

    return answer
input = [1,4,2,3,5,6]
print(solution(input))