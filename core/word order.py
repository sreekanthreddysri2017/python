from collections import OrderedDict
N=int(input())
wrds=OrderedDict()
for _ in range(N):
    wrd=input()
    wrds[wrd] = wrds.get(wrd,0)+1
print(f'{len(wrds)}')
print(*wrds.values())