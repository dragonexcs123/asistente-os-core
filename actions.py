# actions.py
import os
import ctypes
import os

def cambiar_fondo(ruta_imagen):
    if not os.path.exists(ruta_imagen):
        print("❌ La imagen no existe.")
        return

    try:
        # 20 = SPI_SETDESKWALLPAPER
        ctypes.windll.user32.SystemParametersInfoW(20, 0, ruta_imagen, 3)
        print("✅ Fondo de pantalla cambiado correctamente.")
    except Exception as e:
        print(f"❌ Error al cambiar fondo: {e}")
        
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
