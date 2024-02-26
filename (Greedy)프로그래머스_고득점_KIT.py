# 체육복
def solution(n, lost, reserve):
    total = {var:1 for var in range(1,n+1)} # 기본 딕셔너리에 학생들은 모두 체육복이 한 개씩 있다고 가정
    for arg in lost: # 안가지고 온 학생
        total[arg] = 0
    for arg in reserve: # 여벌이 있는 학생
        total[arg] += 1
    
    for arg in total.keys(): # 케이스 별 구분하여 분배(좌,우 학생 만 작업 대상!)
        if arg == 1:
            if total[arg] > 1 and total[arg+1] == 0:
                total[arg+1] = 1
                total[arg] -=1
                
        elif arg == n:
            if total[arg] > 1 and total[arg-1] == 0:
                total[arg-1] = 1
                total[arg] -=1
        else:
            if total[arg] > 1 and total[arg-1] == 0:
                total[arg-1] = 1
                total[arg] -= 1
                
            elif total[arg] > 1 and total[arg+1] == 0:
                total[arg+1] = 1
                total[arg] -= 1
                
    tmp = [n for n in total.values() if n >= 1 ]         
    answer = len(tmp)
    return answer

# 