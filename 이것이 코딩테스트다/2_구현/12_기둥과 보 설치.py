# https://programmers.co.kr/learn/courses/30/lessons/60061


def possible(answer):
    for x, y, structure in answer:
        if structure == 0: # 기둥 경우: 바닥, 보 끝, 다른 기둥 위
            if y == 0 or ([x-1, y, 1] in answer or [x, y, 1] in answer) or ([x, y-1, 0] in answer):
                continue
            return False
        elif structure == 1: # 보 경우: 한쪽 기둥 위, 양쪽 보 동시
            if ([x,y-1,0] in answer or [x+1, y-1, 0] in answer) or ([x-1, y, 1] in answer and [x+1, y, 1] in answer):
                continue
            return False
    return True

def solution(n, build_frame):
    answer = []
    
    for frame in build_frame:
        x, y, structure, build = frame
        
        # 설치하는 경우
        if build == 1:
            answer.append([x,y,structure]) # 일단 설치
            if not possible(answer):
                answer.remove([x,y,structure]) # 불가능하면 다시 제거
                
        # 삭제하는 경우
        elif build == 0:
            answer.remove([x,y,structure]) # 일단 제거
            if not possible(answer):
                answer.append([x,y,structure])
    return sorted(answer)