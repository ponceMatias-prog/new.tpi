import random

def maldonado():
    print("¡Bienvenido al juego de preguntas y respuestas!")
    ciencias_naturales = [
        {"pregunta": "¿Cuál es el planeta más cercano al Sol?", "opciones": ["A) Mercurio", "B) Venus", "C) Marte"], "respuesta": "A"},
        {"pregunta": "¿Qué gas respiramos principalmente?", "opciones": ["A) Oxígeno", "B) Nitrógeno", "C) Dióxido de carbono"], "respuesta": "A"},
        {"pregunta": "¿Cuál es el órgano que bombea la sangre?", "opciones": ["A) Pulmón", "B) Corazón", "C) Hígado"], "respuesta": "B"},
        {"pregunta": "¿Qué estado de la materia tiene forma y volumen definidos?", "opciones": ["A) Líquido", "B) Sólido", "C) Gas"], "respuesta": "B"},
        {"pregunta": "¿Qué objeto produce luz de forma natural?", "opciones": ["A) La Luna", "B) El Sol", "C) Un espejo"], "respuesta": "B"},
        {"pregunta": "¿Cuál de estos materiales puede atraer un imán?", "opciones": ["A) Plástico", "B) Hierro", "C) Madera"], "respuesta": "B"},
    ]

    ciencias_sociales = [
        {"pregunta": "¿Quién fue el primer presidente de Argentina?", "opciones": ["A) Bernardino Rivadavia", "B) San Martín", "C) Sarmiento"], "respuesta": "A"},
        {"pregunta": "¿Cuál es la capital de Argentina?", "opciones": ["A) Córdoba", "B) Buenos Aires", "C) Rosario"], "respuesta": "B"},
        {"pregunta": "¿Qué continente está al sur de Europa?", "opciones": ["A) Asia", "B) África", "C) Oceanía"], "respuesta": "B"},
        {"pregunta": "¿Qué colores tiene la bandera de Argentina?", "opciones": ["A) Azul y blanco", "B) Rojo y blanco", "C) Verde y amarillo"], "respuesta": "A"},
        {"pregunta": "¿Cuál es la capital de francia?", "opciones": ["A) Berlin", "B) Madrid", "C) París"], "respuesta": "C"},
        {"pregunta": "¿En dónde se encuentra el océano Pacífico en Argentina?", "opciones": ["A) Al este", "B) Al oeste", "C) Al norte"], "respuesta": "B"}
    ]

    matematica = [
        {"pregunta": "¿Cuánto es 7 + 8?", "opciones": ["A) 14", "B) 15", "C) 16"], "respuesta": "B"},
        {"pregunta": "¿Cuánto es 9 x 6?", "opciones": ["A) 54", "B) 56", "C) 52"], "respuesta": "A"},
        {"pregunta": "¿Cuál es la mitad de 100?", "opciones": ["A) 25", "B) 50", "C) 75"], "respuesta": "B"},
        {"pregunta": "¿Cuánto es 12 ÷ 4?", "opciones": ["A) 2", "B) 3", "C) 4"], "respuesta": "B"},
        {"pregunta": "¿Cuál es el resultado de 5²?", "opciones": ["A) 10", "B) 25", "C) 50"], "respuesta": "B"},
        {"pregunta": "¿Cuál es el resultado de cos(0)?", "opciones": ["A) 0", "B) 1", "C) -1"], "respuesta": "B"}
    ]

    print("Selecciona la categoría de preguntas:")
    print("1) Ciencias Naturales")
    print("2) Ciencias Sociales")
    print("3) Matemática")
    categoria = input("Ingresa el número de la categoría: ")

    if categoria == "1":
        seleccionadas = random.sample(ciencias_naturales, 3)
    elif categoria == "2":
        seleccionadas = random.sample(ciencias_sociales, 3)
    elif categoria == "3":
        seleccionadas = random.sample(matematica, 3)
    else:
        print("Categoría no válida.")
        return

    puntaje = 0

    for p in seleccionadas:
        print("\n" + p["pregunta"])
        for opcion in p["opciones"]:
            print(opcion)
        respuesta = input("Tu respuesta: ").upper()

        if respuesta == p["respuesta"]:
            print("Correcto!")
            puntaje += 1
        else:
            print("Incorrecto!")

    print(f"\nTu puntaje final es: {puntaje}/{len(seleccionadas)}")

if __name__ == "__main__":
    maldonado()