recordatorios = [['2021-01-01', "11:00", "Levantarse y ejercitar"],
    ['2021-05-01', "15:00", "No trabajar"],
    ['2021-07-15', "13:00", "No hacer nada es feriado"],
    ['2021-09-18', "16:00", "Ramadas"],
    ['2021-12-25', "00:00", "Navidad"]]

# Output
#Agregar evento
recordatorios.insert(0,["2021-02-02", "06:00", "Empezar el Año"])
#Modificar evento
recordatorios[3] =  ['2021-07-16', "13:00", "No hacer nada es feriado"]
#Eliminar evento
del recordatorios[2]
#Agregar cena de navidad y año nuevo
recordatorios.extend([['2021-12-24', '22:00', 'Cena de Navidad'],['2021-12-31', '22:00', 'Cena de Año Nuevo']])
#Ordeno la lista de eventos
recordatorios.sort()

print(recordatorios)

for recordatorio in recordatorios:
    print(recordatorio)