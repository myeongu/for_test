# https://programmers.co.kr/learn/courses/30/lessons/60057

## 답안 예시
def solution(s):
    answer = len(s)
    # 1개 단위(step)부터 압축 단위를 늘려가며 확인
    for step in range(1, len(s) // 2 + 1):
        compressed = ""
        prev = s[0:step] # 앞에서부터 step만큼의 문자열 추출
        count = 1
        # 단위(step) 크기만큼 증가시키며 이전 문자열과 비교
        for j in range(step, len(s), step):
            # 이전 상태와 동일하다면 압축 횟수(count) 증가
            if prev == s[j:j + step]:
                count += 1
            # 다른 문자열이 나왔다면(더 이상 압축하지 못하는 경우라면)
            else:
                compressed += str(count) + prev if count >= 2 else prev
                prev = s[j:j + step] # 다시 상태 초기화
                count = 1
        # 남아있는 문자열에 대해서 처리
        compressed += str(count) + prev if count >= 2 else prev
        # 만들어지는 압축 문자열이 가장 짧은 것이 정답
        answer = min(answer, len(compressed))
    return answer


## 이전에 풀었던 풀이
'''def length_out(L):
    str_length = 0
    for each in L:
        if each[1] == 1:
            str_length += len(each[0])
        else:
            str_length += len(each[0]) + len(str(each[1]))
    return str_length

def solution(s):
    n = len(s) # 문자열 길이
    answer = n # 최종답: 문자열 길이
    
    for i in range(1, n//2+1):
        divided_num = n//i if n % i == 0 else n//i + 1

        str_before = ''
        str_list = []
        for j in range(divided_num):
            str_temp = s[j * i : j * i + i]
            if str_before != str_temp:
                str_list.append([str_temp, 1])
            else:
                str_list[-1][-1] += 1
            str_before = str_temp
        # print(str_list)
        
        length = length_out(str_list)
        answer = min(answer, length)
        
    print(answer)
        
    return answer'''

## 이번에 푼 풀이
'''
def length_out(s, n):
    div, rest = len(s) // n, len(s) % n
    result = 0
    count = 0
    before_s = s[0:n]
    for i in range(div):
        temp_s = s[i*n:(i+1)*n]
        if before_s == temp_s:
            count += 1
            continue
        else:
            if count != 1:
                result += len(str(count) + before_s)
            else:
                result += len(before_s)
            before_s = temp_s
            count = 1
    if count == 1:
        result += rest + n
    else:
        result += len(str(count) + temp_s) + rest
    return result
                

def solution(s):
    length = len(s)
    result = 9999
    for i in range(1, length//2 + 1):
        temp_length = length_out(s, i)
        result = min(result, temp_length)
    print(result)
    return result
'''