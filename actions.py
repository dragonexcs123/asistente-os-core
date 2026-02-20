import os
import ctypes

def crear_carpeta(nombre, ruta_destino=None):
    if ruta_destino:
        ruta_completa = os.path.join(ruta_destino, nombre)
    else:
        ruta_completa = os.path.join(os.getcwd(), nombre)
    try:
        os.makedirs(ruta_completa, exist_ok=True)
        print(f"✅ Carpeta '{nombre}' creada correctamente en '{ruta_completa}'")
    except Exception as e:
        print(f"❌ Error al crear carpeta: {e}")

def cambiar_fondo(ruta_imagen):
    if not os.path.isfile(ruta_imagen):
        print(f"❌ La imagen '{ruta_imagen}' no existe.")
        return
    try:
        ctypes.windll.user32.SystemParametersInfoW(20, 0, ruta_imagen, 3)
        print(f"✅ Fondo de pantalla cambiado a '{ruta_imagen}' correctamente.")
    except Exception as e:
        print(f"❌ Error al cambiar el fondo de pantalla: {e}")