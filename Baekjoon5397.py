def find_password(log):
    front = list()
    back = list()

    for c in log :
        if c == "-":
            if front :
                front.pop()

        elif c == "<" :
            if front:
                back.append(front.pop())
        elif c == '>':
            if back:
                front.append(back.pop())
        else:
            front.append(c)

    return "".join(front) + "".join(back[::-1])

def solution(log):
    answer = ""
    answer = find_password(log)

    return answer

print(solution("<<BP<A>>Cd-"))