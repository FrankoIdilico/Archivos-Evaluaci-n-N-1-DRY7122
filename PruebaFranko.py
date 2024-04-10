# Paso 1 - Importar el módulo json: Primero, necesitas importar el módulo json, que te permitirá trabajar con datos JSON en Python.

import json


# Paso 2 - Definir una función para cargar el archivo JSON: A continuación, define una función llamada cargarjson que tomará el nombre del archivo JSON como argumento y devolverá los datos del archivo cargados en un formato de diccionar>

def cargarjson(nombrearchivo):
    try:
        with open(nombrearchivo, 'r') as archivo:
            datosjson = json.load(archivo)
        return datosjson
    except FileNotFoundError:
        print(f"El archivo {nombrearchivo} no se encontró.")
        return None
    except Exception as e:
        print(f"Ocurrió un error al abrir el archivo JSON: {e}")
        return None

# Paso 3 - Definir la función principal del script: Luego, define una función llamada main que será la función principal del script. En esta función, especifica el nombre del archivo JSON que quieres cargar (myfile.json) y llama a la fu>

def main():
    # Nombre del archivo JSON
    nombre_archivo = "myfile.json"

    # Cargar el archivo JSON
    json_file = cargarjson(nombre_archivo)

    if json_file:
        print("Contenido del archivo JSON:")
        print(json_file)
    else:
        print("No se pudo cargar el archivo JSON.")

# Paso 4 - Ejecutar la función principal si el script se ejecuta directamente: Por último, verifica si el script se está ejecutando directamente (no se está importando como un módulo). Si es así, llama a la función main para ejecutar el>

if __name__ == "__main__":
    main()

# Paso 5 - Después de seguir estos pasos y escribir todo el código, tendrás un script funcional que carga el archivo JSON myfile.json y muestra su contenido en la consola.

