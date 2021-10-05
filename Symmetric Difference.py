count =int(input())
a = set(map(int,input().split()))
count2 = int(input())
b = set(map(int,input().split()))
sym = sorted(list(a.union(b)-a.intersection(b)))
for i in sym:
    print(i)
