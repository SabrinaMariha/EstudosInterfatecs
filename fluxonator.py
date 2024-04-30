numero = int(input())
for i in range(numero):
    L1 = True
    L2 = True
    L3 = True
    entrada = input()
    saida = ""
    for j in range(len(entrada)):
        if entrada[j] == 'B':
            if L2 == True:
                saida += "D"
            else:
                saida += "E"
            L2 = not L2 #Troca 
        elif entrada[j] == 'A':
            if L1 == True:
                saida += "D"
            else:
                if L2 == True:
                    saida += "D"
                else:
                    saida += "E"
                L2 = not L2
            L1 = not L1
        elif entrada[j] == 'C':
            if L3 == False:
                saida += "E"
            else:
                if L2 == True:
                    saida += "D"
                else:
                    saida += "E"
                L2 = not L2
            L3 = not L3
    print(saida)