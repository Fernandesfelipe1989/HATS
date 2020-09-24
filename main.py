def converter_to_base(S, b, k):
    number_in_new_base = []
    # TOD0: Avisar o usuário quando a base é insuficiente?
    for i in (S):
        div = i
        converter =''
        while len(converter) < k:
            if div != 0:
                converter = str(div % b) + converter
                div = div // b
            else:
                converter = "0"+ converter

        number_in_new_base.append(converter)

    return number_in_new_base


def base_sum(number):
    for i in number:
        for a in i:
            pass
        pass
    pass


def main():
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

    print(converter_to_base(S, b, k))

if __name__ == "__main__":
    main()

