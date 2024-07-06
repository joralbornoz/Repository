def menu():
    """ MENU """
    opciones = [
        "Registrar cliente",
        "Listar clientes",
        "Registrar compra",
        "Listar compra cliente",
        "Salir",
    ]

    for i, op in enumerate(opciones):
        print(f"{i+1}. {op}")

def registrar_cliente(bd):
    nombre = input("Ingrese su primer nombre del cliente: ").upper()
    apellido = input("Ingrese su primer apellido del cliente: ").upper()
    correo = input("Ingrese su correo electronico: ").upper() 

    id_cliente = len(bd) + 1

    bd.append(
        {
            "ID": id_cliente,
            "nombre": nombre,
            "apellido": apellido,
            "correo": correo,
            "compra": []
        }
    )

    print("\nSe agrego un nuevo cliente!\n")

def listar_clientes(bd):
    print("\nInformacion de los clientes registrados son:\n")
    print("ID\t\tNombre\t\tApellido\t\tCorreo")
    for cliente in bd:
        print(f'{cliente["ID"]}\t\t{cliente["nombre"]}\t\t{cliente["apellido"]}\t\t{cliente["correo"]}')

    print("\nListado de cliente!\n")

def registrar_compra(bd):
    id = int(input("Ingrese el ID del cliente que esta comprando: "))

    for cliente in bd:
        if cliente["ID"] == id:
            fecha = input("Ingrese fecha de compra (AAAA-MM-DD): ")
            monto = int(input("Ingrese monto de la compra: "))
            cliente["compra"].append(
                {
                    "fecha": fecha,
                    "Monto_Total": monto,
                    "puntos": round(monto*0.01)

                }
            )
            print(f'\nSe ha agregado una compra para {cliente["nombre"]} {cliente["apellido"]}.')
            break
    
def listar_compra_cliente(bd):
    id = int(input("Ingrese el ID del cliente que asiste: "))

    for cliente in bd:
        if cliente["ID"] == id:
            texto = f"ID Cliente: {id}\n"
            texto += f'NOMBRE CLIENTE: {cliente["nombre"]} {cliente["apellido"]}\n'
            texto += f"Fecha de compra\t\tMonto Total\t\tPuntos\n"

            puntos_totales = 0
            for monto in cliente["Fecha compra"]:
                texto += f'{monto["fecha"]}\n'
                puntos_totales += (monto{(Monto_Total)})*0.01
            texto += f'Puntos acumulados: {puntos_totales} Puntos'

            with open(f"RESUMEN_CLIENTE_ID_{id}.txt", "w", encoding='utf-8') as archivo:
	            archivo.write(texto)

            print("ARCHIVO CREADO")

            break
        

