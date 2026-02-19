# main.py
from intents import detectar_intencion, extraer_nombre_carpeta
from actions import crear_carpeta

def ejecutar():
    print("🧠 Asistente OS V1 iniciado")
    print("Escribe un comando. Ejemplo: crear carpeta pruebas")
    print("Escribe 'salir' para terminar.\n")

    while True:
        texto = input(">>> ")

        intencion = detectar_intencion(texto)

        if intencion == "crear_carpeta":
            nombre = extraer_nombre_carpeta(texto)

            if nombre:
                crear_carpeta(nombre)
            else:
                print("🤔 No entendí el nombre de la carpeta.")

        elif intencion == "salir":
            print("👋 Cerrando asistente.")
            break

        else:
            print("❓ No entendí esa orden.")

if __name__ == "__main__":
    ejecutar()
