t=int(input())
songs=[]
fsongs=[]
for i in range(t):
    s=[]
    n,k,l=map(int,input().split())
    for j in range(1,n+1):
        D=dict.fromkeys(['m','l'])
        D['m'],D['l']=map(int,input().split())
        songs.append(D)
        if(songs[j-1]['l']==l):
            fsongs.append(songs[j-1])
            s.append(int(songs[j-1]['m']))
    s.sort(reverse=True)        
    if(k < len(fsongs) and len(fsongs)!=0):
        for i in range(len(fsongs)-k):
             s.pop()
        print(sum(s))
    elif k>=len(fsongs) and len(fsongs)!=0:
        print(sum(s))
               
    else:
        print(-1)
    songs.clear()
    fsongs.clear()