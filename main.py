def converter_to_base(S, b, k):
    number_in_new_base = []
    # TOD0: Avisar o usuário quando a base é insuficiente?
    for i in S:
        div = i
        converter = ''
        while len(converter) < k:
            if div != 0:
                converter = str(div % b) + converter
                div = div // b
            else:
                converter = "0" + converter

        number_in_new_base.append(str(converter))

    return number_in_new_base


def base_sum(number, b):
    result = ''
    overflow = 0
    for a in range(len(number[0])):
        first = number[0][-a - 1]
        second = number[1][-a - 1]
        sum = int(number[0][-a - 1]) + int(number[1][-a - 1]) + overflow
        if sum > (b - 1):
            sum -= b
            overflow = 1
        else:
            overflow = 0
        result = str(sum) + result
    return result


def base_mul(number, b):
    number_mult = []
    overflow = 0
    sum = 0
    for a in range(len(number[0])):
        result = ''
        j = int(number[0][-a - 1])
        for c in range(len(number[1])):
            d = int(number[1][-c - 1])
            sum = (j * pow(b, a) ) * d + overflow
            overflow = sum//b
            sum = sum % b
            #if sum > (b - 1):
            #    overflow = sum//b
            #    sum = sum%b
                    #sum -= b
                    #overflow += 1
            #else:
            #    overflow = 0
            #if c != len(number[1])-1:
            result = str(sum) + result
            #else:
            #    result = str(overflow) + result
        number_mult.append(result)

    return base_sum(number_mult, b)


def input_data():
    while True:
        try:
            n = int(input("Insert the space number: "))
            break
        except:
            print('Invalid input!')

    while True:
        try:
            k = int(input("Insert the number of pile of stones: "))
            break
        except:
            print('Invalid input!')
    S = []
    for i in range(n):
        s = int(input(f'Insert the number {i + 1}: '))
        try:
            S.append(s)
        except:
            print('Invalid input!')

    while True:
        try:
            b = int(input("Insert base: "))
            break
        except:
            print('Invalid input!')
    return S, b, k


def model():
    S, b, k = input_data()
    print(converter_to_base(S, b, k))


def test():
    b = 8
    k = 8
    n = converter_to_base([4, 5], b, k)
    print(n)
    first = base_sum(n, 10)
    print(first)
    second = converter_to_base([1000], b, k)
    second.append(first)
    print(second)
    result = base_sum(second, b)
    print(result)
    print(n)
    mult= base_mul(n, b)
    print(mult)


def main():
    # model()
    test()


if __name__ == "__main__":
    main()
