from itertools import combinations
n = int(input())
lett = input().split()
k = int(input())
count_a = lett.count("a")
comb = list(combinations(lett, k))
cont = 0
for i in comb:
    if "a" in i:
        cont += 1
print(cont/len(comb))