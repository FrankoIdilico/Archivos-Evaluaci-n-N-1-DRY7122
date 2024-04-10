import json

def cargarjson(nombrearchivo):
    try:
        with open(nombrearchivo, 'r') as archivo:
            ourjson = json.load(archivo)  # Almacenar el contenido del archivo JSON en la variable ourjson
        return ourjson  # Retornar el contenido del archivo JSON
    except FileNotFoundError:
        print(f"El archivo {nombrearchivo} no se encontró.")
        return None
    except Exception as e:
        print(f"Ocurrió un error al abrir el archivo JSON: {e}")
        return None

def main():
    # Nombre del archivo JSON
    nombre_archivo = "myfile.json"

    # Cargar el archivo JSON y almacenarlo en la variable ourjson
    ourjson = cargarjson(nombre_archivo)

    if ourjson:  # Verificar si ourjson contiene datos
        print("Contenido del archivo JSON:")
        print(ourjson)  # Imprimir el contenido del archivo JSON
    else:
        print("No se pudo cargar el archivo JSON.")

if __name__ == "__main__":
    main()
