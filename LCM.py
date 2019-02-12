"""
Created on Wed Feb  6 22:24:17 2019

@author: Srishti Singh
"""

def lcm(num1,num2):
    maxnum=max(num1,num2)
    l=[]
    m=[]
    n=[]
    for i in range(1,maxnum+1):
        if num1%i==0 and num2%i==0:
            l.append(i)
            num1=num1/i
            num2=num2/i
        if num1%i==0 and num2%i!=0:
            m.append(i)
            num1=num1/i
        if num1%i!=0 and num2%i==0:
            n.append(i)
            num2=num2/i
    print("Common factors of Number 1 and Number 2:",l)
    print("Remaining factors of Number 1:",m)
    print("Remaining factors of Number 2:",n)
    lm=l+m+n
    print(lm)
    x=1
    for i in lm:
        x=x*i
    return(x)
number1=int(input("Enter First Number: "))
number2=int(input("Enter Second Number: "))
print("Your LCM is=",lcm(number1,number2))

