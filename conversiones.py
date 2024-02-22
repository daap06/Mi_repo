import sys
try:
    if len(sys.argv) !=5:
        raise ValueError("Falta un parámetro, por favor verifique.")
        
    try: 
        tasa_sol = float(sys.argv[1])
        tasa_peso_argent = float(sys.argv[2])
        tasa_dolar_americ = float(sys.argv[3])
        moneda_local = float(sys.argv[4])
    except:
        raise ValueError("El formato de alguno de los parámetros ingresados no es valido. por favor verifique.")
        
    tasas = {
            'soles': tasa_sol,
            'pesos argentinos': tasa_peso_argent,
            'dolares': tasa_dolar_americ,
        }
    
    conver_pesos = {f"conversion a {nombre_divisa}": tasa * moneda_local for nombre_divisa, tasa in tasas.items()}

    print(f"Los {moneda_local:.0f} pesos equivalen a:\n"
        f"{conver_pesos['conversion a soles']} Soles\n"
        f"{conver_pesos['conversion a pesos argentinos']} Pesos Argentinos\n"
        f"{conver_pesos['conversion a dolares']} Dólares\n")

except ValueError as e:   
    print("Error:", e)