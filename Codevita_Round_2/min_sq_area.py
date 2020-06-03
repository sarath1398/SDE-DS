for _ in range(int(input())):
    
    n= int(input())
    x,y=[],[]
    
    for i in range(n):    
        co_ord=list(map(int,input().split()))
        x.append(co_ord[0])
        y.append(co_ord[1])
        
    x2,x1=max(x),min(x)
    y2,y1=max(y),min(y)
    l1=x2-x1
    l2=y2-y1
    
    print(l1*l2)
