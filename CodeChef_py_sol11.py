t= int(input())
for i in range(t):
    a,b= map(int,input().split())
    points_per_test=a//10
    print(points_per_test*b)
