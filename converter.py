## Función conversor de temperatura ##
def convert_temperature():
    print("¿Qué quieres convertir?")
    print("1. Celsius a Fahrenheit")
    print("2. Fahrenheit a Celsius")
    choice = int(input("Selecciona: "))
    if choice == 1:
        temp = float(input("Introduce la temperatura en grados Celsius: "))
        print(f"{temp} grados Celsius equivalen a {(temp*9/5)+32} grados Fahrenheit.")
    elif choice == 2:
        temp = float(input("Introduce la temperatura en grados Fahrenheit: "))
        print(f"{temp} grados Fahrenheit equivalen a {(temp-32)*5/9} grados Celsius.")
    else:
        print("Tienes que seleccionar 1 o 2, no es tan complicado.")

## Función conversor de medida ##

## Interfaz ## 
print("===== Bienvenido al Conversor de Cosas =====")
while 1:
    print("Which option would you like to choose:-")
    print("1. Convert temperature")
    print("2. Convert currency")
    print("3. Convert lengths")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        convert_temperature()
    elif choice != 1:
        print("Función todavía no disponible.")