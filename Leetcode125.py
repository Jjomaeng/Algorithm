#문제 : 주어진 문자열이 팰린드롬인지 확인하라. 대소문자를 구분하지 않으며, 영문자와 숫자만을 대상으로 한다.

# my_solution
# 오류난 부분 : 정규표현식,리턴값이 리스트인지 문자열인지(리스트에 들어가는 함수/ 문자열에 들어가는 함수)
import re
from typing import Collection, Deque

def checkPalindrome(s: str) -> bool:
    check = re.sub('[^a-z0-9]',"",s.lower())
    check = list(check)

    while len(check) > 1 :
        if check.pop() != check.pop(0):
            return False

        
    return True

input = "A man, a plan, a canal : Panama"
F_input = "apple"

print(checkPalindrome(F_input))

#개선점 : 숫자,영어만 남기고 제거하고 소문자로 바꾼 문자열은 바로 비교 가능 -> 슬라이싱 이용

#solution

def solution1( s: str) -> bool :
    ans = re.sub('[^a-z0-9]','',s.lower())
    return ans == ans[::-1]

# 다른 풀이1
# 문자열을 리스트에 숫자,영어만 받기 -> pop() 사용

def solution2(s:str) -> bool:
    ans = []
    for char in s:
        if char.isalnum():
            ans.append(char.lower())
    
    while len(ans) > 1:
        if char.pop() != char.pop(0):
            return False

    return True

# 다른 풀이
# 풀이1에 대한 개선점 -> list를 deque로 사용하면 속도에서 성능 개선

def solution3(s:str) -> bool:
    ans : Deque = Collection.deque()

    for char in s:
        if char.isalnum():
            ans.append(char.lower())
    
    while len(ans) > 1 :
        if ans.popleft() != ans.pop(): # -> 속도 향상 부분
            return False

    return True






