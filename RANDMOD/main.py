def main():
    testsCount = int(input())

    for _ in range(testsCount):
        n = int(input())

        ans = 0

        for k in range(n):
            ans += 1/(k+1)

        # if ans%1 == 0: ans = int(ans)

        print(ans)



if __name__ == "__main__":
    main()