import os
import json
from actions import crear_carpeta, cambiar_fondo, buscar_carpeta_por_nombre, buscar_imagen
from intents import detectar_intencion, extraer_nombre_carpeta

from gpt4all import GPT4All

# ==========================
# Inicializar modelo GPT4All
# ==========================
modelo = GPT4All("models/ggml-gpt4all-l13b-snoozy.bin")  # ruta al .bin del modelo

def interpretar_comando(texto_usuario):
    prompt = f"""
Eres un asistente de Windows. Interpreta el siguiente texto en una acción concreta.
Posibles acciones: crear_carpeta, cambiar_fondo, abrir_carpeta.
Devuelve solo un JSON válido con los campos: accion, nombre, ubicacion (ubicacion puede ser None).

Texto: {texto_usuario}
"""
    respuesta = modelo.generate(prompt, temp=0.1)
    try:
        data = json.loads(respuesta)
    except:
        data = {"accion": None, "nombre": None, "ubicacion": None}
    return data

# ==========================
# UTILIDADES
# ==========================
def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")

def pausar():
    input("\nPresiona ENTER para continuar...")

# ==========================
# FUNCIONES DEL MENU
# ==========================
def opcion_crear_carpeta():
    limpiar_pantalla()
    print("📁 CREAR CARPETA")
    nombre = input("Nombre de la nueva carpeta: ").strip()
    if not nombre:
        print("❌ Nombre inválido")
        pausar()
        return
    ubicacion = input("Ubicación (ej: Descargas, Escritorio, HTML2, o deja vacío): ").strip()
    if not ubicacion:
        ruta_destino = os.getcwd()
    else:
        resultados = buscar_carpeta_por_nombre(ubicacion)
        if resultados:
            ruta_destino = resultados[0]
        else:
            print("❌ No se encontró la carpeta, se creará en la carpeta actual")
            ruta_destino = os.getcwd()
    crear_carpeta(nombre, ruta_destino)
    pausar()

def opcion_cambiar_fondo():
    limpiar_pantalla()
    print("🖼️ CAMBIAR FONDO DE PANTALLA")
    nombre = input("Nombre del archivo de imagen: ").strip()
    if not nombre:
        print("❌ Nombre inválido")
        pausar()
        return
    resultados = buscar_imagen(nombre)
    if resultados:
        cambiar_fondo(resultados[0])
    else:
        print("❌ No se encontró la imagen")
    pausar()

def ejecutar_comando_ia():
    limpiar_pantalla()
    print("🤖 Modo IA activado")
    comando = input("Dime qué quieres hacer: ").strip()
    resultado = interpretar_comando(comando)
    accion = resultado.get("accion")
    nombre = resultado.get("nombre")
    ubicacion = resultado.get("ubicacion")

    if accion == "crear_carpeta" and nombre:
        crear_carpeta(nombre, ubicacion)
    elif accion == "cambiar_fondo" and nombre:
        resultados = buscar_imagen(nombre)
        if resultados:
            cambiar_fondo(resultados[0])
        else:
            print("❌ No se encontró la imagen")
    elif accion == "abrir_carpeta" and nombre:
        print(f"📂 Abrir carpeta: {nombre} (pendiente de implementar)")
    else:
        # fallback a intents.py si GPT4All no entiende
        intencion = detectar_intencion(comando)
        if intencion == "crear_carpeta":
            n, u = extraer_nombre_carpeta(comando)
            if n:
                crear_carpeta(n, u)
            else:
                print("❌ No entendí el nombre de la carpeta")
        else:
            print("❌ No entendí el comando")
    pausar()

# ==========================
# MENÚ PRINCIPAL
# ==========================
def mostrar_menu():
    limpiar_pantalla()
    print("=================================")
    print("      🧠 Asistente OS")
    print("=================================")
    print("1. Crear carpeta")
    print("2. Cambiar fondo de pantalla")
    print("3. Comando IA (lenguaje natural)")
    print("4. Salir")
    print("=================================")

def ejecutar():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ").strip()
        if opcion == "1":
            opcion_crear_carpeta()
        elif opcion == "2":
            opcion_cambiar_fondo()
        elif opcion == "3":
            ejecutar_comando_ia()
        elif opcion == "4":
            print("\n👋 Cerrando asistente...")
            break
        else:
            print("❌ Opción inválida")
            pausar()

if __name__ == "__main__":
    print("🧠 Iniciando asistente...")
    ejecutar()