from FUNCIONES_JORGE_ALBORNOZ_005V import *

BD = [
    {
        "ID": 1,
        "nombre": "John",
        "apellido": "Lennon",
        "correo": "john.lennon@gmail.com",
        "Compra": [{"fecha": "2023-11-01", "Monto_total": 48000, "puntos": 480}, {"fecha": "2024-07-03", "Monto_total": 25000, "puntos": 480}]
    }
]

print("¡Bienvenido a la CADENA SUPERMERCADO TODOAHORRO!")

while True:

    # LOS PRINTS DEL MENU 
    menu()

    # ELEGIR UNA OPCIÓN
    opcion = input("Ingrese la opción a ejecutar: ")

    if opcion == "1":
        registrar_cliente(BD)

    elif opcion == "2":
        listar_clientes(BD)

    elif opcion == "3":
        registrar_compra(BD)

    elif opcion == "4":
        listar_compra_cliente(BD)

    elif opcion == "5":
        print("HASTA LA PRÓXIMA!")
        break 

    else:
        print("%$&$! HAGALO OTRA VEZ")