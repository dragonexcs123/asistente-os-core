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
    "salir": [
        "salir",
        "cerrar",
        "terminar",
        "adios"
    ]
}

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
