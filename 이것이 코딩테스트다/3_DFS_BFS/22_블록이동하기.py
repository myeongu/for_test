# https://school.programmers.co.kr/learn/courses/30/lessons/60063?language=python3

from collections import deque


def get_next_pos(pos, board):
    next_pos = []  # 다음으로 방문할(큐에 삽입할) 위치들
    pos = list(pos)  # 현재 위치를 집합 형태에서 리스트 형태로
    pos1_x, pos1_y, pos2_x, pos2_y = pos[0][0], pos[0][1], pos[1][0], pos[1][1]

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    for i in range(4):  # 이동할 위치
        next_pos1_x, next_pos1_y, next_pos2_x, next_pos2_y = \
            pos1_x + dx[i], pos1_y + dy[i], pos2_x + dx[i], pos2_y + dy[i]
        # 이동하고자 하는 두 칸 모두 비어 있다면 next_pos에 추가
        if board[next_pos1_x][next_pos1_y] == 0 and board[next_pos2_x][next_pos2_y] == 0:
            next_pos.append({(next_pos1_x, next_pos1_y),
                            (next_pos2_x, next_pos2_y)})

    # 현재 수평
    if pos1_x == pos2_x:
        for i in [-1, 1]:
            # 회전 가능 상태라면 next_pos에 추가
            if board[pos1_x + i][pos1_y] == 0 and board[pos2_x + i][pos2_y] == 0:
                next_pos.append({(pos1_x, pos1_y), (pos1_x + i, pos1_y)})
                next_pos.append({(pos2_x, pos2_y), (pos2_x + i, pos2_y)})

    # 현재 수직
    if pos1_y == pos2_y:
        for i in [-1, 1]:
            # 회전 가능 상태라면 next_pos에 추가
            if board[pos1_x][pos1_y + i] == 0 and board[pos2_x][pos2_y + i] == 0:
                next_pos.append({(pos1_x, pos1_y), (pos1_x, pos1_y + i)})
                next_pos.append({(pos2_x, pos2_y), (pos2_x, pos2_y + i)})

    return next_pos


def solution(board):
    n = len(board)
    # 기존 board를 1로 감싸는 새로운 board 생성
    new_board = [[1] * (n+2) for _ in range(n+2)]
    for i in range(n):
        for j in range(n):
            new_board[i + 1][j + 1] = board[i][j]

    q = deque()
    visited = []
    pos = {(1, 1), (1, 2)}
    q.append((pos, 0))
    visited.append(pos)
    # q가 빌 때까지 반복
    while q:
        pos, time = q.popleft()

        if (n, n) in pos:  # 최종 지점 도착
            return time

        # 현재 위치 기준 이동할 수 있는 위치 파악
        for next_pos in get_next_pos(pos, new_board):
            # 만약 방문하지 않은 pos라면 큐에 삽입한 후 방문 처리
            if next_pos not in visited:
                q.append((next_pos, time + 1))
                visited.append(next_pos)

    return 0
