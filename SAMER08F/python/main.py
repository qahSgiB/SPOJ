def main():
    n = None

    while n != 0:
        n = int(input())

        if n != 0: print((n*(n+1)*(2*n+1))//6)



if __name__ == "__main__":
    main()