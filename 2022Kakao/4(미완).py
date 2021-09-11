# 4
def checkscore(info, arr, N, k):
    j=0
    score=0
    for sc in range(10,0,-1):
        if arr[j]!=k and N>0:
            score+=j*sc
            N-=1
        j+=1
    return score

def RvsA(info, N, lo):
    R_score={}
    for i in range(N,info[lo],-1):
        num=N-i
        cnt=num
        while num>0:
            t=cnt
            arr=[0 for i in range(11)]
            arr[lo]=1
            ch=lo+1
            for k in range(ch,len(info)):
                if i>info[k]:
                    arr[k]=1
                    t-=num
                    if t==0: break
            #diff_sc=checkscore(info, arr, N, 1) - checkscore(info, arr, N, 0)
            #if R_score[i]<diff:
            #    R_score[i]=diff
            num-=1
    return R_score

def solution(n, info):
    answer = [0 for i in range(11)]
    for i in range(len(info)):
        R_score=RvsA(info, n, i)
        #result=sorted(R_score.items, key=lambda x:x[1], reverse=True)
        #answer[i]=result[0][0]
    for i in range(1,11):
        if n==i:
            if info[0]==i:
                answer=[-1]
    return answer
