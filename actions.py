import os
import ctypes

def buscar_carpeta_por_nombre(nombre_carpeta, carpetas_iniciales=None):
    """
    Busca carpetas con el nombre indicado en todo el disco (o en carpetas iniciales)
    Devuelve una lista de rutas encontradas
    """
    if carpetas_iniciales is None:
        # Por defecto busca en las unidades comunes (C:\)
        carpetas_iniciales = ["C:\\"]

    encontrados = []

    for inicio in carpetas_iniciales:
        for root, dirs, files in os.walk(inicio):
            for d in dirs:
                if d.lower() == nombre_carpeta.lower():
                    encontrados.append(os.path.join(root, d))

    return encontrados

def cambiar_fondo(ruta_imagen):
    if not os.path.isfile(ruta_imagen):
        print(f"❌ La imagen '{ruta_imagen}' no existe.")
        return
    try:
        ctypes.windll.user32.SystemParametersInfoW(20, 0, ruta_imagen, 3)
        print(f"✅ Fondo de pantalla cambiado a '{ruta_imagen}' correctamente.")
    except Exception as e:
        print(f"❌ Error al cambiar el fondo de pantalla: {e}")