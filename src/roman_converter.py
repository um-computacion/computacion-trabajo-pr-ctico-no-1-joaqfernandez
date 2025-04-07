def roman_to_decimal(roman):
    romanos = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    decimal = 0
    i= 0 

    while i < len(roman):
        if i + 1 < len(roman) and romanos[roman[i]] < romanos[roman[i + 1]]:
            decimal += romanos[roman[i + 1]] - romanos[roman[i]]
            i += 2
        else:
            decimal += romanos[roman[i]]
            i += 1
    return decimal

def main():
    my_roman = input('decime tu romano: ')
    decimal_humano = roman_to_decimal(my_roman)

    print(my_roman + ' -> ' + str(decimal_humano))

