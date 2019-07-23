def main():
    testsCount = int(input())

    for test in range(testsCount):
        n = list(map(int, list(input())))
        nPalin = None

        if len(n) == 1:
            if n[0] < 9:
                nPalin = [n[0]+1]
            else:
                nPalin = [1, 1]
        elif len(n)%2 == 1:
            half = (len(n)-1)//2

            left = n[:half]
            middle = n[half]
            right = n[(half+1):]

            leftIsHigher = False

            for index in range(len(left)-1, -1, -1):
                leftN = left[index]
                rightN = right[-index-1]

                if leftN != rightN:
                    leftIsHigher = leftN > rightN
                    break

            if leftIsHigher:
                nPalin = left+[middle]+list(reversed(left))
            else:
                if int(middle) < 9:
                    nPalin = left+[middle+1]+list(reversed(left))
                else:
                    allNines = True

                    for index in range(len(left)-1, -1, -1):
                        leftN = left[index]

                        if leftN < 9:
                            left[index] = leftN+1
                            allNines = False
                        else:
                            left[index] = 0

                        if not allNines:
                            break

                    if allNines:
                        nPalin = [1]+[0 for i in range(len(n)-1)]+[1]
                    else:
                        nPalin = left+[0]+list(reversed(left))
        else:
            half = len(n)//2

            left = n[:half]
            right = n[half:]

            leftIsHigher = False

            for index in range(len(left)-1, -1, -1):
                leftN = left[index]
                rightN = right[-index-1]

                if leftN != rightN:
                    leftIsHigher = leftN > rightN
                    break

            if leftIsHigher:
                nPalin = left+list(reversed(left))
            else:
                allNines = True

                for index in range(len(left)-1, -1, -1):
                    leftN = left[index]

                    if leftN < 9:
                        left[index] = leftN+1
                        allNines = False
                    else:
                        left[index] = 0

                    if not allNines:
                        break

                if allNines:
                    nPalin = [1]+[0 for i in range(len(n)-1)]+[1]
                else:
                    nPalin = left+list(reversed(left))

        print(''.join(map(str, nPalin)))



if __name__ == "__main__":
    main()