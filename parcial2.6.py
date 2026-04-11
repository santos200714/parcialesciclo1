
texto = "crithofer santos portillo landaverde"

texto_normalizado = texto.casefold()

resultado = texto_normalizado.replace(" ", "").isalpha()

print(texto)
print(resultado)