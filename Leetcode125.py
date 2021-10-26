#문제 : 주어진 문자열이 팰린드롬인지 확인하라. 대소문자를 구분하지 않으며, 영문자와 숫자만을 대상으로 한다.

import re

def checkPalindrome(s: str) -> bool:
    check = re.sub('[^a-z0-9]',"",s.lower())
    check = list(check)
    print(check)

    while len(check) > 1 :
        if check.pop() != check.pop(0):
            return False

        
    return True

input = "A man, a plan, a canal : Panama"
F_input = "apple"

print(checkPalindrome(F_input))