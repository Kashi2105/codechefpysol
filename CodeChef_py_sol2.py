T=int(input())
l=[None]*T
for i in range(0,T):
    s=input()
    j=s.split()
    l[i]={'Chef':int(j[0]),'Chefina':int(j[1])}
for i in range(0,T):
    if l[i]['Chef']+l[i]['Chefina'] in range(1,7):
      print("NO")
    else:
        print("YES")
 
