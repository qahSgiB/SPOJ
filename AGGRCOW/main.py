def main():
    testCases = int(input())

    for test in range(testCases):
        nsCount, needed = map(int, input().split(' '))
        ns = list(sorted([int(input()) for _ in range(nsCount)]))

        maxMaxDist = (ns[-1]-ns[0])//(needed-1)
        maxDist = None

        start = 0
        end = maxMaxDist+1

        while True:
            testMaxDist = start+(end-start)//2

            last = ns[0]
            count = 1
            ok = False

            for n in ns:
                if n-last >= testMaxDist:
                    last = n
                    count += 1
            
                if count == needed:
                    ok = True
                    break

            if ok:
                better = False

                if maxDist == None: better = True
                else:
                    if testMaxDist > maxDist: better = True
                
                if better:
                    maxDist = testMaxDist

                start = testMaxDist
            else:
                end = testMaxDist

            if end-start <= 1: break

        print(maxDist)



if __name__ == "__main__":
    main()