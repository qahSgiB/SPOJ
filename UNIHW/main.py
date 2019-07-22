def main():
    from functools import reduce


    testsCount = int(input())
    
    for test in range(testsCount):
        input()

        numbers = list(map(int, input().split(' ')))
        used = [True for i in range(len(numbers))]

        negOne = None
        posOne = None
        onlyOnes = True
        isNeg = False

        for numberIndex in range(len(numbers)):
            number = numbers[numberIndex]

            if number == 0: 
                used[numberIndex] = False
            elif number == 1:
                used[numberIndex] = False
                if posOne == None: posOne = numberIndex
            elif number == -1:
                used[numberIndex] = False
                if negOne == None: negOne = numberIndex
            else:
                onlyOnes = False
                if number < 0:
                    isNeg = not isNeg

        if onlyOnes:
            if posOne != None:
                used[posOne] = True
            else:
                negOneCount = numbers.count(-1)

                if negOneCount >= 2:
                    count = 0

                    for numberIndex in range(len(numbers)):
                        number = numbers[numberIndex] 

                        if number == -1:
                            used[numberIndex] = True
                            count += 1

                        if count >= 2: break
                else:
                    if negOneCount == 1 and len(numbers) == 1:
                        used[0] = True
                    else:
                        for numberIndex in range(len(numbers)):
                            number = numbers[numberIndex] 

                            if number == 0:
                                used[numberIndex] = True
                                break

        else:
            if isNeg:
                if len(numbers) != 1:
                    if negOne != None:
                        used[negOne] = True
                    else:
                        min_ = None
                        minIndex = None

                        for numberIndex in range(len(numbers)):
                            number = numbers[numberIndex]

                            if number < -1:
                                better = False
                                
                                if min_ == None: 
                                    better = True
                                else:
                                    if number >= min_: better = True

                                if better:
                                    min_ = number
                                    minIndex = numberIndex

                        used[minIndex] = False

        out = ''.join(map(lambda n: '1' if n else '0', used))
        print('Case {testIndex}: {out}'.format(testIndex=test+1, out=out))



if __name__ == "__main__":
    main()