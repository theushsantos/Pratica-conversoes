#Modulo de conversões

#Converter celsius para fahrenheit
def celsius_to_fahrenheit(c):
    return 9 * c / 5 + 32

#Converter fahrenheit para celsius
def fahrenheit_to_celsius(f):
    return 5 * (f - 32) / 9

#Converter celsius para kelvin
def celsius_to_kelvin(c):
    return c + 273

#Converter kelvin para celsius
def kelvin_to_celsius(k):
    return 273 - k

#Conversores de volume

#Litros para galões

def litros_to_galoes(l):
    return l * 0.264172

#Galões para litros
def galoes_to_litros(g):
    return g * 3.78541
