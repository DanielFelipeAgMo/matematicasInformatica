alumnos = set()

while True:
    print("\nMenú:")
    print("1. Agregar alumno")
    print("2. Verificar alumno")
    print("3. Eliminar alumno")
    print("4. Lista de alumnos")
    print("5. Salir")
    
    opcion = input("Ingrese el número de la opción: ")
    
    if opcion == "1":
        nombre = input("Ingrese el nombre del alumno: ")
        alumnos.add(nombre)
        print(f"{nombre} ha sido agregado a la lista de alumnos.")
    elif opcion == "2":
        nombre = input("Ingrese el nombre del alumno: ")
        if nombre in alumnos:
            print(f"{nombre} está registrado en la clase.")
        else:
            print(f"{nombre} no está registrado en la clase.")
    elif opcion == "3":
        nombre = input("Ingrese el nombre del alumno a eliminar: ")
        if nombre in alumnos:
            alumnos.remove(nombre)
            print(f"{nombre} ha sido eliminado de la lista de alumnos.")
        else:
            print(f"{nombre} no está registrado en la clase.")
    elif opcion == "4":
        print("\nLista de alumnos:")
        for alumno in alumnos:
            print(alumno)
    elif opcion == "5":
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida. Por favor, elija una opción válida del menú.")
