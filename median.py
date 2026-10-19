a=sorted(list(map(int,input().split())))
l=len(a)
if l%2!=0:
    print(a[l//2])
else:
    print((a[l//2-1]+a[l//2])/2)