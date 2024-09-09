def calcular_area_rectangulo(base, altura):
    return base * altura

def calcular_area_triangulo(base, altura):
    return (base * altura * 0.5)
4
def principal():
    try:
        base_rectangulo = float(input("Ingrese la base del rectángulo: "))
        altura_rectangulo = float(input("Ingrese la altura del rectángulo: "))

        area_rectangulo = calcular_area_rectangulo(base_rectangulo, altura_rectangulo)
        print(f"Área del rectángulo ({base_rectangulo} x {altura_rectangulo}): {area_rectangulo}")

        base_triangulo = float(input("Ingrese la base del triángulo: "))
        altura_triangulo = float(input("Ingrese la altura del triángulo: "))

        area_triangulo = calcular_area_triangulo(base_triangulo, altura_triangulo)
        print(f"Área del triángulo (0.5 x {base_triangulo} x {altura_triangulo}): {area_triangulo}")

    except ValueError:
        print("Error: por favor, ingrese valores numéricos.")


if __name__ == "__main__":
    principal()
