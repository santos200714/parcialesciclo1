Nombre= ("ING.Cristhofer Santos Portillo Landaverde.txt")
print(Nombre)
eliminar= Nombre.removesuffix(".txt")
print(eliminar)

prefijo = eliminar.replace("ING.", "")
minusculas = prefijo.lower()
dividido= minusculas.split()

print(minusculas)
print(dividido)