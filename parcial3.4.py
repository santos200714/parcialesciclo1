def registro():
    resultados = [] 
    for numero in range(1, 51):
        if numero == 42:
            break
        elif numero % 3 == 0:
            continue  
        else:
            print(f"procesando registro ID: {numero}")
            resultados.append(numero)  
            
    return resultados

print(registro())