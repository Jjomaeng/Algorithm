# 문자열을 두집는 함수를 작성하라. 입력값은 문자 배열이며, 리턴 없이 리스트 내부를 직접 조작하라
# 헷갈린 부분 : split()함수

input = ["h","e","l","l","o"]

def reverse_string(s : list[str]) -> list[str]:
    s = "".join(s)
    s = s[::-1]
    s = list(s) ##헷갈린 부분

    return s

print(reverse_string(input))

#solution : 투 포인터 사용

def reverseString(s: list[str]) -> None:
    left,right = 0, len(s) -1
    while left < right:
        s[left], s[right] = s[right] , s[left]
        left += 1
        right -= 1

# reverse() 함수 사용 -> 리스트에 제공되는 함수 (문자열에서는 s[::-1])

def reverseString(s:list[str]) -> None:
    s.reverse()