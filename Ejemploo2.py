def calcular(a, b, c):
    res = a * b + c
    return res

def principal():
    try:
        a = float(input("Ingrese el valor de 'a': "))
        b = float(input("Ingrese el valor de 'b': "))
        c = float(input("Ingrese el valor de 'c': "))

        resultado = calcular(a, b, c)

        print(f"El resultado de {a} * {b} + {c} es: {resultado}")

    except ValueError:
        print("Error: por favor, ingrese valores numéricos.")


if __name__ == "__main__":
    principal()
