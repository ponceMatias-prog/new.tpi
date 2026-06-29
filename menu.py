import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def run_game(filename):
    os.system(f"python {os.path.join(BASE_DIR, filename)}")

def menu():
    while True:
        print("\n===== MENÚ DE JUEGOS =====")
        print("1. ADIVINAR EL NÚMERO")
        print("2. QUIEN SABE MAS")
        print("3. Serpiente")
        print("4. Cuentos Locos")
        print("5. Salir")

        opcion = input("Selecciona una opción (1-5): ")

        if opcion == "1":
            run_game("juego_ponce.py")
        elif opcion == "2":
            run_game("juego.maldo.py")
        elif opcion == "3":
            run_game("ferrero.py")
        elif opcion == "4":
            run_game("main.py")
        elif opcion == "5":
            print("👋 Saliendo del menú...")
            break
        else:
            print("Opción inválida, intenta de nuevo.")

if __name__ == "__main__":
    menu()
