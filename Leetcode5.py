# 문제 : 가장 긴 팰린드롬 부분 문자열을 출력하라
# 헷갈린 부분 : 슬라이싱 범위

input = "cababad"

def palindrome(s:str) -> str:
    return s==s[::-1]

def longestPalindrome(s:str) -> str:

    for i in range(len(s)-1):
        for j in range(len(s)-1,i,-1):
            if s[i] == s[j]:
                if palindrome(s[i:j+1]):
                    return s[i:j+1]


print(longestPalindrome(input))

#solution : 투 포인터 확장 -> 속도 개선

def solution(s:str) -> str:
    def expand(left : int,right:int) -> str:
        while left >= 0 and right <= len(s) and s[left] == s[right-1]:
            left -= 1
            right += 1
        return s[left + 1 : right -1]

    if len(s) < 2 or s == s[::-1]:
        return s

    result = ''
    for i in range(len(s) - 1) :
        result = max(result,expand(i,i+1),expand(i,i+2),key = len)
    
    return result