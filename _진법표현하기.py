#진법 표현하는 방법 (2~10진법 까지만..)
import sys
input=sys.stdin.readline

def jinbub(string_num, x, k):
    num=str(x%k)
    if x>=k:
        string_num+=jinbub(string_num,x//k,k)
    string_num+=num
    return string_num

if __name__=='__main__':
    n, k=list(map(int, input().split()))
    string_num=jinbub('',n,k)
    
    print(string_num)
