def main():
    def transform(exp):
        newExp = None

        if exp[0] != '(':
            newExp = exp
        else:
            exp = exp[1:-1]

            left = None
            right = None
            op = None

            l = 0
            innerExp = ''

            for char in exp:
                if char == '(': l += 1
                elif char == ')': l -= 1

                if l == 0:
                    if char in list('+-*/^'):
                        op = char
                        left = innerExp
                        innerExp = ''
                    else:
                        innerExp += char
                else:
                    innerExp += char

            right = innerExp

            newExp = transform(left)+transform(right)+op

        return newExp


    testsCount = int(input())

    for test in range(testsCount):
        exp = input()

        print(transform(exp))



if __name__ == "__main__":
    main()