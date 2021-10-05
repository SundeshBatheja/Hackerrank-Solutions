# Enter your code here. Read input from STDIN. Print output to STDOUTimport itertools
 
import itertools
def findsubsets(s, n):
    return list(itertools.combinations(s, n))
 
# Driver Code
l=input()
n, y = [int(x) for x in input().split()] 
lis = []
lis3=[]
def test_prime(n):
    if (n==1):
        return False
    elif (n==2):
        return True;
    else:
        for x in range(2,n):
            if(n % x==0):
                return False
        return True
for i in range(2,n+1):
    if test_prime(i)==True:
        lis.append(i)
for i in range(2,y+1):
    if test_prime(i)==True:
        lis3.append(i)
lis4 = []
lis2 = []
for i in range(1,len(lis3)+1):
    sub = findsubsets(lis3, i)
    lis4.extend(sub)
f=[]
for i in lis4:
    if test_prime(sum(i))==True:
        f.append(i)

for i in range(1,len(lis)+1):
    sub = findsubsets(lis, i)
    lis2.extend(sub)
d=[]
for i in lis2:
    if test_prime(sum(i))==True:
        d.append(i)
print(len(d),len(f))    
    
    
    
        
        
