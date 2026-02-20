import os
import ctypes

# ==========================
# FUNCIONES
# ==========================
def crear_carpeta(nombre, ruta_destino=None):
    if ruta_destino:
        ruta_completa = os.path.join(ruta_destino, nombre)
    else:
        ruta_completa = os.getcwd()
    try:
        os.makedirs(ruta_completa, exist_ok=True)
        print(f"✅ Carpeta '{nombre}' creada en '{ruta_completa}'")
    except Exception as e:
        print(f"❌ Error al crear carpeta: {e}")

def cambiar_fondo(ruta_imagen):
    if not os.path.isfile(ruta_imagen):
        print(f"❌ La imagen '{ruta_imagen}' no existe.")
        return
    try:
        ctypes.windll.user32.SystemParametersInfoW(20, 0, ruta_imagen, 3)
        print(f"✅ Fondo de pantalla cambiado a '{ruta_imagen}'")
    except Exception as e:
        print(f"❌ Error al cambiar fondo: {e}")

def buscar_carpeta_por_nombre(nombre_carpeta, carpetas_iniciales=None):
    if carpetas_iniciales is None:
        carpetas_iniciales = ["C:\\Users"]
    encontrados = []
    for inicio in carpetas_iniciales:
        for root, dirs, files in os.walk(inicio):
            for d in dirs:
                if d.lower() == nombre_carpeta.lower():
                    encontrados.append(os.path.join(root, d))
    return encontrados

def buscar_imagen(nombre_archivo, carpetas=None):
    if carpetas is None:
        user = os.getlogin()
        carpetas = [
            f"C:\\Users\\{user}\\Desktop",
            f"C:\\Users\\{user}\\Downloads",
            f"C:\\Users\\{user}\\Pictures"
        ]
    encontrados = []
    for carpeta in carpetas:
        for root, dirs, files in os.walk(carpeta):
            for file in files:
                if file.lower() == nombre_archivo.lower():
                    encontrados.append(os.path.join(root, file))
    return encontrados

# ==========================
# UTILIDADES
# ==========================
def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")

def pausar():
    input("\nPresiona ENTER para continuar...")

# ==========================
# CREAR CARPETA
# ==========================
def opcion_crear_carpeta():
    limpiar_pantalla()
    print("📁 CREAR CARPETA")
    print("---------------------------------")

    nombre_nueva = input("Nombre de la nueva carpeta: ").strip()
    if not nombre_nueva:
        print("❌ Nombre inválido")
        pausar()
        return

    ubicacion = input(
        "Ubicación (ej: Descargas, Escritorio, HTML2, o deja vacío): "
    ).strip()
    user = os.getlogin()
    ruta_destino = None

    # Carpetas especiales
    especiales = {
        "escritorio": f"C:\\Users\\{user}\\Desktop",
        "documentos": f"C:\\Users\\{user}\\Documents",
        "descargas": f"C:\\Users\\{user}\\Downloads"
    }

    if not ubicacion:
        ruta_destino = os.getcwd()
    elif ubicacion.lower() in especiales:
        ruta_destino = especiales[ubicacion.lower()]
    elif os.path.isabs(ubicacion):
        ruta_destino = ubicacion
    else:
        print(f"🔍 Buscando carpeta '{ubicacion}' en el disco...")
        resultados = buscar_carpeta_por_nombre(ubicacion)
        if len(resultados) == 0:
            print("❌ No se encontró, se creará en la carpeta actual")
            ruta_destino = os.getcwd()
        elif len(resultados) == 1:
            ruta_destino = resultados[0]
        else:
            print("Se encontraron varias carpetas:")
            for i, r in enumerate(resultados):
                print(f"{i+1}. {r}")
            opcion = input("Elige el número de la carpeta: ").strip()
            if opcion.isdigit() and 1 <= int(opcion) <= len(resultados):
                ruta_destino = resultados[int(opcion)-1]
            else:
                print("❌ Opción inválida, se creará en la carpeta actual")
                ruta_destino = os.getcwd()

    crear_carpeta(nombre_nueva, ruta_destino)
    pausar()

# ==========================
# CAMBIAR FONDO
# ==========================
def opcion_cambiar_fondo():
    limpiar_pantalla()
    print("🖼️ CAMBIAR FONDO DE PANTALLA")
    print("---------------------------------")

    nombre = input("Nombre del archivo de imagen (ej: fondo.jpg): ").strip()
    if not nombre:
        print("❌ Nombre inválido")
        pausar()
        return

    resultados = buscar_imagen(nombre)
    if len(resultados) == 0:
        print("❌ No se encontró el archivo")
    elif len(resultados) == 1:
        cambiar_fondo(resultados[0])
    else:
        print("Se encontraron varios archivos:")
        for i, r in enumerate(resultados):
            print(f"{i+1}. {r}")
        opcion = input("Elige el número: ").strip()
        if opcion.isdigit() and 1 <= int(opcion) <= len(resultados):
            cambiar_fondo(resultados[int(opcion)-1])
        else:
            print("❌ Opción inválida")

    pausar()

# ==========================
# MENÚ PRINCIPAL
# ==========================
def mostrar_menu():
    limpiar_pantalla()
    print("=================================")
    print("      🧠 Asistente OS")
    print("=================================")
    print("1. Crear carpeta")
    print("2. Cambiar fondo de pantalla")
    print("3. Salir")
    print("=================================")

def ejecutar():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ").strip()
        if opcion == "1":
            opcion_crear_carpeta()
        elif opcion == "2":
            opcion_cambiar_fondo()
        elif opcion == "3":
            print("\n👋 Cerrando asistente...")
            break
        else:
            print("❌ Opción inválida")
            pausar()

if __name__ == "__main__":
    print("🧠 Iniciando asistente...")
    ejecutar()