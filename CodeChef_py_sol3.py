T=int(input())
for i in range(T):
    s=input()
    (X,Y,A)=map(int,s.split())
    if A>=X and A<Y :
        print("YES")
    else:
        print("NO")
    