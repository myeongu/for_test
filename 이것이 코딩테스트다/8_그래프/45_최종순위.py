# https://www.acmicpc.net/problem/3665

from collections import deque

# test case 수만큼 반복
for tc in range(int(input())):
    n = int(input())  # 팀의 수(노드 수)
    indegree = [0] * (n+1)  # 진입 차수

    # 각 노드에 연결된 간선 정보
    graph = [[False] * (n + 1) for i in range(n + 1)]

    # 작년 순위 정보
    data = list(map(int, input().split()))
    # 방향 그래프의 간선 정보 초기화 by 작년 순위
    for i in range(n):
        for j in range(i + 1, n):
            graph[data[i]][data[j]] = True  # i가 j보다 순위 높음 == row_i col_j가 True
            indegree[data[j]] += 1  # 순위가 낮은 노드의 진입 차수 증가

    # 올해 변경된 순위 정보
    m = int(input())  # 변경된 순위 개수
    for i in range(m):
        a, b = map(int, input().split())  # 변경된 순위
        # 화살표 방향 변경(간선 방향 뒤집기)
        if graph[a][b]:  # 기존에 a가 b보다 순위가 높은 경우
            graph[a][b] = False
            graph[b][a] = True
            indegree[a] += 1  # a 순위가 낮아졌으므로 진입 차수 1 증가
            indegree[b] -= 1  # b 순위는 높아졌으므로 진입 차수 1 감소
        else:  # 기존에 b가 a보다 순위가 높은 경우
            graph[a][b] = True
            graph[b][a] = False
            indegree[a] -= 1
            indegree[b] += 1

    # 새로운 graph를 기준으로 위상 정렬 수행
    result = []  # 알고리즘 수행 결과 리스트
    q = deque()

    # 초기에는 진입차수가 0인 노드를 큐에 삽입
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)

    is_certain = True  # 위상 정렬 결과가 하나인지 여부
    is_cycle = False  # 그래프 내 사이클이 존재하는지 여부

    # 노드의 수 만큼 반복.
    for i in range(n):  # 각 반복마다 큐에서 하나의 원소가 제거 & 삽입
        if len(q) == 0:  # 큐가 빈다면 사이클이 발생한 것
            is_cycle = True
            break

        if len(q) >= 2:  # 큐의 원소가 2개 이상이라면 가능한 결과가 여러 개
            is_certain = False
            break

        now = q.popleft()
        result.append(now)  # 현재 노드를 결과에 삽입
        for i in range(1, n+1):  # 해당 원소와 연결된 노드들의 진입차수 -1
            if graph[now][i]:  # 현재 노드보다 연결된 노드가 순위가 낮은 경우
                indegree[i] -= 1
                # 새롭게 진입차수가 0이 되는 노드는 큐에 삽입
                if indegree[i] == 0:
                    q.append(i)

    if is_cycle:  # 일관성이 없는 경우
        print("IMPOSSIBLE")
    elif not is_certain:  # 결과가 여러 개인 경우
        print("?")
    else:
        for i in result:
            print(i, end=" ")
        print()
