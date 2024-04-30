while(True):
    try:
    


        caracter=""
        placa=""
        entrada=input() #pegando a linha da entrada
        entradaSep=entrada.split(" ")#separando em uma lista


        for i in entradaSep: #percorrendo os valores da lista
            caracter=chr(int(i)) #transformando de ASCII para Caracter
            placa+=caracter #junto os caracteres em uma placa

        #vendo se os 3 primeiros caracteres da placa são letras, o quarto um numero, o quinto uma letra e os dois últimos um número
        if(placa[0].isalpha() and placa[1].isalpha() and placa[2].isalpha() and placa[3].isnumeric() and placa[4].isalpha() and placa[5].isnumeric() and placa[6].isnumeric()):
            print("MERCOSUL")

        #vendo se os 3 primeiros são letras e os outros quatro são numeros
        elif(placa[0].isalpha() and placa[1].isalpha() and placa[2].isalpha() and placa[3].isnumeric() and placa[4].isnumeric() and placa[5].isnumeric() and placa[6].isnumeric()):
            print("ANTIGA")

            #se não se encaixar em nenhum dos casos acima, a placa é inválida
        else:
            print("ERRO")
    



    except EOFError: #ERRO QUE FAZ PARA DE PEDIR ENTRADA
        break
