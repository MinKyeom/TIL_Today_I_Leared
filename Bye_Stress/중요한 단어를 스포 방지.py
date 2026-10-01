# 소문자와 숫자로만 구성됨
# 출처: https://school.programmers.co.kr/learn/courses/30/lessons/468370

"""

목적: 스포방지 단어 중 중요한 단어의 수

"""

def solution(message, spoiler_ranges):
    test = message.split(" ")
    
    for start,end in spoiler_ranges:
        print(message[start:end+1])
    answer = 0
    return answer