def solution(fees, records):
    def to_minutes(time):
        h, m = map(int, time.split(":"))
        return h * 60 + m
    
    def calc_fee(minutes):
        minutes -= fees[0]
        fee = fees[1]
        if minutes > 0:
            fee += (minutes // fees[2]) * fees[3]
            if minutes % fees[2] != 0:
                fee += fees[3]
        return fee
        
    # key = 차 번호, value = 입차 시간
    # map
    # 'OUT' 이면 꺼내서 비용 계ㅅ산
    d = dict()
    total_time = dict()
    answer = []
    for record in records:
        time, number, inout = record.split()
        if inout == 'IN':
            d[number] = to_minutes(time)
            if number not in total_time:
                total_time[number] = 0
        else:
            out_time = to_minutes(time)
            in_time = d[number]
            total_time[number] += out_time - in_time
            del d[number]
        
    
    out_time = to_minutes("23:59")
    for number, in_time in d.items():
        total_time[number] += out_time - in_time
    
    cars_fees = []
    for number, times in total_time.items():
        cars_fees.append((number, calc_fee(times)))
    
    cars_fees.sort()
    answer = [fee for number, fee in cars_fees]
    
    return answer