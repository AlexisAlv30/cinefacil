funciones = [
    {"pelicula": "avatar 2", "hora": "14:00"},
    {"pelicula": "rapidos y furiosos 10", "hora": "16:30"},
    {"pelicula": "toy story 4", "hora": "18:45"},
    {"pelicula": "oppenheimer", "hora": "21:00"}
]

reservas = []

precio_entrada = 45.00

print("bienvenido a cinefácil")
print("\nfunciones disponibles:\n")
for i, funcion in enumerate(funciones):
    print(f"{i + 1}. {funcion['pelicula']} - {funcion['hora']}")

nombre = input("\ningresa tu nombre: ")
opcion = int(input("elige el número de la función que deseas: ")) - 1

if opcion >= 0 and opcion < len(funciones):
    funcion_elegida = funciones[opcion]
    boletos = int(input("cuántos boletos deseas comprar: "))
    total = boletos * precio_entrada

    reserva = {
        "cliente": nombre,
        "pelicula": funcion_elegida["pelicula"],
        "hora": funcion_elegida["hora"],
        "boletos": boletos,
        "total": total
    }

    reservas.append(reserva)

    print("\nresumen de la reserva:")
    print(f"cliente: {nombre}")
    print(f"película: {funcion_elegida['pelicula']}")
    print(f"hora: {funcion_elegida['hora']}")
    print(f"boletos: {boletos}")
    print(f"total a pagar: q{total:.2f}")
else:
    print("opción no válida")

print("\nreservas realizadas hasta el momento:")
for r in reservas:
    print(r)

# opción extra 
opcion_historial = input("\ndeseas ver el historial completo de reservas (s/n): ")

if opcion_historial.lower() == "s":
    print("\n--- historial completo de reservas ---")
    for i, r in enumerate(reservas):
        print(f"\nreserva #{i + 1}")
        print(f"cliente: {r['cliente']}")
        print(f"película: {r['pelicula']}")
        print(f"hora: {r['hora']}")
        print(f"boletos: {r['boletos']}")
        print(f"total: q{r['total']:.2f}")

