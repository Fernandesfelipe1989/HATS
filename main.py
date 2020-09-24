def converter_to_base(S, b, k):
    number_in_new_base = []
    # TOD: Avisar o usuário quando a base é insuficiente?
    for i in (S):
        div = i
        flag_converter = True
        # print(i)
        converter =''
        while len(converter) < k:
            if div != 0:
                converter = str(div % b) + converter
                div = div // b
            else:
                converter = "0"+ converter

        number_in_new_base.append(converter)

    return number_in_new_base

print(converter_to_base([9, 30], 3, 2))


