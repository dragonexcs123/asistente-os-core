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

    ruta = input("Escribe la ruta completa de la imagen: ").strip()

    if ruta:
        cambiar_fondo(ruta)
    else:
        print("❌ Ruta inválida.")

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