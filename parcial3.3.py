def evaluar(lista):
    resultados = []
    
    for lectura in lista:
        
        
        match lectura:
            case 0:
                resultados.append(f"Alerta: punto de Congelación{lectura}")
            case _ if 1 <= lectura <= 9:
                resultados.append(f"{lectura}Estado:cristico")
            case _ if 10 <= lectura <= 30:
                resultados.append(f"{lectura}Estado: Estable")
            case _ if 30 < lectura < 100:
                resultados.append(f"{lectura}:Estado: Critico")
            case 100:
                resultados.append(f"{lectura}Alerta: punto de Ebullición")
            case _ if lectura > 100:
                resultados.append(f"{lectura}Estado: Fuera de rango")

    return resultados


lecturas = list(map(int, input("Ingrese 5 lecturas de temperatura separadas por espacio: ").split()))

if len(lecturas) != 5:
    print("Debe ingresar exactamente 5 lecturas.")
else:
    resultado = evaluar(lecturas)
    print("lecturas :", resultado)
