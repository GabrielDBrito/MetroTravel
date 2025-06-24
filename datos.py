import csv

def cargar_aeropuertos(ruta):
    aeropuertos = {}
    with open(ruta, newline='', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            codigo = fila["Codigo"].strip()
            nombre = fila["Nombre"].strip()
            visa = fila["RequiereVisa"].strip().upper() == "SI"
            aeropuertos[codigo] = {
                "nombre": nombre,
                "requiere_visa": visa
            }
    return aeropuertos

def cargar_tarifas(ruta):
    rutas = {}
    with open(ruta, newline='', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            origen = fila["Origen"].strip()
            destino = fila["Destino"].strip()
            precio = float(fila["Precio"])

            if origen not in rutas:
                rutas[origen] = []
            if destino not in rutas:
                rutas[destino] = []

            rutas[origen].append((destino, precio))
            rutas[destino].append((origen, precio))  # Vuelos ida y vuelta
    return rutas