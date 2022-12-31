def bisiesto(año):
    if año % 4 == 0 and (año % 100 != 0 or año % 400 ==0):
        print(f"El {año} es biciento")
        
    else:
        print(f"El año {año} no es biciesto")

bisiesto(2151)