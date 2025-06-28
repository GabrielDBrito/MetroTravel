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

def filtrar_rutas_por_visa(rutas, aeropuertos, tiene_visa):
    if tiene_visa:
        return rutas  # No hace falta filtrar

    rutas_filtradas = {}

    for origen in rutas:
        if aeropuertos[origen]["requiere_visa"]:
            continue  # Excluir aeropuerto si requiere visa

        conexiones_validas = []
        for destino, precio in rutas[origen]:
            if not aeropuertos[destino]["requiere_visa"]:
                conexiones_validas.append((destino, precio))

        if conexiones_validas:
            rutas_filtradas[origen] = conexiones_validas

    return rutas_filtradas
def mostrar_rutas(rutas):
    print("\nRutas disponibles (origen -> destino: precio):\n")
    for origen in sorted(rutas):
        for destino, precio in sorted(rutas[origen]):
            print(f"{origen} -> {destino}: ${precio:.2f}")

def dijkstra(rutas, origen, destino):
    nodos_por_visitar = list(rutas.keys())
    distancias = {nodo: float('inf') for nodo in rutas}
    anteriores = {nodo: None for nodo in rutas}
    distancias[origen] = 0

    while nodos_por_visitar:
        # Selecciona el nodo con la menor distancia conocida
        actual = min(
            (nodo for nodo in nodos_por_visitar),
            key=lambda nodo: distancias[nodo],
            default=None
        )

        if actual is None or distancias[actual] == float('inf'):
            break  # No hay camino posible

        nodos_por_visitar.remove(actual)

        if actual == destino:
            break  # Ya llegamos

        for vecino, costo in rutas.get(actual, []):
            nueva_distancia = distancias[actual] + costo
            if nueva_distancia < distancias[vecino]:
                distancias[vecino] = nueva_distancia
                anteriores[vecino] = actual

    # Reconstrucción del camino
    camino = []
    actual = destino
    while actual is not None:
        camino.insert(0, actual)
        actual = anteriores[actual]

    if camino and camino[0] == origen:
        return camino, distancias[destino]
    else:
        return None, float('inf')

def bfs(rutas, origen, destino):
    cola = [(origen, [origen])]
    visitados = set()

    while cola:
        actual, camino = cola.pop(0)
        if actual == destino:
            return camino, len(camino) - 2 # -2 porque no contamos el origen como escala

        if actual in visitados:
            continue
        visitados.add(actual)

        for vecino, _ in rutas.get(actual, []):  # Ignora el costo
            if vecino not in visitados:
                cola.append((vecino, camino + [vecino]))

    return None, float('inf')



def main():
    print("Bienvenido a Metro Travel\n")

    while True:
        print("\nMenú principal:")
        print("1. Buscar ruta")
        print("2. Salir")
        opcion_menu = input("Selecciona una opción (1/2): ").strip()

        if opcion_menu == "2":
            print("¡Gracias por usar Metro Travel! Hasta pronto.")
            break
        elif opcion_menu != "1":
            print("Opción inválida. Intenta nuevamente.")
            continue

        mostrar_aeropuertos()
        origen, destino, tiene_visa = pedir_datos_usuario()

        if aeropuertos[origen]["requiere_visa"] and not tiene_visa:
            print(f"\nNo puedes salir desde {origen} porque requiere visa.")
            continue
        if aeropuertos[destino]["requiere_visa"] and not tiene_visa:
            print(f"\nNo puedes viajar a {destino} porque requiere visa.")
            continue

        print(f"\nBuscando rutas desde {origen} hasta {destino}...")
        rutas_filtradas = filtrar_rutas_por_visa(rutas, aeropuertos, tiene_visa)
        mostrar_rutas(rutas_filtradas)

        print("\nElige el criterio de búsqueda:")
        print("1. Ruta más barata (Dijkstra)")
        print("2. Ruta con menos escalas (BFS)")
        opcion = input("Opción (1/2): ").strip()

        if opcion == "1":
            ruta, costo = dijkstra(rutas_filtradas, origen, destino)
            if ruta:
                print("\nRuta más barata encontrada:")
                print(" -> ".join(ruta))
                print(f"Costo total: ${costo:.2f}")
            else:
                print("\nNo hay ruta disponible bajo las condiciones dadas.")
        elif opcion == "2":
            ruta, escalas = bfs(rutas_filtradas, origen, destino)
            if ruta:
                print("\nRuta con menos escalas encontrada:")
                print(" -> ".join(ruta))
                print(f"Escalas: {escalas}")
            else:
                print("\nNo hay ruta disponible bajo las condiciones dadas.")
        else:
            print("Opción inválida.")





if __name__ == "__main__":
    main()
