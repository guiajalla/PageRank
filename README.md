# PageRank
implementação de algoritmo PageRank para a cadeira de Inteligência Artificial - IFRS - Campus Canoas

enunciado da questão:

Implemente um algoritmo em qualquer linguagem suportada pelo VPL (C, Python, Java e PHP foram testados e confirmados) para calcular o PageRank de um grafo dado como entrada em forma e matriz de adjacências.

Exemplo de entrada, onde cada linha e coluna representa um nó do grafo (1 indica que o nó representado pela linha tem uma conexão com o nó representado pela coluna):

0110
0010
1000
0010

Representa o grafo do material de aula (A liga com B e C, B liga com C, C liga com A e D liga com C):



A saída, neste caso, teria 4 linhas (1 para cada nó do grafo, todos com precisão de 2 casas decimais):

1.49
0.78
1.58
0.15

O programa deve suportar grafos de qualquer tamanho. Use d=0.15 e K=100. (cuidado: na aula eu me confundi e usei o d de 2 formas opostas, o correto é que ele é a probabilidade de saltar para outra página e 0.15 é o valor usado pelo Google. 0.85 é 1-d no caso)

Dica: Após ler a primeira linha de entrada, já dá para saber quantas linhas são (= número de caracteres), pois a matriz de adjacências é quadrada (#linhas = #colunas).
