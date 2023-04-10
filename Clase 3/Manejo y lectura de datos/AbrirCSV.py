#r, leer archivos
#a, añadir al final del archivo
#w, sobreescribir los datos del archivo
#x, crear un nuevo archivo

file = open("nuevo_archivo.txt","x")
file.write("Esto es un ejemplo!")
file.close()

file = open("nuevo_archivo.txt","a")
file.write("Esto se colocara abajo de ejemplo!")
file.close()

file = open("nuevo_archivo.txt","w")
file.write("Primer reglon. \n")
file.write("Segundo reglon. \n")
file.write("Tercero reglon. \n")
file.write("Cuerto reglon. \n")
file.write("Quinto reglon. \n")
file.close()

file = open("nuevo_archivo.txt","r")
objeto = file.readlines()
print(objeto)
file.close()

file = open("DATApuntocoma.csv","r")
objeto = file.readlines()
file.close()
for linea in objeto:
    data = linea.split(';')
    # print(data)
    Nombre = data[0].strip()
    Apellido = data[1].strip()
    Email = data[2].strip()
    Genero = data[3].strip()

    print(f"Nombre: {Nombre}")
    print(f"Apellido: {Apellido}")
    print(f"Correo: {Email}")
    print(f"Genero: {Genero}")
    print("-------------------------------")
