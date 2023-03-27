T = int(input())
for _ in range(T):
    n = int(input())
    blocks = list(map(int, input().split()))
    c = -1
    fail = False
    while len(blocks) > 0:
        if blocks[0] > blocks[-1]:
            b = blocks.pop(0)
        else:
            b = blocks.pop(-1)

        if c == -1 or b <= c:
            c = b
        else:
            print("No")
            fail = True
            break

    if not (fail):
        print("Yes")