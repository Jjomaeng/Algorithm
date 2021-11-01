# 문자열 배열을 받아 애너그램 단위로 그룹핑하라
# 헷갈린 부분 : sort() 와 sorted의 차이/ defaultdict(list)에 문자열 그대로 넣는 방법
import collections


input = ["eat","tea","tan","ate","nat","bat"]

def groupAnagrams(s : list[str]) -> list[str]:
    groupAna = collections.defaultdict(list)


    for char in s:
        key = "".join(sorted(list(char)))
        groupAna[key] += [char] #헷갈린 부분
        
        #개선
        #groupAna["".join(sorted(char))].append(char)

    return groupAna.values()

print(groupAnagrams(input))

