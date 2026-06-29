import random

#Lista de plantillas de historias. Cada plantilla es un diccionario con 3 campos:
#"titulo" = nombre del cuento
#"tipos" = lista de tuplas (clave, descripcion_para_el_usuario)
#"texto" = minicuentos con marcadores {clave}

#se usó lista de diccionarios porque se necesita mantener juntos el texto del cuento y los tipos de palabras
#que le corresponden. El diccionario asocia cada dato con su nombre.

PLANTILLAS = [
    {
        "titulo": "La gran aventura",
        "tipos": [
            ("animal",    "Escribe un animal (ej: perro, dragón, pingüino)"),
            ("lugar",     "Escribe un lugar (ej: la selva, la luna, el supermercado)"),
            ("adjetivo",  "Escribe un adjetivo (ej: valiente, torpe, brillante)"),
            ("objeto",    "Escribe un objeto (ej: sombrero, paraguas, cohete)"),
            ("color",     "Escribe un color (ej: violeta, dorado, transparente)"),
        ],
        "texto": (
            "Érase una vez un {animal} muy {adjetivo} que vivía en {lugar}.\n"
            "Un día, mientras paseaba tranquilamente, encontró un {objeto}\n"
            "de color {color} tirado en el medio del camino. Lo levantó con\n"
            "cuidado y, de repente, el {objeto} comenzó a brillar y a hablar:\n"
            "'¡Gracias por salvarme, {animal}! Ahora seremos los mejores amigos\n"
            "de {lugar} para siempre!' Y colorín colorado, este cuento ha terminado."
        ),
    },
    {
        "titulo": "Viaje al espacio",
        "tipos": [
            ("personaje", "Escribe un nombre de personaje (ej: Marta, el robot, tu mascota)"),
            ("planeta",   "Escribe un planeta o lugar del espacio (ej: Marte, una nube, el Sol)"),
            ("comida",    "Escribe una comida (ej: pizza, milanesa, chocolate)"),
            ("verbo",     "Escribe un verbo en infinitivo (ej: bailar, gritar, dormir)"),
            ("numero",    "Escribe un número entero (ej: 3, 47, 1000)"),
        ],
        "texto": (
            "{personaje} decidió un martes viajar hasta {planeta} en una nave\n"
            "construida completamente con {comida}. El viaje duró {numero} horas.\n"
            "Al llegar, los habitantes de {planeta} salieron a recibirlo y le\n"
            "pidieron que les enseñara a {verbo}, porque en ese lugar nadie\n"
            "sabía cómo hacerlo. {personaje} pasó toda la tarde enseñando,\n"
            "y resultaron ser los mejores alumnos de todo el universo conocido."
        ),
    },
    {
        "titulo": "El día en la escuela",
        "tipos": [
            ("nombre",   "Escribe un nombre propio (ej: Tomas, la directora, la maestra)"),
            ("materia",  "Escribe una materia escolar (ej: matematica, gimnasia, arte)"),
            ("animal",   "Escribe un animal (ej: loro, cocodrilo, pulpo)"),
            ("verbo",    "Escribe un verbo en infinitivo (ej: cantar, explotar, flotar)"),
            ("objeto",   "Escribe un objeto de la mochila (ej: la cartuchera, un cuaderno)"),
        ],
        "texto": (
            "Era un lunes normal cuando {nombre} llegó al colegio con un {animal}\n"
            "escondido dentro de {objeto}. La clase de {materia} estaba por empezar\n"
            "y el {animal} decidió que ese era el momento perfecto para {verbo}.\n"
            "La maestra de {materia} se sorprendió tanto que se subió al escritorio\n"
            "y declaró que desde ese día {verbo} sería parte obligatoria del programa.\n"
            "Firmado: {nombre}, el alumno más famoso de toda la historia escolar."
        ),
    },
    {
        "titulo": "El bosque mágico",
        "tipos": [
            ("animal",       "Escribe un animal del bosque (ej: zorro, oso, koala)"),
            ("fruta",        "Escribe una fruta (ej: sandia, kiwi, arándanos)"),
            ("adjetivo",     "Escribe un adjetivo (ej: misterioso, ruidoso, pequeño)"),
            ("verbo",        "Escribe un verbo en infinitivo (ej: volar, cocinar, desaparecer)"),
            ("instrumento",  "Escribe un instrumento musical (ej: trompeta, bateria, flauta)"),
        ],
        "texto": (
            "En un bosque {adjetivo} vivía un {animal} con un talento increíble:\n"
            "podía {verbo} cada vez que comía {fruta}. Un día encontró una\n"
            "{instrumento} apoyada contra un árbol enorme. La tocó con la nariz\n"
            "y, para su sorpresa, todos los árboles del bosque empezaron a bailar.\n"
            "Desde entonces, el {animal} toca la {instrumento} todas las tardes\n"
            "y reparte {fruta} gratis para que el bosque nunca deje de moverse."
        ),
    },
    {
        "titulo": "El Superheroe inesperado",
        "tipos": [
            ("nombre",     "Escribe un nombre de heroe (ej: capitán Pancho, la abuela veloz)"),
            ("superpoder", "Escribe un superpoder (ej: volar, supervelocidad, ser invisible)"),
            ("villano",    "Escribe un villano o problema (ej: el mal olor, un científico loco, un alienígena)"),
            ("ciudad",     "Escribe un lugar o ciudad (ej: villa maria, la isla, el castillo, la plaza)"),
            ("objeto",     "Escribe un objeto cotidiano (ej: una escoba, una taza, el control de la televisión)"),
        ],
        "texto": (
            "Nadie sabía que {nombre} tenía el poder de {superpoder}.\n"
            "Pero cuando {villano} amenazó con destruir {ciudad}, no había opción.\n"
            "{nombre} agarró {objeto} con ambas manos, respiró profundo,\n"
            "y usó su poder de {superpoder} para salvar a todos los habitantes.\n"
            "La gente de {ciudad} aplaudió durante tres días seguidos sin parar.\n"
            "{nombre} volvió a casa, tomó un té, y siguió siendo completamente normal."
        ),
    },
]

ARCHIVO_HISTORIAS = "historias.txt"
SEPARADOR = "*" * 50

# FUNCIONES

def mostrar_encabezado():                   #encabezado de bienvenida al juego
    print("\n" + SEPARADOR)
    print("         CUENTOS LOCOS")
    print("     Historias interactivas")
    print(SEPARADOR)


def mostrar_menu():                          #muestra opciones del submenú de cuentos locos

    print("\n" + SEPARADOR)
    print("  ¿Qué querés hacer?")
    print(SEPARADOR)
    print("  1 - Crear una nueva historia")
    print("  2 - Ver historias guardadas")
    print("  0 - Volver al menú principal")
    print(SEPARADOR)


def validar_palabra(descripcion):                                   #pide una palabra al usuario y valida que no esté vacía.
                                                                    #repite la pregunta hasta recibir un valor váido
                                                                    # usa .strip() para ignorar espacios en blanco
                                                                    # retorna la palabra ingresada como string                      

    while True:
        palabra = input("  -> " + descripcion + ": ").strip()
        if palabra == "":
            print(" No puede quedar vacío. Intentá de nuevo.")
        else:
            return palabra


def pedir_palabras(tipos):

    """recibe una lista de tuplas (clave, descripcion). Le pide al usuario una palabra par cada tipo de validación.
        Devuelve un diccionario {clave: palabra_ingresada}. Se usa diccionario para asociar el nombre del marcador (clave)
        con el valor ingresado por el usuario, para después insertarlos en la plantilla con .format(**palabras)"""
   
    print("\n  Completá las siguientes palabras sin saber la historia:")
    print("  " + "-" * 46)
    palabras = {}
    for clave, descripcion in tipos:
        palabras[clave] = validar_palabra(descripcion)
    return palabras


def elegir_plantilla():                                 #elige una plantilla al azar de la lisra PLANTILLAS
                                                        #Usa random.randit para generar un índice válido
                                                        #devuelve el diccionrio completo de la plantilla elegida.

    indice = random.randint(0, len(PLANTILLAS) - 1)
    return PLANTILLAS[indice]


def generar_historia(plantilla, palabras):              #toma el texto de la plantilla y reemplaza los marcadores
                                                        #{clave} con las palabras del diccionario usando .format().
                                                        #el operador ** desempaqueta el diccionario como argumentos.
                                                        #devuelve el string final de la historia creada

    historia = plantilla["texto"].format(**palabras)
    return historia


def mostrar_historia(titulo, historia):             #muestra la historia generada con formato en la terminal.
                                                    #convierte el titulo en mayusculas con .upper() para destacarlo.
   
    print("\n" + SEPARADOR)
    print("  " + titulo.upper())
    print(SEPARADOR)
    print()
    print(historia)
    print()
    print(SEPARADOR)


def guardar_historia(titulo, historia):                                 #guarda la historia en el archivo de texto ARCHIVO_HISTORIAS.
                                                                 #Usa modo 'a' (append) para agregar sin borrar las anteriores.
                                                                        #si el archivo no existe python lo crea automáticamente.
                                                                        #utf-8 guarda tildes y ñ sin errores.
    with open(ARCHIVO_HISTORIAS, "a", encoding="utf-8") as archivo:
        archivo.write("\n" + SEPARADOR + "\n")
        archivo.write("HISTORIA: " + titulo + "\n")
        archivo.write(SEPARADOR + "\n")
        archivo.write(historia + "\n")
    print("\n Historia guardada en '" + ARCHIVO_HISTORIAS + "'.")


def ver_historial():                                           #lee el archivo de historias guardadas y muestra su contenido.
                                    #Usa try/except para manejar el caso en que el archivo no exista todavía (primera vez que se usa el programa).

    print("\n" + SEPARADOR)
    print("      HISTORIAS GUARDADAS")
    print(SEPARADOR)
    try:
        with open(ARCHIVO_HISTORIAS, "r", encoding="utf-8") as archivo:
            contenido = archivo.read()
        if contenido.strip() == "":
            print("\n  todavía no hay historias guardadas.")
        else:
            print(contenido)
    except FileNotFoundError:              #el archivo no existe porque nynca se guardó ninguna historia
        print("\n  todavía no hay historias guardadas.")
    input("\n ENTER para continuar...")


def iniciar():                                                  #función principal del juego
                                                                #contiene el bucle del submenú y coordina todas las funciones.
                                                                #el menú principal del grupo llama a ésta función para ingresar
    
    mostrar_encabezado()
    print("\n  Te pediremos algunas palabras y las usaremos")
    print("  para crear una historia completamente inesperada.")

    continuar = True
    while continuar:
        mostrar_menu()
        opcion = input("  Ingresá tu opción: ").strip()

        if opcion == "1":
            plantilla = elegir_plantilla()
            palabras = pedir_palabras(plantilla["tipos"])
            historia = generar_historia(plantilla, palabras)
            mostrar_historia(plantilla["titulo"], historia)

            guardar = input("  ¿Querés guardar esta historia? (s/n): ").strip().lower()
            if guardar == "s":
                guardar_historia(plantilla["titulo"], historia)

            input("\n ENTER para continuar...")

        elif opcion == "2":
            ver_historial()

        elif opcion == "0":
            print("\n  volviendo al menú principal...")
            continuar = False

        else:
            print("\n Opción inválida. Ingresá 0, 1 o 2.")
