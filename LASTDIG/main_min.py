muls = [[2,4,8,6],[3,9,7,1],[4,6],[5],[6],[7,9,3,1],[8,4,2,6],[9,1]]
testsCount = int(input())
for _ in range(testsCount):
    a, b = list(map(int, input().split(' ')))
    a %= 10
    lastDig = None
    if a == 0: lastDig = 0
    elif a == 1: lastDig = 1
    else:
        if b == 0: lastDig = 1
        else:
            lastDigs = muls[a-2]
            lastDigIndex = (b-1)%len(lastDigs)
            lastDig = lastDigs[lastDigIndex]
    print(lastDig)