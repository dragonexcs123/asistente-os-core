import os
import ctypes
# main.py
import os
import ctypes

# main.py
import os
import ctypes

# Función para crear carpeta
def crear_carpeta(nombre, ruta_destino=None):
    if ruta_destino:
        ruta_completa = os.path.join(ruta_destino, nombre)
    else:
        ruta_completa = os.getcwd()
    try:
        os.makedirs(ruta_completa, exist_ok=True)
        print(f"✅ Carpeta '{nombre}' creada en '{ruta_completa}'")
    except Exception as e:
        print(f"❌ Error: {e}")

# Función para cambiar fondo
def cambiar_fondo(ruta_imagen):
    if not os.path.isfile(ruta_imagen):
        print(f"❌ La imagen '{ruta_imagen}' no existe.")
        return
    try:
        ctypes.windll.user32.SystemParametersInfoW(20, 0, ruta_imagen, 3)
        print(f"✅ Fondo cambiado a '{ruta_imagen}'")
    except Exception as e:
        print(f"❌ Error: {e}")

# Función para buscar carpeta por nombre
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

# Aquí iría todo el código del menú, opciones, etc.