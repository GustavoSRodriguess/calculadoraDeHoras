def converter_massa_lunar(massa_terrestre):
    return massa_terrestre / 6

def converter_massa_marte(massa_terrestre):
    gravidade_terrestre = 9.81
    gravidade_marte = 3.71
    return (gravidade_terrestre / gravidade_marte) * massa_terrestre

def calculadora():

    massa_terrestre = float(input("Insira a massa em quilogramas na Terra: "))

    massa_lunar = converter_massa_lunar(massa_terrestre)
    massa_marte = converter_massa_marte(massa_terrestre)

    print(f"Massa lunar: {massa_lunar:.2f} kg")
    print(f"Massa em Marte: {massa_marte:.2f} kg")

if __name__ == '__main__':
    calculadora()
