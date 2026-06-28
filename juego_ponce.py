
import random
ponce_matias = "Adivina el número"

def ponce():
    print("Ejecutando Juego:" , ponce_matias)
    
    numero_secreto = random.randint(1, 1000)
    intento = None
    max_intentos = int(input("Cantidad de intentos: "))
    intentos_realizados = 0

    while intento != numero_secreto and  intentos_realizados < max_intentos:
        intento = int(input("Valor de 0 a 1000 :"))
        intentos_realizados += 1

        if intento < numero_secreto:
            print(" Demasiado bajo...", intentos_realizados, "/ ", max_intentos, " intentos")
        elif intento > numero_secreto:
            print(" Demasiado alto...", intentos_realizados, "/ ", max_intentos, " intentos")
        else:
            print("Exelente,  El número era :", numero_secreto)

    if intentos_realizados == max_intentos and intento != numero_secreto:
        print("Perdedor...  El número secreto era", numero_secreto)