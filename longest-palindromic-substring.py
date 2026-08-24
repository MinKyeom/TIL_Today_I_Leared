# 출처:https://leetcode.com/problems/longest-palindromic-substring/

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