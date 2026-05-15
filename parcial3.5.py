nombrecompleto = input("Ingrese su nombre completo: ")

cambios = nombrecompleto.split()
invertir = cambios[::-1]

for palabra in invertir:
    palabrafinal = "" 
    
    
    for letra in palabra:
        palabrafinal += letra + "."
    
    
    palabrafinal = palabrafinal[:-1]
    print(palabrafinal)
