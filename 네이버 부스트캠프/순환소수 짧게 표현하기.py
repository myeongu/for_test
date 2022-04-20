## [SW Expert Academy] 3501. 순환소수 짧게 표현하기
## [입력]
# 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
# 각 테스트 케이스의 첫 번째 줄에는 두 자연수 p, q(1 ≤ p, q ≤ 105) 가 주어진다.
# 이는 p/q를 소수로 표현해야 함을 의미한다.

## [출력]
# 각 테스트 케이스마다 p/q를 소수로 표현하여 출력한다.

def is_circulated(p, q):
    while q % 2 == 0 or q % 5 == 0:
        if q % 2 == 0:
            q = q // 2
        if q % 5 == 0:
            q = q // 5
    
    if p % q == 0:
        return True
    
    return False

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    p, q = map(int, input().split())

    if is_circulated(p, q):
        result = p / q if p / q != p // q else int(p/q)
        print(result)
    
    else:
        check_dict = {}
        num = p // q
        p = p - num
        count = 0
        
        while True:
            p = p * 10
            div = p // q
            rest = p % q

            if (div, rest) in check_dict.values():
                break

            check_dict[count] = (div, rest)

            count += 1
            p = rest
        print(check_dict)

        result = str(num) + '.' if num != 0 else '0.'
        for i in check_dict.keys():
            if check_dict[i] == (div, rest):
                result += '(' + str(check_dict[i][0])
            else:
                result += str(check_dict[i][0])

        result += ')'
        print(result)

    # ///////////////////////////////////////////////////////////////////////////////////