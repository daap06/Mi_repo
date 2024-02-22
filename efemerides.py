# definimos el diccionario
efemerides = {'1 de Enero': 'Año Nuevo',
    '27 de Febrero': 'Terremoto en Chile',
    '8 de Marzo': 'Día de la Mujer',
    '21 de Mayo': 'Glorias Navales',
    '18 de Septiembre': 'Fiestas Patrias',
    '19 de Septiembre': 'Glorias del Ejercito',
    '25 de Diciembre': 'Navidad'}

# Con python comprehension creo un nuevo diccionario y modifico sus valores a minusculas para evitar errores al ingresar datos.
efemerides_minus = {k.lower(): v.lower() for k, v in efemerides.items()}

fecha_consulta = input("Ingrese una fecha: ").lower()

print(f'Efemérides: {efemerides_minus.get(fecha_consulta,"No hay eventos para esta fecha.")}´')


