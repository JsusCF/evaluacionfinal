alumno = {"Codigo": ["001", "002", "003", "004"],
          "Nombre": ["Jesus", "Carlos", "Luis", "Juan"],
          "Cursos": ["Algoritmos", "Diseño Web", "Soporte de TI"]}
notas = []
continuar = True
while continuar:
    codigo = input("Ingrese el codigo del alumno: ")
    curso = input("Ingrese el curso a tomar las notas: ")
    nota1 = int(input("Ingrese la  nota 1 : "))
    nota2 = int(input("Ingrese la nota 2: "))
    nota3 = int(input("Ingrese la nota 3: "))
    x = 0
    for i in alumno["Codigo"]:
        if i == codigo:
            codigotemp = i
            nombretemp = alumno["Nombre"][x]
            prom = (nota1 + nota2 + nota3)/3
            registro = ["Codigo: " + str(codigotemp) + "\n" + "Nombre: " + str(nombretemp) + "\n" + "Cursos: " + curso + "\n" + "Nota 1: " + str(nota1) + "\n" + "Nota 2: " + str(nota2) + "\n" + "Nota 3: " + str(nota3) + "\n" + "Promedio: " + str(prom) + "\n"]
            f = open("notas.txt", "a")
            cadena = "".join(registro)
            f.write("\n" + cadena)
            f.close()
        x += 1
    continuar = input("¿Desea seguir ingresando datos? : s/n ") == "s"
f = open("notas.txt")
print(f.read())
f.close()