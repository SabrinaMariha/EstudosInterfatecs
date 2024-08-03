##https://judge.beecrowd.com/pt/runs/code/40724354
#Aqui foi usada uma estratégia de leitura diferente já que esse problema pode estourar o tempo de execução facilmente. A biblioteca sys permite que o input leia todas as linhas 
#do documento.txt.
## a variavel data irá guardar uma lista que conterá cada linha do documento

import math
import sys
input = sys.stdin.read

def main():
    data = input().strip().split('\n')
    
    index = 0
    cidade = 1

    while index < len(data):
        
        numeroCasas = int(data[index].strip())
        index += 1
        
        if numeroCasas == 0:
            break
        
        print(f'Cidade# {cidade}:')
        
        consumoMedioCidade = 0
        consumoMedioENumeroPessoas = {}

        for _ in range(numeroCasas):
            numeroMoradores, consumoMoradores = map(int, data[index].strip().split())
            index += 1
            
            consumoMedioCasa = math.floor(consumoMoradores / numeroMoradores)
            
            if consumoMedioCasa not in consumoMedioENumeroPessoas:
                consumoMedioENumeroPessoas[consumoMedioCasa] = numeroMoradores
            else:
                consumoMedioENumeroPessoas[consumoMedioCasa] += numeroMoradores
            
            consumoMedioCidade += consumoMoradores
        
        consumoPorCasaOrdenado = dict(sorted(consumoMedioENumeroPessoas.items(), key=lambda item: item[0]))

        for consumo, pessoas in consumoPorCasaOrdenado.items():
            print(f"{pessoas}-{consumo}", end=" ")
        print()
        
        if consumoMedioENumeroPessoas:
            consumoMedioCidade /= sum(consumoMedioENumeroPessoas.values())
            truncated = math.floor(consumoMedioCidade * 100) / 100
        print(f"Consumo medio: {truncated:.2f} m3.", end="")
        
        cidade += 1
        if index<len(data)-1:
            print("\n")

main()
