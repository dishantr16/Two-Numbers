for _ in range(int(input())):
    a,b,n=map(int,input().split(" "))
    i=1
    while i<=n:
        if i&1==1:
            a*=2
        else:
            b*=2
        i+=1
    x=max(a,b)
    y=min(a,b)
    print(x//y)