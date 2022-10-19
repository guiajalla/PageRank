def tamPageRank(str): #Função que irá verificar o Tamanho que terá a Matriz
    tam = 0
    for i in str:
        tam += 1
    return tam

def completePageRank(str, tam): #Função para completar o pageRank
    matriz = []

    linha = defineRow(str)
    matriz.append(linha)
    
    cont = 1
    while cont < tam:
        no = input("Digite o no: ")
        linha = defineRow(no)
        matriz.append(linha)
        cont +=1

    return matriz

def defineRow(str):
    linha = []
    for i in str:
        numero = int(i)
        linha.append(numero)
    return linha

def setAimPageRank(matriz, tam): #função responsável por verificar para quantos cada um aponta
    aimPageRank = []
    for i in range(tam):
        nos = 0
        for j in range(tam):
            if(matriz[i][j]==1):
                nos += 1
        aimPageRank.append(nos)
    return aimPageRank

def setPageRank(matrizPageRank, aimPageRank, tam): #Função responsável pelo cálculo do Pagerank
    pageRank = []
    d = 0.85
    k = 0

    for i in range(tam):
        pageRank.append(1.0)
    
    while k < 100:
        for i in range(tam):
            temp = 0.0
            for j in range(tam):
                if (matrizPageRank[j][i]==1):
                    temp = temp + (pageRank[j]/aimPageRank[j])
            pageRank[i] = (1 - d) + (d*temp)
        k+=1
    return pageRank

def showPageRank(pageRank, tam): #Função irá mostrar o PageRank
    for i in range(tam):
        print('%.2f' % pageRank[i])

def main():
    firstNo = input('Digite a primeira linha(no) do pageRank: ')
    tampageRank = tamPageRank(firstNo)
    matrizPageRank = completePageRank(firstNo, tampageRank)
    aimPageRank = setAimPageRank(matrizPageRank, tampageRank)
    pageRank =  setPageRank(matrizPageRank, aimPageRank, tampageRank)
    showPageRank(pageRank, tampageRank)

if __name__ == "__main__":
    main()