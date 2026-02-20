# intents.py
from rapidfuzz import fuzz
from utils import normalizar
INTENCIONES = {
    "crear_carpeta": [
        "crear carpeta",
        "haz una carpeta",
        "nueva carpeta",
        "crea carpeta"
    ],
    "cambiar_fondo": [
        "cambiar fondo",
        "poner fondo",
        "cambia el fondo",
        "poner fondo de pantalla"
    ],
    "salir": [
        "salir",
        "cerrar",
        "terminar",
        "adios"
    ]
}

def detectar_intencion(texto):
    """
    Determina la acción que el usuario quiere hacer
    Devuelve: "crear_carpeta", "cambiar_fondo", "abrir_carpeta", None
    """
    texto = texto.lower()

    if fuzz.partial_ratio("crear carpeta", texto) > 70:
        return "crear_carpeta"
    elif fuzz.partial_ratio("cambiar fondo", texto) > 70 or fuzz.partial_ratio("poner fondo", texto) > 70:
        return "cambiar_fondo"
    elif fuzz.partial_ratio("abrir", texto) > 70:
        return "abrir_carpeta"
    else:
        return None

def extraer_nombre_carpeta(texto):
    """
    Extrae el nombre de la carpeta del comando
    Ej: 'crear carpeta HTML3 en HTML2' -> ('HTML3','HTML2')
    """
    partes = texto.lower().split("crear carpeta")
    if len(partes) < 2:
        return None, None
    contenido = partes[1].strip()
    if "en" in contenido:
        nombre, destino = contenido.split("en")
        return nombre.strip(), destino.strip()
    return contenido.strip(), None

def detectar_intencion(texto):
    texto = normalizar(texto)

    mejor_score = 0
    mejor_intencion = None

    for intencion, frases in INTENCIONES.items():
        for frase in frases:
            score = fuzz.partial_ratio(texto, frase)
            if score > mejor_score:
                mejor_score = score
                mejor_intencion = intencion

    if mejor_score > 60:
        return mejor_intencion
    return None


def extraer_nombre_carpeta(texto):
    texto = normalizar(texto)
    palabras = texto.split()

    if "carpeta" in palabras:
        indice = palabras.index("carpeta")
        if indice + 1 < len(palabras):
            return palabras[indice + 1]

    return None
def extraer_ruta_imagen(texto):
    palabras = texto.split()

    for palabra in palabras:
        if palabra.endswith((".jpg", ".png", ".jpeg")):
            return palabra

    return None