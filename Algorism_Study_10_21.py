# 출처:https://school.programmers.co.kr/learn/courses/30/lessons/468379?language=python3

"""
조건:격자는 회전을 하지 않는다
선인장 범위가 정해져있고, 그 범위가 비가 내리는 위치가 정해져 있을 때 가장 늦게 맞을 위치를 정하고 찾아야한다

아이디어:

각 범위를 이동시키면서, 제일 처음 맞는 날의 Day를 리스트화 시키고 그게 맞을 시 해당 리스트 종료
정답은 Day 중 가장 뒤에있고 조건에 맞는 위치를 찾기

비를 뿌리는 날을 기록하여 board에 해놓고 가장 늦게 맞는 날을 기록하는 방법도 고민

목표: 선인장이 제일 비가 늦게 맞게 하는 방법

"""
def solution(m, n, h, w, drops):
    board = [ [0 for i in range(m)] for j in range(n)]
    
    print(board)
    
    for num,i in enumerate(drops):
        print(num,i)
        
    
    
    
    return 0

"""
조건:격자는 회전을 하지 않는다

아이디어:

목표: 선인장이 제일 비가 늦게 맞게 하는 방법

"""
def solution(m, n, h, w, drops):
    board = [ [0 for i in range(m)] for j in range(n)]
    
    print(board)
    
    
    return answer