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
        sum = 0
        for c in range(len(number)):
            sum += int(number[c][-a - 1])
        sum += overflow
        overflow = sum // b
        div = sum % b
        #first = number[0][-a - 1]
        #second = number[1][-a - 1]
        #sum = int(number[0][-a - 1]) + int(number[1][-a - 1]) + overflow
        #if sum > (b - 1):
         #   sum -= b
         #   overflow = 1
        #else:
         #   overflow = 0
        result = str(div ) + result
    return result


def base_mul(number, b):
    number_mult = []
    overflow = 0
    for a in range(len(number[0])):
        result = ''
        for c in range(len(number[1])):
            sum = ((int(number[0][-a - 1])) * pow(b, a)) * (int(number[1][-c - 1])) + overflow
            overflow = sum//b
            div = sum % b
            result = str(div) + result
        number_mult.append(result)

    return base_sum(number_mult, b)


def convert_base_to_base(n, bi, bf):
    number_base = []
    for a in range(len(n)):
        sum = 0
        for c in range(len(n[a])):
            sum += int(n[a][-c -1])*pow(bi, c)
        number_base.append(sum)
    return converter_to_base(number_base, bf, len(n[0]))


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
    b = 10
    k = 2
    n = converter_to_base([5, 5], b, k)
    print(n)
    first = base_sum(n,  b)
    print(first)
    #second = converter_to_base([1000], b, k)
    #second.append(first)
    #print(second)
    #result = base_sum(second, b)
    #print(result)
    #print(n)
    mult= base_mul(n, b)
    print(mult)
    convert = convert_base_to_base(['0011001000', '1111101000'], 2, 3)
    print(convert)


def main():
    # model()
    test()


if __name__ == "__main__":
    main()
