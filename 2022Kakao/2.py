#2번
import math
def jinbub(string_num, x, k):
    num=str(x%k)
    if x>=k:
        string_num+=jinbub(string_num,x//k,k)
    string_num+=num
    return string_num

def Isprime(x):
    if x<=1:
        return 0
    for i in range(2,int(math.sqrt(x))+1):
        if x%i==0:
            return 0
    return 1

def solution(n, k):
    answer = 0
    string_num=jinbub('',n,k)
    number=''
    for i in range(len(string_num)):
        if int(string_num[i])==0:
            if len(number)>0:
                if Isprime(int(number)):
                    answer+=1
            number=''
            continue
        number+=string_num[i]
    if len(number)>0:
        if Isprime(int(number)):
            answer+=1
        
    return answer
