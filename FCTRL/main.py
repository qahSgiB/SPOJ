def main():
    testsCount = int(input())

    for test in range(testsCount):
        n = int(input())

        nEnd = True
        p = 1
        zeros = 0

        while nEnd:
            f = 5**p

            if f > n: nEnd = False
            else: zeros += n//f

            p += 1

        print(zeros)


if __name__ == "__main__":
    main()