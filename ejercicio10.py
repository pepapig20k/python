import time 

tiempo = time.localtime()

hora = tiempo.tm_hour

if hora >= 19:
    print("Es hora de ir a la casa.")
else:
    tiempo_restante = 19 - hora
    print(f"quedan {tiempo_restante} horas de trabajo")