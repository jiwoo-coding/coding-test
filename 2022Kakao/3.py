# 3번
import numpy as np

def calculation(fees, m):
    if m<fees[0]:
        return fees[1]
    return fees[1]+np.ceil((m-fees[0])/fees[2])*fees[3]
    
def hourtomin(string):
    h=int(string[:2])
    m=int(string[3:])
    return h*60+m
    
def solution(fees, records):
    answer = []
    cars={}
    cars_index={}
    cars_re={}
    for st in records:
        H, NUM, CH=st.split()
        NUM=int(NUM)
        cars_index[NUM]=CH
        if NUM not in cars.keys(): # 최초 입차
            cars[NUM]=hourtomin(H)
            cars_re[NUM]=0
        elif cars_index[NUM]=="OUT": # 출차
            cars_re[NUM]+=hourtomin(H)-cars[NUM]
        else: # 중복 입차
            cars[NUM]=hourtomin(H)
            
    for NUM in cars: # 마감까지 안나간경우
        if cars_index[NUM]=="IN":
            cars_re[NUM]+=hourtomin('23:59')-cars[NUM]
            
    for NUM in cars_re: # 가격 계산
        cars_re[NUM]=calculation(fees, cars_re[NUM])
        
    for n, result in sorted(cars_re.items(), key=lambda x:x[0]):
        answer.append(int(result))
        
    return answer
