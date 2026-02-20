import os
from actions import crear_carpeta, cambiar_fondo

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

    nombre = input("Escribe el nombre de la nueva carpeta: ").strip()
    if nombre:
        crear_carpeta(nombre)
    else:
        print("❌ Nombre inválido.")

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