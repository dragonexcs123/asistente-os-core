from rapidfuzz import fuzz

# Detecta la intención básica (backup si GPT4All falla)
def detectar_intencion(texto):
    texto = texto.lower()
    if fuzz.partial_ratio("crear carpeta", texto) > 70:
        return "crear_carpeta"
    elif fuzz.partial_ratio("cambiar fondo", texto) > 70 or fuzz.partial_ratio("poner fondo", texto) > 70:
        return "cambiar_fondo"
    elif fuzz.partial_ratio("abrir", texto) > 70:
        return "abrir_carpeta"
    else:
        return None

# Extrae nombre y ubicación de carpetas de comandos simples
def extraer_nombre_carpeta(texto):
    texto = texto.lower()
    partes = texto.split("crear carpeta")
    if len(partes) < 2:
        return None, None
    contenido = partes[1].strip()
    if "en" in contenido:
        nombre, destino = contenido.split("en", 1)
        return nombre.strip(), destino.strip()
    return contenido.strip(), None