codigo = input("Ingrese un código o con el formato AÑO-CATEGORÍA-PAÍS: ")

def validar(codigo):
    if codigo is None or codigo == "":
        print("Error: El código no puede estar vacío o ser None.")
        return False
  
      
categoria= codigo[4:-2]   
print(categoria)

if codigo.endswith("SV"):
    print("Ruta Local")
else:
    print("Ruta Internacional")
