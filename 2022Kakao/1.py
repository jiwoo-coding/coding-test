# 1
def solution(id_list, report, k):
    dic={}
    dic_re={}
    for key in id_list:
        dic[key]=[]
        dic_re[key]=0
    for name in report:
        temp=name.split()
        if temp[1] not in dic[temp[0]]:
            dic[temp[0]].append(temp[1])
            dic_re[temp[1]]+=1
        
    check=[]
    for name in dic_re:
        if dic_re[name]>=k:
            check.append(name)
            
    answer=[ 0 for i in range(len(id_list)) ]
    i=0
    for lst in list(dic.values()):
        for name in lst:
            if name in check:
                answer[i]+=1
        i+=1
    return answer
