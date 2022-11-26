import conversoes

def linha():
    return print("---------------------------------")

def mostra_valores(c,f,l,g,k):

    linha()
    print("Converções de Temperatura")
    linha()
    print(f'Celsius para Fahrenheit: {conversoes.celsius_to_fahrenheit(c)}')
    print(f'Fahrenheit para Celsius: {conversoes.fahrenheit_to_celsius(f)}')
    print(f'Celsius para kelvin: {conversoes.celsius_to_kelvin(c)}')
    print(f'Kelvin para celsius: {conversoes.kelvin_to_celsius(k)}')
    linha()
    print(f'Conversão de volume')
    linha()
    print(f'Litro para galão: {conversoes.litros_to_galoes(l)}')
    print(f'Galão para litro: {conversoes.galoes_to_litros(g)}')
    linha()

linha()
celsius = float(input("Digite o valor de celsius: " ))
fahrenheit = float(input('Digite o valor de fahrenheit: '))
litro = float(input("Digite o valor de litro: "))
galão = float(input("Digite o valor de galão: "))
kelvin = float(input("Digite o valor em kelvin: "))
linha()

mostra_valores(celsius,fahrenheit,litro,galão,kelvin)