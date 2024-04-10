#Script de ACL Franko Vergara

def determinar_tipo_acl(numero_acl):
    if numero_acl.isdigit():
        numero_acl = int(numero_acl)
        if 1 <= numero_acl <= 99:
            return "ACL Estándar"
        elif 100 <= numero_acl <= 199:
            return "ACL Extendida"
        else:
            return "El número ingresado no corresponde a una lista de acceso."
    else:
        return "El número de ACL ingresado no es válido."

def main():
    while True:
        numero_acl = input("Ingrese el número de ACL IPv4 (o 'salir' para terminar): ")
        
        if numero_acl.lower() == 'salir':
            break
        
        tipo_acl = determinar_tipo_acl(numero_acl)
        print("Es una ACL de tipo:", tipo_acl)
        print()  # Agregamos una línea en blanco para mejorar la presentación

if __name__ == "__main__":
    main()
