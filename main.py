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
        result = str(div ) + result
    return result


def base_mul(number_list, b):
    if len(number_list) % 2 != 0:
        even = number_list.pop()
    else:
        even = "1"
    res = base_mul_two_number([number_list[0], number_list[1]], b)
    for a in range(2, len(number_list)):
        res = base_mul_two_number([res, number_list[a]], b)
    res = base_mul_two_number([even, res], b)
    return res


def base_mul_two_number(number, b):
    number_mult = []
    overflow = 0
    for a in range(len(number[0])):
        result = ''
        for c in range(len(number[1])):
            sum = ((int(number[0][-a - 1])) * pow(b, a)) * (int(number[1][-c - 1])) + overflow
            overflow = sum // b
            div = sum % b
            result = str(div) + result
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


def convert_base_to_base(n, bi, bf):
    number_base = []
    for a in range(len(n)):
        sum = 0
        for c in range(len(n[a])):
            sum += int(n[a][-c -1])*pow(bi, c)
        number_base.append(sum)
    return converter_to_base(number_base, bf, len(n[0]))


def test():
    b = 8
    k = 8
    n = converter_to_base([2, 5, 5, 5], b, k)
    print(n)
    first = base_sum(n,  b)
    print(first)
    mult= base_mul(n, b)
    print(mult)
    convert = convert_base_to_base(['0011001000', '1111101000'], 2, 3)
    print(convert)


def main():
    #model()
    test()


if __name__ == "__main__":
    main()
