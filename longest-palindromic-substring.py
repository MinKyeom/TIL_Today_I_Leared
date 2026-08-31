# 출처:https://leetcode.com/problems/longest-palindromic-substring/

# 개선 중 
# 투포인터에 대한 접근 생각 for문 2번을 실행할 걸 1번만에 해결

from collections import deque,Counter
import copy

class Solution:
    def longestPalindrome(self, s: str) -> str:
        sList = list(s)
        check = []
        for start in range(len(s)):
            words = sList[start]

            for end in range(start+1,len(s)):
                words+=sList[end]
                check.append(words)
        
            if len(words)==1:
                check.append(words)

        check = set(check)

        num = 0
        result = ''
        for c in check:
            if c == c[::-1] and len(c) > num:
                num = len(c)
                result = c

        return result

# 개선 중
from collections import deque,Counter
import copy

class Solution:
    def longestPalindrome(self, s: str) -> str:
        String_list = list(s)
        before_list = deque([''])
        result_list = []

        if len(String_list) == 1:
            return String_list[0]

        elif len(String_list)==0:
            return ''

        # 직전 문자
        beforeString = ''

        for String_num in range(len(String_list)):
            String = s[String_num]

            new_list = deque([])
            
            for num in range(len(before_list)):
                
                # 해당 문자
                before = before_list[num]

                # 빈 리스트인 경우 확인 필요 없음
                if before =='':
                    before += String
                    new_list.append(before)
                    

                else:
                    start = String_num - 1

                    # 이전 현재 숫자를 비롯해 점검
                    for minus in range(len(before)-1,-1,-1):
                        print(before[minus],s[start])
                        # 문자열 비교
                        if before[minus] == s[start]:
                            start-=1 
                            
                        else:
                            break
                
                    else:
                        # print(before)
                        before+=String
                        new_list.append(before)
                        
            #print("before",before_list)
            before_list += new_list
            #print("after",before_list)
        #print("end",before_list)
 

        result_num =0
        result = ''

        for check in before_list:

            check_count = Counter(check)

            # 앞 뒤가 같고, 총 개수가 2개
            if len(check) >=2 and check == check[::-1]:
                if len(check) > result_num:
                    result_num = len(check)
                    result = check
            else:
                if len(check) == 1 and result_num ==0:
                    result_num = len(check)
                    result =check


        return result

# 개선 중 
from collections import deque,Counter
import copy

class Solution:
    def longestPalindrome(self, s: str) -> str:
        String_list = list(s)
        before_list = deque([''])
        result_list = []

        if len(String_list) == 1:
            return String_list[0]

        elif len(String_list)==0:
            return ''

        # 직전 문자
        beforeString = ''

        for String in String_list:

            new_list = deque([])
            
            for num in range(len(before_list)):
                
                # 해당 문자
                before = before_list[num]

                # 빈 리스트인 경우 확인 필요 없음
                if before =='':
                    before += String
                    new_list.append(before)
                    continue

                else:
                    start = num

                    # 이전 현재 숫자를 비롯해 점검
                    for minus in range(len(before)-1,-1,-1):
                        if before[minus] == s[start]:
                            start-=1 
                            continue
                        
                        else:
                            break
                
                    else:
                        before+=String
                        new_list.append(before)
                        continue


            before_list += new_list
            # print(new_list)
 

        result_num =0
        result = ''

        for check in before_list:

            check_count = Counter(check)

            # 앞 뒤가 같고, 총 개수가 2개
            if len(check) >=2 and check == check[::-1]:
                if len(check) > result_num:
                    result_num = len(check)
                    result = check
            else:
                if len(check) == 1 and result_num ==0:
                    result_num = len(check)
                    result =check


        return result

# 개선 중
from collections import deque,Counter
import copy

class Solution:
    def longestPalindrome(self, s: str) -> str:
        String_list = list(s)
        before_list = deque([''])
        result_list = []

        if len(String_list) == 1:
            return String_list[0]

        elif len(String_list)==0:
            return ''

        for String in String_list:

            new_list = deque([])
            
            for before in before_list:
                before += String
                new_list.append(before)
            
            before_list += new_list
            # print(new_list)

        # print(before_list) 

        result_num =0
        result = ''

        for check in before_list:

            check_count = Counter(check)

            # 앞 뒤가 같고, 총 개수가 2개
            if len(check) >=2 and check == check[::-1]:
                if len(check) > result_num:
                    result_num = len(check)
                    result = check
            else:
                if len(check) == 1 and result_num ==0:
                    result_num = len(check)
                    result =check


        return result

# 개선 중 

from collections import deque,Counter

class Solution:
    def longestPalindrome(self, s: str) -> str:
        String_list = list(s)
        before_list = deque([])
        result_list = []

        for String in String_list:
            before_list.appendleft('')

            new_list = deque([])
            
            for before in before_list:
                before += String
                new_list.append(String)
            

            before_list = new_list

        print(before_list) 

        result_num =0
        result = ''

        for check in before_list:

            check_count = Counter(check)

            # 앞 뒤가 같고, 총 개수가 2개
            if check[0] == check[-1] and check_count[check[0]]==2:
                if len(check) > result_num:
                    result_num = len(check)
                    result = check

        return result


"""
다른 분 풀이
출처: https://cuffyluv.tistory.com/124

  #  class Solution:
  #     def longestPalindrome(self, s: str) -> str:
  #       # 팰린드롬 판별 및 투 포인터 확장
  #       # s[left] == s[right]: 이 팰린드롬인지 확인하는 조건.
  #       def expand(left: int, right: int) -> str:
  #           while left >= 0 and right < len(s) and s[left] == s[right]:
  #               left -= 1
  #               right += 1
  #           return s[left + 1:right] 
  #           # 입력받았던 포인터 기준으로 얻은 가장 큰 팰랜드롬 부분 문자열.
  #           # 하나 이전꺼 반환

  #       # 입력 문자열이 이미 팰린드롬이면 그 자체를 빠르게 반환.
  #       if len(s) < 2 or s == s[::-1]:
  #           return s

  #       result = ''
  #       # 슬라이딩 윈도우 우측으로 이동
  #       for i in range(len(s) - 1):
  #           result = max(result, # 한 칸 이전 포인터들까지의 가장 긴 팰린드롬 부분 문자열.
  #                        expand(i, i + 1), # 2칸짜리 포인터
  #                        expand(i, i + 2), # 3칸짜리 포인터
  #                        key=len) # 길이 기준으로
  #       return result   
"""
  
  # 리트코드 샘플 DP 정답
  # 출처 : 리트코드 샘플 코드


"""
# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         n = len(s)
#         dp = [[False] * n for _ in range(n)]
#         ans = [0, 0]

#         for i in range(n):
#             dp[i][i] = True

#         for i in range(n - 1):
#             if s[i] == s[i + 1]:
#                 dp[i][i + 1] = True
#                 ans = [i, i + 1]

#         for diff in range(2, n):
#             for i in range(n - diff):
#                 j = i + diff
#                 if s[i] == s[j] and dp[i + 1][j - 1]:
#                     dp[i][j] = True
#                     ans = [i, j]

#         i, j = ans
#         return s[i : j + 1]
    """