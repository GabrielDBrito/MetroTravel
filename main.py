from datos import cargar_aeropuertos, cargar_tarifas

aeropuertos = cargar_aeropuertos("data/aeropuertos.csv")
rutas = cargar_tarifas("data/tarifas.csv")

def mostrar_aeropuertos():
    print("Lista de aeropuertos disponibles:\n")
    for codigo, info in aeropuertos.items():
        visa = "Sí" if info["requiere_visa"] else "No"
        print(f"{codigo} - {info['nombre']} (Requiere visa: {visa})")

def validar_codigo(codigo):
    return codigo in aeropuertos

def pedir_datos_usuario():
    origen = input("Introduce el código del aeropuerto de origen: ").strip().upper()
    while not validar_codigo(origen):
        print("Código no válido.")
        origen = input("Introduce el código del aeropuerto de origen: ").strip().upper()

    destino = input("Introduce el código del aeropuerto de destino: ").strip().upper()
    while not validar_codigo(destino):
        print("Código no válido.")
        destino = input("Introduce el código del aeropuerto de destino: ").strip().upper()

    visa = input("¿El pasajero tiene visa? (s/n): ").strip().lower()
    while visa not in ["s", "n"]:
        visa = input("Respuesta inválida. ¿Tiene visa? (s/n): ").strip().lower()

    tiene_visa = (visa == "s")

    return origen, destino, tiene_visa

def main():
    print("Bienvenido a Metro Travel\n")
    mostrar_aeropuertos()

    origen, destino, tiene_visa = pedir_datos_usuario()

    # Validación de visa
    if aeropuertos[origen]["requiere_visa"] and not tiene_visa:
        print(f"\nNo puedes salir desde {origen} porque requiere visa.")
        return
    if aeropuertos[destino]["requiere_visa"] and not tiene_visa:
        print(f"\nNo puedes viajar a {destino} porque requiere visa.")
        return

    print(f"\nBuscando rutas desde {origen} hasta {destino}...")

if __name__ == "__main__":
    main()
