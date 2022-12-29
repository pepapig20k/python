print("Calcula tu inidce de masa corporal")
print("")

peso = float(input("Digita tu peso en kg: "))
estatura = float(input("Indicame tu estatura en metros: "))
imc = peso / estatura**2

print(f"Tu indice de masa corporal es: {imc:.2f}")
