def convert_2_to_6(n):
    convert_6 = []
    k = 3
    overflow = 0
    qnt = len(n)
    for i in n:
        result = ''
        c = len(i)//k
        d = len(i)
        for a in range(0, len(i)//k, k):
            first = int(i[-a-1]) * pow(2, 0)
            second = int(i[-a-2]) * pow(2, 1)
            third = int(i[-a-3]) * pow(2, 2)
            sum = first + second + third + overflow
            div = sum % 6
            overflow = sum // 6
            result = str(div) + result
        convert_6.append(result)
    return convert_6


def convert_6_to_3():
    pass


def test():
    n = ['000', '001', '010', '011', '100', '101', '110', '111']
    print(convert_2_to_6(n))


def model():
    pass


def main():
    test()
    # model()


if __name__ == "__main__":
    main()
