def main():
    import math


    max_ = 1000000000
    # max_ = 100**2
    testsCount = int(input())

    erMax = math.ceil(max_**0.5)
    er = [None, False]+[True for i in range(erMax-1)]

    for n in range(1, erMax): 
        if er[n]: 
            for nPrime in range(2*n, erMax, n): er[nPrime] = False

    for test in range(testsCount):
        start, end = tuple(map(int, input().split(' ')))

        primes = [True for i in range(end-start+1)]
        testMax = math.ceil(end**0.5)

        for n in range(1, testMax):
            if er[n]:
                nStart = max(n*2, start if start%n == 0 else start-(start%n)+n)

                for nPrime in range(nStart, end+1, n):
                    primes[nPrime-start] = False

        for n in range(start, end+1):
            if primes[n-start] and n != 1:
                print(n)

        if test < testsCount-1:
            print('')

        



if __name__ == "__main__":
    main()