
# 오답 노트 


"""
의문점 및 생각

저 함수를 활용해서 보냈을 때 제일 먼저 나오는 문자를 거를 수 있나?
MAX 값이 여러 개일 때 길이로만 키 값을 잡았으니까
가장 긴 길이가 return되면 while문을 못빠져 나오면 의미가 있을까?
return의 슬라이싱은 시간복잡도에 영향이 없나 

  
"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 팰린드롬 판별 및 투 포인터 확장
        # s[left] == s[right]: 이 팰린드롬인지 확인하는 조건.
        def expand(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right] 
            # 입력받았던 포인터 기준으로 얻은 가장 큰 팰랜드롬 부분 문자열.
            # 하나 이전꺼 반환

        # 입력 문자열이 이미 팰린드롬이면 그 자체를 빠르게 반환.
        if len(s) < 2 or s == s[::-1]:
            return s

        result = ''
        # 슬라이딩 윈도우 우측으로 이동
        for i in range(len(s) - 1):
            result = max(result, # 한 칸 이전 포인터들까지의 가장 긴 팰린드롬 부분 문자열.
                         expand(i, i + 1), # 2칸짜리 포인터
                         expand(i, i + 2), # 3칸짜리 포인터
                         key=len) # 길이 기준으로
        return result