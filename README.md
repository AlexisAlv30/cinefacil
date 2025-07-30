# cinefácil

cinefácil es un sistema básico desarrollado en python para gestionar las funciones de una empresa de cine. permite registrar reservas de clientes, calcular el total a pagar y mostrar un historial de todas las reservas realizadas.

---

## funciones principales

1. permite ingresar el nombre del cliente y seleccionar una película de una lista predefinida
2. permite registrar la cantidad de boletos a comprar
3. calcula el total a pagar por la reserva
4. muestra un resumen de la reserva actual
5. guarda cada reserva en una lista de diccionarios
6. (extra) permite mostrar todas las reservas realizadas durante la ejecución

---

## mejoras implementadas en una nueva rama

se creó una rama llamada `mostrar_historial` donde se agregó:

- una opción para mostrar el historial completo de reservas si el usuario lo desea

se hizo el merge de esa rama a `main` con este comando:

```bash
git checkout main
git merge mostrar_historial
