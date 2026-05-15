from decimal import Decimal, InvalidOperation

total = Decimal("0.0")

while True:
    try:
        entrada = input("Ingrese el precio (cero para terminar): ")
        if entrada == "0":
            break

        precio = Decimal(entrada)
        total += precio

    except InvalidOperation:
        print("Error: Por favor, ingrese un número válido.")

print(f"El total es :$ {total:.2f}")

