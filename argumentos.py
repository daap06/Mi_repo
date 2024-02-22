import sys

nombre = sys.argv[1]
apellido = sys.argv[2]
edad = sys.argv[3]

print(f"Mi nombre es {nombre}")
print(f"Mi apellido es {apellido}")
print(f"Mi edad es {edad}")
print(f" nombre de este archivo es {sys.argv[0]}")
print(type(sys.argv))