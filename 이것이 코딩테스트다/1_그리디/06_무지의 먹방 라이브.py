# https://programmers.co.kr/learn/courses/30/lessons/42891?language=python3

## 내 풀이: 정확성 테스트 O, 효율성 테스트 X
def solution(food_times, k):
    N = len(food_times)
    count = 0
    zeros_index = [] # 값이 0인 index들
    not_zero_list = [i for i in range(N)]
    for i, time in enumerate(food_times):
        if time == 0:
            zeros_index.append(i)
            not_zero_list.remove(i)
    
    index = 0 # 현재 index
    min_index = 0 # 다시 앞으로 돌아갈 대상의 index 
    max_index = N-1 # 앞으로 돌아가는 시점의 index
    while True:
        # while index in zeros_index:
            # if index == max_index:
            #     index = min_index
            # else:
            #     index += 1
        
        food_times[index] -= 1
            
        if food_times[index] == 0:
            zeros_index.append(index)
            zeros_index.sort()
            cur_index = not_zero_list.index(index)
            not_zero_list.remove(index)
            if not_zero_list == []: 
                if count == k:
                    print(index + 1)
                    return index + 1
                else:
                    return -1
        
            if index == min_index:
                min_index = not_zero_list[0]
                
            elif index == max_index:
                max_index = not_zero_list[-1]
                
        if count == k:
            print(index + 1)
            return index + 1
        
        count += 1
        if index >= max_index:
            index = min_index
        else:
            if index in not_zero_list:
                cur_index = not_zero_list.index(index)
                index = not_zero_list[cur_index + 1]
            else:
                index = not_zero_list[cur_index]      
        
        if food_times == [0]*N: 
            break
    
    return -1

## 예시 답안
import heapq

def solution(food_times, k):
    # 전체 음식을 먹는 시간보다 k가 크거나 같다면 -1
    if sum(food_times) <= k:
        return -1

    # 시간이 작은 음식부터 빼야 하므로 우선순위 큐를 이용
    q = []
    for i in range(len(food_times)):
        # (음식 시간, 음식 번호) 형태로 우선순위 큐에 삽입
        heapq.heappush(q, (food_times[i], i + 1))  

    sum_value = 0 # 먹기 위해 사용한 시간
    previous = 0 # 직전에 다 먹은 음식 시간
    length = len(food_times) # 남은 음식의 개수

    # sum_value + (현재의 음식 시간 - 이전 음식 시간) * 현재 음식 개수와 k 비교
    while sum_value + ((q[0][0] - previous) * length) <= k:
        now = heapq.heappop(q)[0]
        sum_value += (now - previous) * length
        length -= 1 # 다 먹은 음식 제외
        previous = now # 이전 음식 시간 재설정

    # 남은 음식 중에서 몇 번째 음식인지 확인하여 출력
    result = sorted(q, key=lambda x: x[1]) # 음식의 번호 기준으로 정렬
    return result[(k - sum_value) % length][1]