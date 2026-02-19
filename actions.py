# actions.py
import os

def confirmar(mensaje):
    respuesta = input(f"{mensaje} (si/no): ").lower()
    return respuesta == "si"

def crear_carpeta(nombre):
    if os.path.exists(nombre):
        print("⚠️ Esa carpeta ya existe.")
        return

    if confirmar(f"¿Seguro que quieres crear la carpeta '{nombre}'?"):
        os.mkdir(nombre)
        print("✅ Carpeta creada correctamente.")
    else:
        print("❌ Acción cancelada.")
