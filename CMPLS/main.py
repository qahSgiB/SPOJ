def main():
    testsCount = int(input())

    for test in range(testsCount):
        _, toPrintCount = list(map(int, input().split(' ')))
        numbers = list(map(int, input().split(' ')))

        diffsCalc = [numbers]

        nEnd = True
        while nEnd:
            lastDiff = diffsCalc[-1]

            if all(map(lambda n: n == 0, lastDiff)):
                nEnd = False
            elif len(lastDiff) == 1:
                diffsCalc.append([0])
                nEnd = False
            else:
                newDiff = [lastDiff[index+1]-lastDiff[index] for index in range(len(lastDiff)-1)]
                diffsCalc.append(newDiff)

        diffs = [[diffsCalc[diffIndex][-1]] for diffIndex in range(len(diffsCalc))]

        for _ in range(toPrintCount):
            diffs[-1].append(0)

            for diffIndex in range(len(diffs)-2, -1, -1):
                diffs[diffIndex].append(diffs[diffIndex][-1]+diffs[diffIndex+1][-1])

        toPrint = diffs[0][1:]
        print(' '.join(map(str, toPrint)))



if __name__ == "__main__":
    main()