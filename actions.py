import os
import ctypes

def opcion_crear_carpeta():
    limpiar_pantalla()
    print("📁 CREAR CARPETA")
    print("---------------------------------")

    nombre = input("Escribe el nombre de la nueva carpeta: ").strip()
    if not nombre:
        print("❌ Nombre inválido.")
        pausar()
        return

    ruta_input = input(
        "Escribe la ubicación (ej: Descargas, Escritorio, HTML2, o deja vacío para la carpeta actual): "
    ).strip()
    user = os.getlogin()
    ruta_destino = None

    # Carpetas especiales conocidas
    especiales = {
        "escritorio": f"C:\\Users\\{user}\\Desktop",
        "documentos": f"C:\\Users\\{user}\\Documents",
        "descargas": f"C:\\Users\\{user}\\Downloads"
    }

    # Si es una carpeta especial
    if ruta_input.lower() in especiales:
        ruta_destino = especiales[ruta_input.lower()]

    # Si es ruta absoluta
    elif os.path.isabs(ruta_input):
        ruta_destino = ruta_input

    # Si es nombre de carpeta existente
    elif ruta_input:
        # Buscamos primero en el directorio actual
        posible_ruta = os.path.join(os.getcwd(), ruta_input)
        if os.path.isdir(posible_ruta):
            ruta_destino = posible_ruta
        else:
            # También podemos buscar en Descargas, Documentos y Escritorio
            buscadas = [
                especiales["descargas"],
                especiales["documentos"],
                especiales["escritorio"]
            ]
            encontrado = False
            for carpeta in buscadas:
                posible_ruta2 = os.path.join(carpeta, ruta_input)
                if os.path.isdir(posible_ruta2):
                    ruta_destino = posible_ruta2
                    encontrado = True
                    break
            if not encontrado:
                # Si no existe, crear en carpeta actual por defecto
                ruta_destino = os.getcwd()
    else:
        # Si el usuario no escribe nada, crear en carpeta actual
        ruta_destino = os.getcwd()

    crear_carpeta(nombre, ruta_destino)
    pausar()

def cambiar_fondo(ruta_imagen):
    if not os.path.isfile(ruta_imagen):
        print(f"❌ La imagen '{ruta_imagen}' no existe.")
        return
    try:
        ctypes.windll.user32.SystemParametersInfoW(20, 0, ruta_imagen, 3)
        print(f"✅ Fondo de pantalla cambiado a '{ruta_imagen}' correctamente.")
    except Exception as e:
        print(f"❌ Error al cambiar el fondo de pantalla: {e}")