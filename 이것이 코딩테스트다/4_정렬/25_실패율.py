# https://school.programmers.co.kr/learn/courses/30/lessons/42889

def solution(N, stages):
    fail = [0] * (N)  # 각 스테이지 실패율(index=스테이지)
    stages.sort()

    player_dict = dict()
    fail_dict = dict()

    for i in range(1, N+1):
        fail_dict[i] = 0

    for stage in stages:
        if stage in player_dict.keys():
            player_dict[stage] += 1
            continue
        player_dict[stage] = 1

    player_num = len(stages)

    for stage, cur_num in player_dict.items():
        if stage == N+1:
            break
        fail_dict[stage] = cur_num / player_num
        player_num -= cur_num

    answer = []
    for i in sorted(fail_dict.items(), key=lambda x: -x[1]):
        answer.append(i[0])

    return answer


# 모범 답안
'''
def solution(N, stages):
    answer = []
    length = len(stages)

    # 스테이지 번호를 1부터 N까지 증가시키며
    for i in range(1, N + 1):
        # 해당 스테이지에 머물러 있는 사람의 수 계산
        count = stages.count(i)
        
        # 실패율 계산
        if length == 0:
            fail = 0
        else:
            fail = count / length
        
        # 리스트에 (스테이지 번호, 실패율) 원소 삽입
        answer.append((i, fail))
        length -= count

    # 실패율을 기준으로 각 스테이지를 내림차순 정렬
    answer = sorted(answer, key=lambda t: t[1], reverse=True)
    
    # 정렬된 스테이지 번호 반환
    answer = [i[0] for i in answer]
    return answer
'''
