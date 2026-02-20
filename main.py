import os
from actions import crear_carpeta, cambiar_fondo

def buscar_carpeta_por_nombre(nombre_carpeta, carpetas_iniciales=None):
    """
    Busca carpetas con el nombre indicado en todo el disco (o en carpetas iniciales)
    Devuelve una lista de rutas encontradas
    """
    if carpetas_iniciales is None:
        carpetas_iniciales = ["C:\\Users"]  # buscar solo en C:\Users para acelerar

    encontrados = []

    for inicio in carpetas_iniciales:
        for root, dirs, files in os.walk(inicio):
            for d in dirs:
                if d.lower() == nombre_carpeta.lower():
                    encontrados.append(os.path.join(root, d))

    return encontrados
# ==============================
# UTILIDADES
# ==============================
def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")

def pausar():
    input("\nPresiona ENTER para continuar...")

# ==============================
# BUSQUEDA DE IMAGEN
# ==============================
def buscar_imagen(nombre_archivo, carpetas=None):
    """
    Busca un archivo por nombre en las carpetas indicadas.
    Si no se indican carpetas, busca en Escritorio, Descargas e Imágenes.
    """
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

# ==============================
# MENÚ PRINCIPAL
# ==============================
def mostrar_menu():
    limpiar_pantalla()
    print("=================================")
    print("      🧠 Asistente OS")
    print("=================================")
    print("1. Crear carpeta")
    print("2. Cambiar fondo de pantalla")
    print("3. Salir")
    print("=================================")

# ==============================
# OPCIONES
# ==============================
def opcion_crear_carpeta():
    limpiar_pantalla()
    print("📁 CREAR CARPETA")
    print("---------------------------------")

    nombre_nueva = input("Escribe el nombre de la nueva carpeta: ").strip()
    if not nombre_nueva:
        print("❌ Nombre inválido.")
        pausar()
        return

    ubicacion = input("Escribe la carpeta donde quieres crearla (ej: HTML2, Descargas, Escritorio) o deja vacío: ").strip()
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
        # Buscar carpeta por nombre en todo el disco (puede tardar un poco)
        print(f"🔍 Buscando carpeta '{ubicacion}' en el disco...")
        resultados = buscar_carpeta_por_nombre(ubicacion)
        if len(resultados) == 0:
            print("❌ No se encontró la carpeta, se creará en la carpeta actual")
            ruta_destino = os.getcwd()
        elif len(resultados) == 1:
            ruta_destino = resultados[0]
        else:
            print("Se encontraron varias carpetas:")
            for i, r in enumerate(resultados):
                print(f"{i+1}. {r}")
            opcion = input("Elige el número de la carpeta donde crear la nueva: ").strip()
            if opcion.isdigit() and 1 <= int(opcion) <= len(resultados):
                ruta_destino = resultados[int(opcion)-1]
            else:
                print("❌ Opción inválida, se creará en la carpeta actual")
                ruta_destino = os.getcwd()

    crear_carpeta(nombre_nueva, ruta_destino)
    pausar()

def opcion_cambiar_fondo():
    limpiar_pantalla()
    print("🖼️ CAMBIAR FONDO DE PANTALLA")
    print("---------------------------------")

    nombre = input("Escribe el nombre del archivo de imagen (ej: fondo.jpg): ").strip()
    if not nombre:
        print("❌ Nombre inválido")
        pausar()
        return

    resultados = buscar_imagen(nombre)
    if len(resultados) == 0:
        print("❌ No se encontró el archivo en las carpetas comunes")
    elif len(resultados) == 1:
        ruta = resultados[0]
        cambiar_fondo(ruta)
    else:
        print("Se encontraron varios archivos:")
        for i, r in enumerate(resultados):
            print(f"{i+1}. {r}")
        opcion = input("Elige el número del archivo que deseas usar: ").strip()
        if opcion.isdigit() and 1 <= int(opcion) <= len(resultados):
            ruta = resultados[int(opcion)-1]
            cambiar_fondo(ruta)
        else:
            print("❌ Opción inválida")

    pausar()

# ==============================
# LOOP PRINCIPAL
# ==============================
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
            print("\n❌ Opción inválida.")
            pausar()

if __name__ == "__main__":
    ejecutar()