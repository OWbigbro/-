# 폰켓몬
def solution(nums):
    unique_poketmon = len(set(nums))
    max_poketmon = len(nums)//2
    if unique_poketmon > max_poketmon:
        answer = max_poketmon
    else:
        answer = unique_poketmon
    return answer

# 완주하지 못한 선수
def solution(participant, completion):
    parti_dict = {val:0 for val in participant}
    for arg in participant:
        parti_dict[arg] += 1
    for arg in completion:
        parti_dict[arg] -= 1
        
    answer_list = [val for val in parti_dict.keys() if parti_dict[val] > 0]

    answer = answer_list[-1]
    return answer

# 전화번호 목록 - sort 후 for문(구현)
# sort한다면 앞뒤로 정렬되어 앞의 것과 뒤의 것이 접두사 관계가 아니라면
# 그 이후로 역시 접두사 관계가 없다!
# sort 전 - ["12","567","88","123","1235"]
# sort 후 - ['12', '123', '1235', '567', '88']
def solution(phone_book):
    answer = True
    phone_book.sort()
    
    for idx,arg in enumerate(phone_book):
        if arg == phone_book[-1]:
            continue
        if arg == phone_book[idx+1][:len(arg)]:
            return False
    return answer

# 전화번호 목록 - 해시

# 의상 - 해시
def solution(clothes):
    # ---
    prod_count = len(clothes)
    dict_val = {arg:0 for prod,arg in clothes}
    for prod,arg in clothes:
        dict_val[arg] += 1
    unique_prod = len(dict_val.keys())
    # ---
    if unique_prod > 1:
        tmp = 1
        for arg in dict_val.values():
            tmp *= (arg+1) # 해당 의상 종류를 입지 않은 경우 
            # A(N 개) B(M 개)
            # (N+1)(M+1) = NM + N + M + 1
        answer = tmp -1
    else:   
        answer = prod_count
    return answer
