# 출처:https://leetcode.com/problems/longest-substring-without-repeating-characters/
# 풀이 개선 중
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        check = list(s)
        start = ''
        result_list = []
        result = 0
        for c in check:
            if c not in start:
                start+=c
                if start not in result_list:
                    result_list.append(start)
                
                result = max(len(start),result)
            else:
                result = max(len(start),result)
                start =''
                start+=c
        print(result_list)
        return result
