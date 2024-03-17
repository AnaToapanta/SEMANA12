def calcular_descuento(monto_total):
    descuento = 0

    if monto_total > 1000:
        descuento = monto_total * 0.1  # 10% de descuento si el monto total es mayor a 1000
    elif monto_total > 500:
        descuento = monto_total * 0.05  # 5% de descuento si el monto total es mayor a 500
    elif monto_total < 500:
        descuento = monto_total * 0.02   # 2% de descuento si el monto total es menor a 500


    monto_final = monto_total - descuento
    return monto_final


monto_total = float(input("Ingrese el monto total de la compra: "))
monto_final = calcular_descuento(monto_total)
print("El monto final a pagar es: ", monto_final)