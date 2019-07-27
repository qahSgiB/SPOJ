from random import randint



def do(n):
    ans = 0

    while (n > 0):
        ans += 1
        n = randint(0, n-1)

    return ans



n = 4
count = 10**5
avgSum = 0

for i in range(count):
    avgSum += do(n)



print(avgSum/count)