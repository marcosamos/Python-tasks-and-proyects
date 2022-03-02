# En construccion

# Interfaz para posicionar a un usuario nuevo al nivel correcto. 
idioma = ""

while idioma != "9":
    print("Que idioma deseas aprender? escribe la letra correcta: A = English, B = Frances, 9 para salir")

    idioma = input("Teclea la letra del idioma: ")

    if idioma.lower() == "a":
        print("Exelent")
        nivel_ingles = int(input("cual es tu nivel? teclea del 1-4:  "))
        if nivel_ingles == 1:
            print("Necesitas mucha ayuda")
            break
        elif nivel_ingles == 2:
            print("vas bien pero necesitamos aprender mas")
            break
        elif nivel_ingles == 3:
            print("Muy bien casi alcanzas al maestro")
            break
        elif nivel_ingles == 4:
            print("Trabaja con nosotros")
            break
        else:
            print("Teclea un numero valido 1-4")
    elif idioma == "B":
        print("très bien")
    elif idioma == "9":
        print("Gracias por contactar a MRUS, vuelve pronto")
    else:
        print("Teclea A o B")

print("Programa terminado")