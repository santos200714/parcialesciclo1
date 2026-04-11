palabra=("CANTANDO")

palabra=palabra.lower()

elimina=palabra.removesuffix("ando")
posicion=palabra.find("t")

print(palabra)
print(elimina)
print("posicion de letra t:", posicion)