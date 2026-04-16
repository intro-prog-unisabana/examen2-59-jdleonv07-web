# temp_monitor.py
# Libreria de funciones para registrar lecturas de temperatura.
#
# Estructura del diccionario (monitor):
#   - 'max':      numero maximo de lecturas permitidas (int)
#   - 'readings': lista con las temperaturas de cada lectura (list)
#   - 'total':    suma total de todas las temperaturas (float)


def init(max_readings):
    
    return {"max": max_readings, "readings": [], "total": 0.0}

    
    # TODO: Implementar
    pass


def add_reading(monitor, temp):

    monitor["readings"].append(values) 
    monitor["total"] = monitor["total"] + values 
    return monitor

    # TODO: Implementar
    pass


def count(monitor):
    return len(monitor("readings"))

    # TODO: Implementar
    pass


def average_temp(monitor):
   if count(monitor) == 0:
        return 0.0
   return monitor["total"] / count(monitor)


    # TODO: Implementar
   pass


def format_readings(monitor):

    lista = monitor["readings"]
    texto = "["

    i = 0
    while i < len(lista):
        texto = texto + str(lista[i])
        if i < len(lista) - 1:
            texto = texto + ", "
        i = i + 1
    texto = texto + "]"

    return texto 

    

    


    # TODO: Implementar
    pass


def highest_temp(monitor):
   lista = monitor["readings"]
   maximo = lista[0]

   for valor in lista:
        if valor > maximo:
            maximo = valor

   return maximo

    # TODO: Implementar
   pass


def coldest_window(monitor, k):
    lista = monitor["readings"]
    n = len(lista)

    # suma inicial
    suma = 0
    i = 0
    while i < k:
        suma = suma + lista[i]
        i = i + 1

    min_promedio = suma / k

    i = k
    while i < n:
        suma = suma - lista[i - k]
        suma = suma + lista[i]

        promedio = suma / k
        if promedio < min_promedio:
            min_promedio = promedio

        i = i + 1
  
    return min_promedio

    # TODO: Implementar
    pass


def longest_rising_streak(monitor):
    """
    Retorna la longitud maxima de una secuencia de lecturas consecutivas
    donde las temperaturas aumentan estrictamente.
    """
    # TODO: Implementar
    pass


def main():
    # crear un monitor para temperaturas de Bogota (12 horas, 6am-5pm)
    monitor = init(12)
    monitor = add_reading(monitor, 8.0)   # 6am
    monitor = add_reading(monitor, 9.5)   # 7am
    monitor = add_reading(monitor, 11.0)  # 8am
    monitor = add_reading(monitor, 13.5)  # 9am
    monitor = add_reading(monitor, 15.0)  # 10am
    monitor = add_reading(monitor, 17.5)  # 11am
    monitor = add_reading(monitor, 19.0)  # 12pm
    monitor = add_reading(monitor, 20.0)  # 1pm
    monitor = add_reading(monitor, 19.5)  # 2pm
    monitor = add_reading(monitor, 18.0)  # 3pm
    monitor = add_reading(monitor, 16.5)  # 4pm
    monitor = add_reading(monitor, 15.0)  # 5pm

    # imprimir estadisticas
    print("numero de lecturas =", count(monitor))               # 12
    print("temp promedio =", average_temp(monitor))             # 15.208...
    print("temp mas alta =", highest_temp(monitor))             # 20.0
    print("ventana mas fria (3) =", coldest_window(monitor, 3)) # 9.5
    print("racha creciente =", longest_rising_streak(monitor))  # 8

    # imprimir temperaturas
    print(format_readings(monitor))


if __name__ == "__main__":
    main()
