import os
import ctypes

def crear_carpeta(nombre):
    try:
        os.makedirs(nombre, exist_ok=True)
        print(f"✅ Carpeta '{nombre}' creada correctamente.")
    except Exception as e:
        print(f"❌ Error al crear carpeta: {e}")

def cambiar_fondo(ruta_imagen):
    """
    Cambia el fondo de pantalla de Windows usando la ruta absoluta
    """
    if not os.path.isfile(ruta_imagen):
        print(f"❌ La imagen '{ruta_imagen}' no existe.")
        return

    try:
        # SPI_SETDESKWALLPAPER = 20, 3 = actualizar inmediatamente
        ctypes.windll.user32.SystemParametersInfoW(20, 0, ruta_imagen, 3)
        print(f"✅ Fondo de pantalla cambiado a '{ruta_imagen}' correctamente.")
    except Exception as e:
        print(f"❌ Error al cambiar el fondo de pantalla: {e}")