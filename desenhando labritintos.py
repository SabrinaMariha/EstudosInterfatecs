nCasos=int(input())

for _ in range(nCasos):
    comeco=input()
    v,a = map(int, input().split())

    listaAd=[[] for i in range(v)]


    for i in range(a):
        origem,destino=map(int, input().split())
        if origem not in listaAd[destino]:
            listaAd[destino].append(origem)
        if destino not in listaAd[origem]:
            listaAd[origem].append(destino)
       
    
    somaConexoes=sum([len(listaAd[i]) for i in range(v)])
    print(listaAd)
    print(str(somaConexoes))