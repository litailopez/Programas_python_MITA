# suma numeros en un rango

def sumarango(ini,fin):
    s=0
    for i in range(ini,fin+1):
        s=s+i
    return s

print(f"La suma del Rango es {sumarango(1,3)}")