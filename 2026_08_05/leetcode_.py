# 출처:https://leetcode.com/problems/longest-substring-without-repeating-characters/

# 정답 풀이(list > set으로 변경)
from collections import deque

class Solution3:
    def lengthOfLongestSubstring(self, s: str) -> int:
        check = deque(list(s))
        start = deque([])
        result_list = set()
        result = 0
        
        for c in check:
            if c not in start:
                start.append(c)
                if "".join(start) not in result_list:
                    result_list.add("".join(start))
                
                result = max(len(start),result)
            else:
                
                while True:
                    k = start.popleft()
                    if k==c:
                        break

                # print(start)
                start.append(c)
                result_list.add("".join(start))

        # print(result_list)
        return result


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

# 개선 시킨 풀이
from collections import deque

class Solution2:
    def lengthOfLongestSubstring(self, s: str) -> int:
        check = deque(list(s))
        start = deque([])
        result_list = deque([])
        result = 0
        
        for c in check:
            if c not in start:
                start.append(c)
                if "".join(start) not in result_list:
                    result_list.append("".join(start))
                
                result = max(len(start),result)
            else:
                
                while True:
                    k = start.popleft()
                    if k==c:
                        break

                # print(start)
                start.append(c)
                result_list.append("".join(start))

        # print(result_list)
        return result

