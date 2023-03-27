n, m = input().split()
array = list(map(int,input().split()))
ma = set(map(int,input().split()))
mb = set(map(int,input().split()))
h=0
for i in array:
    if i in ma:
        h +=1
for i in array:
    if i in mb:
        h -=1
print(h)