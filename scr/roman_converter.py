def roman_to_decimal(roman):
    resultado = 0
    for letra in roman:
        if letra == 'I':
            resultado += 1
        if letra == 'V':
            resultado += 5
    return resultado
