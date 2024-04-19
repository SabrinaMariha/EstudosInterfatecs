#para executar uma funcao, é só chamar ela abaixo da lista de funcoes no fim do arquivo ex: colocar no fim do arquivo "strip()" sem aspas

def lowerUpper(): #deixa maiuscula ou minuscula
    entrada="Olá, mundo!"
    print(entrada.upper())
    print(entrada.lower())

def strip(): #Remove espaços em branco do início e do fim da string.
    entrada="  Olá, mundo! "
    print(entrada.strip())
    print(entrada.lstrip())
    print(entrada.rstrip())

def split(): #Divide a string em substrings se encontrar instâncias do separador
    entrada="Olá, mundo!"
    print(entrada.split())
    print(entrada.split(","))
    print(entrada.split(" "))

def join(): #Junta os elementos de uma lista usando um separador
    entrada=["1", "2", "3", "4", "5"]
    print("sem o join:"+entrada)
    print(",".join(entrada))
    