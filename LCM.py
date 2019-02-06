"""
Created on Wed Feb  6 22:24:17 2019

@author: Srishti Singh
"""
def lcm(a,b):
    z=max(a,b)
    l=[]
    m=[]
    n=[]
    for i in range(1,z+1):
        if a%i==0 and b%i==0:
            l.append(i)
            a=a/i
            b=b/i
        if a%i==0 and b%i!=0:
            m.append(i)
            a=a/i
        if a%i!=0 and b%i==0:
            n.append(i)
            b=b/i
    print(l)
    print(m)
    print(n)
    lm=l+m+n
    print(lm)
    x=1
    for i in lm:
        x=x*i
    return(x)
lcm(12,14) 
