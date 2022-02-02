# 주차요금계산
# https://programmers.co.kr/learn/courses/30/lessons/92341

def solution(fees, records):
    basic_time, basic_fee, plus_time, plus_fee = fees
    
    def money(t):
        result = 0
        if t > basic_time:
            result += basic_fee
            t -= basic_time
            
            if t % plus_time == 0:
                extra = t // plus_time
            else:
                extra = t // plus_time + 1
            
            result += plus_fee * extra
            
        elif t <= basic_time:
            result = basic_fee
        
        return result
    
    time_each = {}
    time_in = {}
    
    for record in records:
        time, car, status = record.split()
        if status == "IN":
            time_in[car] = time
        elif status == 'OUT':
            hour = int(time[:2]) - int(time_in[car][:2])
            minute = int(time[3:]) - int(time_in[car][3:])
            total = 60*hour + minute
            try:
                time_each[car] += total
            except:
                time_each[car] = total
            del time_in[car]
    
    if time_in != {}:
        for car, time in time_in.items():
            hour = 23 - int(time[:2])
            minute = 59 - int(time[3:])
            total = 60*hour + minute
            try:
                time_each[car] += total
            except:
                time_each[car] = total
    
    answer = []
    for car in sorted(time_each):
        total_time = int(time_each[car])
        answer.append(money(total_time))
    print(answer)
    return answer