recordatorios = [['2021-01-01', "11:00", "Levantarse y ejercitar"],
    ['2021-05-01', "15:00", "No trabajar"],
    ['2021-07-15', "13:00", "No hacer nada es feriado"],
    ['2021-09-18', "16:00", "Ramadas"],
    ['2021-12-25', "00:00", "Navidad"]]

#Función para mostrar lista de recordatorios con indice.
def mostrar_recordatorios(recordatorios):
    for indice, recordatorio in enumerate(recordatorios):
        print(f"Recordatorio {indice +1}: {recordatorio}")
    print(f"\n")



#Agregar eventos de forma dinámica.
while True:
    tiene_mas_evento = input("Tiene más eventos que agregar? (s/n)").lower()
    if tiene_mas_evento != "s" and tiene_mas_evento != "n":
        print("Ingrese un valor válido (s/n)")
    else:
        break
    
if tiene_mas_evento == "s":
    while True:
        fecha = input("Agregue la fecha (Ej: 2021-01-01): (e para salir)")
        if fecha != "e":
            hora = input("Agregue la hora (Ej: 06:00): ")
            evento = input("Agregue el evento (Ej: cumpleaños): ")     
            recordatorios.append([f"{fecha}", f"{hora}", f"{evento}"])
        else:
            break

recordatorios.sort()

#Llamo función para mostrar recordatorios y que el usuario pueda escoger el que desea eliminar.
mostrar_recordatorios(recordatorios)

#Eliminar recordatorios.
while True:    
    eliminar_evento = input("Desea eliminar eventos? (s/n)").lower()
    if eliminar_evento != "s" and eliminar_evento != "n":
        print(f"Ingrese un valor válido (s/n)"
            f"\n")
    else:
        break
        
if eliminar_evento =="s":
    while True:
        eliminar_evento = input("Ingrese el indice del recordatorio a eliminar : (e para salir)").lower()
        if eliminar_evento != "e":
            try:
                del recordatorios[int(eliminar_evento) - 1]
                mostrar_recordatorios(recordatorios)
            except ValueError:
                print("Ingrese un parámetro valido (s/n o números)")
        else:
            break

#Modificar recordatorios.
while True:
    modificar_evento = input("Desea modificar eventos? (s/n)").lower()
    if modificar_evento != "s" and modificar_evento != "n":
        print("Ingrese un valor válido (s/n)"
        f"\n")
    else:
        break

if modificar_evento =="s":
    while True:
        modificar_evento = input("Ingrese el indice del recordatorio a modificar : (e para salir)").lower()
        if modificar_evento != "e":
            fecha = input("Agregue la nueva fecha (Ej: 2021-01-01): ")
            hora = input("Agregue la nueva hora (Ej: 06:00): ")
            evento = input("Agregue el nuevo evento (Ej: cumpleaños): ")     
            recordatorios[int(modificar_evento) - 1] = ([f"{fecha}", f"{hora}", f"{evento}"])
        else:
            break

recordatorios.sort()

print(f"\n"
    f"**********Recordatorios***********\n")
mostrar_recordatorios(recordatorios)