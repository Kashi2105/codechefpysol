t= int(input())
for i in range(t):
    arecons=0
    n=int(input())
    s=input()
    for i in s:
        if i in ('a','e','i','o','u'):
            arecons=0
            continue
        else :
            arecons=arecons+1
            if arecons==4:
                break
    if(arecons>=4):
        print("no")
    else:
        print("yes")
            