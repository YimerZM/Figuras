class Figura:
    # Función para calcular el área de un rectángulo
    def areaDelCuadrado(self, lado1, lado2):
        result = lado1 * lado2
        return result

    # Función para calcular el área de un triángulo
    def g(self, b, h):
        r = 0.5 * b * h
        return r

    # Función principal
    def main(self):
        x = 4
        y = 6
        rect_area = self.areaDelCuadrado(x, y)
        print("Área del rectángulo:", rect_area)

        base = 5
        altura = 8
        tri_area = self.g(base, altura)
        print("Área del triángulo:", tri_area)
if __name__=="__main__":
    figura = Figura()
    figura.main()