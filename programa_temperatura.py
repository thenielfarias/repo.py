userInput=input("Digite a temperatura atual: ")

if int(userInput) < 7:
    print("Congelando! " + userInput + "Cº")
elif int(userInput) < 10:
    print("Frio! " + userInput + "Cº")
elif int(userInput) > 26:
    print("Ótimo! " + userInput + "Cº")
else:
    print("Agradável " + userInput + "Cº")