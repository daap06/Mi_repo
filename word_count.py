import sys
try:
    if len(sys.argv) !=2:
        raise ValueError("Falta un parámetro, por favor verifique.")
    try:
        nombre_txt = sys.argv[1]
        with open(f"{nombre_txt}", "r") as file:
            texto = file.read()
        caracteres = set(texto)    
        tex_separado = texto.split(" ")

        palabras_unicas = set(tex_separado)
        print(f"El número de palabras distintas es:",len(caracteres))
        print(f"El número de palabras distintas es:",len(palabras_unicas))
    except:
        raise ValueError("El formato de alguno de los parámetros ingresados no es valido. por favor verifique.")

except ValueError as e:
    print("Error: ",e)
