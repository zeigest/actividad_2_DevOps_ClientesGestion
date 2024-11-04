import os

# Directorio donde se guardarán los archivos de los clientes
CLIENTES_DIR = './clientes'

# Asegurarse de que el directorio exista
os.makedirs(CLIENTES_DIR, exist_ok=True)

# Servicios disponibles
SERVICIOS_DISPONIBLES = ["Telefonía", "Internet", "TV de Paga"]

# Tabla hash para asociar el nombre del cliente con su archivo
clientes_archivos = {}

# Función para cargar los clientes existentes en la tabla hash
def cargar_clientes():
    for archivo in os.listdir(CLIENTES_DIR):
        if archivo.endswith('.txt'):
            nombre = os.path.splitext(archivo)[0]
            clientes_archivos[nombre] = os.path.join(CLIENTES_DIR, archivo)

# Función para crear un archivo nuevo de cliente
def crear_cliente():
    nombre = input("Ingrese el nombre del cliente: ")
    archivo = os.path.join(CLIENTES_DIR, f"{nombre}.txt")
    
    if os.path.isfile(archivo):
        print("El cliente ya existe.")
    else:
        with open(archivo, 'w') as f:
            f.write(f"Cliente: {nombre}\n")
            f.write("Servicios solicitados:\n")
        clientes_archivos[nombre] = archivo  # Agregar a la tabla hash
        agregar_servicio(nombre)
        print("Archivo de cliente creado correctamente.")

# Función para agregar servicio a un cliente existente
def agregar_servicio(nombre=None):
    if not nombre:
        nombre = input("Ingrese el nombre del cliente: ")
    
    archivo = clientes_archivos.get(nombre)
    
    if archivo and os.path.isfile(archivo):
        servicios_existentes = obtener_servicios_existentes(archivo)
        print("\nSeleccione un servicio para agregar:")
        mostrar_servicios()
        servicio = seleccionar_servicio()
        
        if servicio in servicios_existentes:
            print(f"El cliente ya tiene el servicio de {servicio}.")
        else:
            with open(archivo, 'a') as f:
                f.write(f"- {servicio}\n")
            print(f"Servicio '{servicio}' agregado correctamente al cliente {nombre}.")
    else:
        print("El cliente no existe.")

# Función para modificar la información del cliente
def modificar_cliente():
    nombre = input("Ingrese el nombre del cliente a modificar: ")
    archivo = clientes_archivos.get(nombre)
    
    if archivo and os.path.isfile(archivo):
        print("\nContenido actual del cliente:")
        buscar_cliente(nombre)
        
        print("\nIngrese el nuevo nombre (o presione Enter para dejarlo igual):")
        nuevo_nombre = input("Nuevo nombre: ").strip()
        if nuevo_nombre:
            nuevo_archivo = os.path.join(CLIENTES_DIR, f"{nuevo_nombre}.txt")
            os.rename(archivo, nuevo_archivo)
            clientes_archivos.pop(nombre)
            clientes_archivos[nuevo_nombre] = nuevo_archivo
            nombre = nuevo_nombre
        
        print("Modificación completada.")
    else:
        print("El cliente no existe.")

# Función para eliminar un cliente
def eliminar_cliente():
    nombre = input("Ingrese el nombre del cliente a eliminar: ")
    archivo = clientes_archivos.get(nombre)
    
    if archivo and os.path.isfile(archivo):
        os.remove(archivo)
        clientes_archivos.pop(nombre)
        print(f"Cliente {nombre} eliminado correctamente.")
    else:
        print("El cliente no existe.")

# Función para listar todos los clientes
def listar_clientes():
    print("Clientes existentes:")
    for cliente in clientes_archivos.keys():
        print(cliente)

# Función para buscar un cliente por nombre
def buscar_cliente(nombre=None):
    if not nombre:
        nombre = input("Ingrese el nombre del cliente a buscar: ")
    archivo = clientes_archivos.get(nombre)
    
    if archivo and os.path.isfile(archivo):
        with open(archivo, 'r') as f:
            print(f.read())
    else:
        print("El cliente no existe.")

# Función para mostrar los servicios disponibles
def mostrar_servicios():
    print("Servicios disponibles:")
    for i, servicio in enumerate(SERVICIOS_DISPONIBLES, start=1):
        print(f"{i}. {servicio}")

# Función para seleccionar un servicio del menú
def seleccionar_servicio():
    while True:
        try:
            opcion = int(input("Seleccione una opción de servicio (1-3): "))
            if 1 <= opcion <= len(SERVICIOS_DISPONIBLES):
                return SERVICIOS_DISPONIBLES[opcion - 1]
            else:
                print("Opción no válida. Intente de nuevo.")
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número.")

# Función para obtener los servicios existentes de un cliente
def obtener_servicios_existentes(archivo):
    servicios = []
    with open(archivo, 'r') as f:
        for line in f:
            if line.startswith("- "):
                servicios.append(line[2:].strip())
    return servicios

# Simulación de usuarios en un grupo de trabajo
def simular_interaccion():
    usuarios = ["Usuario1", "Usuario2"]
    print("Interacciones simuladas entre usuarios del grupo de trabajo.")
    for usuario in usuarios:
        print(f"\nAccediendo como: {usuario}")
        listar_clientes()
        buscar_cliente(input("Ingrese el nombre del cliente a buscar: "))

# Menú principal
def menu():
    cargar_clientes()  # Cargar los clientes existentes en la tabla hash
    while True:
        print("\n1. Crear nuevo cliente")
        print("2. Agregar servicio a cliente existente")
        print("3. Modificar información de cliente")
        print("4. Eliminar cliente")
        print("5. Listar todos los clientes")
        print("6. Buscar un cliente")
        print("7. Simular interacción de grupo de trabajo")
        print("8. Salir")
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            crear_cliente()
        elif opcion == '2':
            agregar_servicio()
        elif opcion == '3':
            modificar_cliente()
        elif opcion == '4':
            eliminar_cliente()
        elif opcion == '5':
            listar_clientes()
        elif opcion == '6':
            buscar_cliente()
        elif opcion == '7':
            simular_interaccion()
        elif opcion == '8':
            print("Saliendo...")
            break
        else:
            print("Opción no válida")

# Ejecutar el menú principal
if __name__ == "__main__":
    menu()
