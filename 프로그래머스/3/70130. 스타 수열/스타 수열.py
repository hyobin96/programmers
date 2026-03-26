def solution(a):
    arr_length = len(a)
    # 교집합의 원소를 정했을 때 해당하는 집합
    select_element_arr = [[] for _ in range(arr_length + 1)]
    
    for i in range(arr_length - 1):
        first_element = a[i]
        second_element = a[i + 1]
        
        if first_element == second_element:
            continue
        
        select_first_arr = select_element_arr[first_element]
        if not select_first_arr:
            select_first_arr.append(i + 1)
        elif select_first_arr[-1] < i:
            select_first_arr.append(i + 1)
        
        select_second_arr = select_element_arr[second_element]
        if not select_second_arr:
            select_second_arr.append(i + 1)
        elif select_second_arr[-1] < i:
            select_second_arr.append(i + 1)
            
            
    max_length = 0
    for arr in select_element_arr:
        max_length = max(max_length, len(arr) * 2)
    
    answer = max_length
    return answer