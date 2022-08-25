from collections import deque
import copy


n = int(input())

time_list = [0] * (n+1)  # 각 강의 최소 시간 리스트
indegree = [0] * (n+1)  # 진입차수
graph = [[] for i in range(n+1)]  # 각 노드 연결 간선 정보

for i in range(1, n+1):
    data = list(map(int, input().split()))
    time_list[i] = data[0]  # 초기 시간 정보
    for x in data[1:-1]:  # 선수 과목들
        indegree[i] += 1
        graph[x].append(i)  # x를 들어야 i를 들을 수 있음


def get_time():
    result = copy.deepcopy(time_list)  # 수행 결과 리스트
    q = deque()

    # 진입 차수가 0인 노드를 큐에 삽입
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)

    while q:  # 큐가 빌 때까지
        now = q.popleft()
        for i in graph[now]:
            result[i] = max(result[i], result[now] + time_list[i])
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

    for i in range(1, n+1):
        print(result[i])


get_time()
