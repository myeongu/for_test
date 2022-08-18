# https://school.programmers.co.kr/learn/courses/30/lessons/60060

from bisect import bisect_left, bisect_right


def count_index(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index


array = [[] for _ in range(10001)]  # 단어들 길이별로 리스트 저장
reversed_array = [[] for _ in range(10001)]  # 단어들 길이별로 뒤집어서 저장


def solution(words, queries):
    answer = []
    for word in words:  # 모든 단어를 길이별로 정방향, 역방향으로 배열에 삽입
        array[len(word)].append(word)
        reversed_array[len(word)].append(word[::-1])

    for i in range(10001):  # 각 배열 정렬 for 이진 탐색
        array[i].sort()
        reversed_array[i].sort()

    for q in queries:
        # ?을 a로 대체한 단어가 들어갈 위치부터 z로 대체한 단어가 들어갈 위치까지의 범위
        if q.endswith('?'):
            result = count_index(array[len(q)], q.replace(
                '?', 'a'), q.replace('?', 'z'))
        else:
            result = count_index(
                reversed_array[len(q)], q[::-1].replace('?', 'a'), q[::-1].replace('?', 'z'))
        answer.append(result)
    return answer
