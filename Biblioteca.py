#--------- tentando fazer o algoritmo corretamente, vou ter que simular as deslocações
# dos livros para esquerda uma por uma

quantidadeLivros=3
entrada="NMH"
listaOrdenada=[] #lista que irá simular a biblioteca orgazinada por ordem alfabética
listaFinal=[] #Estado final da desorganização dos livros dada pelo exercício


posicaoAlfabetica=0
posicaoBaguncada=0
contador=0
for i in entrada:
    listaFinal.append(i)
    listaOrdenada.append(i)
    

listaOrdenada.sort() #essa será usada para fazer os deslocamentos até ficar igual à bagunçada
print("\nlista ordenada (como se fosse a biblioteca organizada): ", listaOrdenada)
print("Lista desorgazinada (como se fosse o estado da biblioteca depois dos alunos baguncarem:)",listaFinal)
print("\n\n")
while(listaOrdenada!=listaFinal): #enquanto as listas não ficarem iguais

    for i in range(0, quantidadeLivros): #percorro de 0 até 3(quantidade de livros)
        posicaoAlfabetica = listaOrdenada.index(listaOrdenada[i]) #vejo a posição da primeira letra na lista ordenada
        posicaoBaguncada = listaFinal.index(listaOrdenada[i]) ##vejo a posição da primeira letra na lista bagunçada
       
        diferencaPosicao = posicaoBaguncada - posicaoAlfabetica
        # quando os livros forem para esquerda a diferença será negativa

        if diferencaPosicao < 0:  # o primeiro caso será o N, q dará -2
            for j in range(0, abs(diferencaPosicao)): # vou mover o N na lista auxiliar 2 vezes 
                temp = listaOrdenada[posicaoAlfabetica - j]
                listaOrdenada[posicaoAlfabetica - j] = listaOrdenada[posicaoAlfabetica - (j + 1)]
                listaOrdenada[posicaoAlfabetica - (j + 1)] = temp
                contador+=1
                print("Lista depois da alteração:", listaOrdenada)
        #terei como resultado outra lista e vou ter que verificar se já ficou igual



print("Lista resultante:", listaOrdenada)
print("Quantidade de movimentos que foram necessários para bagunçar ela assim:", contador)
      
