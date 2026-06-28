
import random
ponce_matias = "Adivina el número"


def ponce():
    print("Ejecutando Juego:" , ponce_matias)

    limite = int(input("¿Hasta qué número máximo querés jugar?: "))
    numero_secreto = random.randint(1, limite)
    intento = 0
    max_intentos = int(input("Cantidad de intentos: "))
    intentos_realizados = 0
    

    while intento != numero_secreto and  intentos_realizados < max_intentos:
        intento = int(input(f"Valor de 1 a {limite}: "))
        intentos_realizados += 1

        if intento < numero_secreto:
            print(" Demasiado bajo...", intentos_realizados, "/ ", max_intentos, " intentos")
        elif intento > numero_secreto:
            print(" Demasiado alto...", intentos_realizados, "/ ", max_intentos, " intentos")
        else:
            print("Exelente,  El número era :", numero_secreto)
            porcentaje = (intentos_realizados / max_intentos) * 100
            print("Porcentaje de intentos realizados: ", porcentaje, "%")


    if intentos_realizados == max_intentos and intento != numero_secreto:
        print("Perdedor...  El número secreto era", numero_secreto)

    jugar_otra = input("¿Querés jugar otra vez? (S/N): ").upper()
    if jugar_otra == "S":
      ponce()

ponce()

    