#Projeto de TAG 3 - Universidade de Brasilia
#Rodrigo Mamedio Arrelaro - 190095164

#Imports com macros, facilitando escrita
#random para gerar tables e numeros
#comando copy para passar valores sem referencia de objeto
import random as rd
import copy as cp


def montar_grafo():
    #Monta a lista de adjacências do tabuleiro de sudoku
    #Montagem por linhas e colunas, respectivamente. ranges grandes para formatacao
    linhas = [[x for x in range(y-9,y)] for y in range(9,82,9)]

    colunas = [[x*9+y for x in range(9)] for y in range(9)]

    blocos = [[[x for x in range(z-27,z) if y-3 <= x%9 < y]
        for y in range(3,10,3)] for z in range(27,82,27)]

    lista_adjacencias = []
    for x in range(81):
        adjs = [y for y in blocos[x//27][x%9//3] if y!=x]
        adjs += [y for y in linhas[x//9] if y!=x and y not in adjs]
        adjs += [y for y in colunas[x%9] if y!=x and y not in adjs]
        lista_adjacencias.append(adjs)

    return lista_adjacencias



def pode_colorir(grafo, coloracao, vertice, cor):
    #Realize check para pintura
    if coloracao[vertice] == cor:
        return True
    if coloracao[vertice] != 0:
        return False
    if cor not in [coloracao[x] for x in grafo[vertice]]:
        return True
    else:
        return False



def colorir_util(grafo, coloracao, vertice, print_flag):
    #Coloraçao funcao de forma recursiva -> O(n^2)
    #Check se v'ertices estao coloridos e retorna booleano, iteracao baseada em cor para table
    #Caso nao possuir cor, nao possui solucao
    if vertice == 81:
        return True
    if vertice%50 == 0 and print_flag:
        print("Solucao media:")
        print_sudoku(coloracao)
        print("")

    for cor in range(1,10):
        if pode_colorir(grafo, coloracao, vertice, cor):
            pre_color = True
            if not coloracao[vertice]:
                pre_color = False
                coloracao[vertice] = cor
            if colorir_util(grafo, coloracao, vertice+1, print_flag):#chamada recursiva para checar se o vértice com essa cor faz parte da solução
                return True
            if not pre_color:
                coloracao[vertice] = 0

    return False



def colorir(grafo, proposta, print_flag):
    #Retorna a coloração do grafo a partir da proposta
    if not colorir_util(grafo, proposta, 0, print_flag):
        return False

    return proposta



def print_sudoku(coloracao):
    #Output da table
    for x in enumerate(coloracao):
        if x[0]%27 == 0:
            print("-"*28)
        if x[0]%3 == 0 and x[0]%9 != 0:
            print("|", end='')
        print(x[1], end='  ')
        if x[0]%9 == 8:
            print()

    print("-"*28)


def gerar_proposta(grafo):
    #Gerador de proposta
    #Entrega table montada
    proposta = [0]*81
    num = rd.randrange(1,10)
    proposta[0] = num
    resolvido = colorir(grafo, proposta, False)
    num_clues = rd.randrange(17,51)
    proposta = [0]*81
    i = 0
    while len([x for x in proposta if x!=0]) < num_clues:
        if rd.randrange(4) == 0:
            proposta[i%81] = resolvido[i%81]
        i += 1
    return proposta




def test():
    g = montar_grafo()
    p = gerar_proposta(g)
    print_sudoku(p)
    print_sudoku(colorir(g,p,False))






def main():
    proposta = [9,0,0, 0,0,0, 0,0,0,
                2,0,7, 0,0,0, 0,0,8,
                0,0,6, 0,8,0, 5,0,4,

                0,0,2, 0,0,3, 0,0,6,
                7,0,4, 2,0,0, 3,0,0,
                0,3,0, 8,0,0, 0,0,0,

                0,0,0, 0,1,0, 9,4,0,
                0,0,0, 6,0,0, 0,0,0,
                0,7,8, 9,0,0, 1,0,0]
    grafo = montar_grafo()
    while True:
        print("Proposta:")
        print_sudoku(proposta)
        print("")
        resolvido = colorir(grafo, proposta, True) 
        if not resolvido:
            print("Sem solucoes possiveis")
        else:
            print("Solucao final:")
            print_sudoku(resolvido)
        cont = input("Gerar outro jogo? (s/n)")
        if cont == "n":
            break
        elif cont == "s":
            proposta = gerar_proposta(grafo)



if __name__ == "__main__":
    main()
