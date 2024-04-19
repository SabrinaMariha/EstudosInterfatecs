dicionario={1:"A",2:"B",3:"C",4:"D",5:"E", 6:"F", 7:"H", 8:"I", 9:"J", 10:"K", 11:"L", 12:"M", 13:"N", 14:"O", 15:"P", 16:"Q", 17:"R", 18:"S", 19:"T", 20:"U", 21:"V", 22:"W", 23:"X", 24:"Y", 25:"Z",26:"."}

entrada = input()
entradaLista= entrada.split()
numero=int(entradaLista[0])
formato=entradaLista[1]
letras=""
saida="."*26
for i in range(1,numero+1):
    if (formato=="maiuscula"):
        letras+=dicionario[i] # A AB ABC ABCD ABCDE
        print(saida[1:-i]+letras)
    else:#A AB
        letras+=dicionario[i].lower() # A AB ABC ABCD ABCDE
        print(saida[1:-i]+letras)
#.....A
#....AB
#...ABC
#..ABCD
