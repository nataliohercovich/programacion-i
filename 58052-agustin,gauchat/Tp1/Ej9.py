datos = {'nombre' : None, 'edad' : None, 'direccion' : None, 'telefono' : None}

d = input("Ingrese su nombre: ")
datos['nombre'] = d

d = input("Ingrese su edad: ")
datos['edad'] = d

d = input("Ingrese su direccion: ")
datos['direccion'] = d

d = input("Ingrese su telefono: ")
datos['telefono'] = d

print(datos['nombre'] + " tiene " + datos['edad'] + " años, vie en " + datos['direccion'] + " y su numero de telefono es " + datos['telefono'])