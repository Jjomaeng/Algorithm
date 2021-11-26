# 가장 큰 수

def solution(numbers):
    numbers = list(map(str,numbers))
    numbers.sort(key = lambda x : x * 3,reverse= True) # 자리수를 맞추기 위해 (기억하기)
    return str(int("".join(numbers))) # int로 변환 후 str 하는 이유 0000-> 0 으로 하기 위핸

numbers = [0,0,0,0]
print(solution(numbers))