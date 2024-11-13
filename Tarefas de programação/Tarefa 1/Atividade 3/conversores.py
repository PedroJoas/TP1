def celsius_para_fahrenheit(celsius):
    fahrenheit = 32 + (celsius * (9/5))
    return fahrenheit

def fahrenheit_para_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * (5/9)
    return celsius

def metro_para_pes(metro):
    pes = metro * 3.281
    return pes

def pes_para_metro(pes):
    metro = pes / 3.281
    return metro

def quilometro_para_milhas(km):
    milhas = km / 1.609
    return milhas

def milhas_para_quilometro(milhas):
    km = milhas * 1.609
    return km

def dia_para_horas(dia):
    horas = dia * 24
    return horas