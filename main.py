alumno = {}
notas = []
continuar = True
while continuar:
    codigo = int(input("Ingrese el codigo del alumno "))
    nombre = input("Ingrese el nombre del alumno ")
    cursos = input("Ingrese los cursos a tomar las notas ")
    x = 0
    for i in range(3):
        nota = int(input("Ingrese las nota correspondientes "))
        notas.append(nota)
        x += 1
    continuar = input("¿Desea seguir ingresando datos? : s/n ") == "s"
print(alumno)