t= int(input())
for i in range(t):
    s=""
    l=[]
    n,k=map(int,input().split())
    S=input().split()
    for z in S:
        l.append(int(z))
    for j in l:
        if j<=k:
            s=s+'1'
            k=k-j
        else:
            s=s+'0'
    print(s)
