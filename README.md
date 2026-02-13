Índice Remissivo utilizando Árvore AVL
1. Introdução

Este trabalho tem como objetivo a construção de um índice remissivo a partir de um arquivo de texto, relacionando cada palavra às linhas em que aparece. O índice remissivo permite organizar informações de forma estruturada e facilita a consulta posterior dos termos presentes no texto.

Para a implementação da solução foi utilizada uma Árvore AVL, que é uma árvore binária de busca auto-balanceada. Essa estrutura foi escolhida por garantir eficiência nas operações de inserção e busca, mantendo complexidade O(log n), mesmo com o crescimento da quantidade de dados.

O projeto foi dividido em dois arquivos principais:

avl.py, responsável pela implementação da árvore AVL;

main.py, responsável pela leitura do arquivo e construção do índice.

2. Estrutura da Solução

A árvore AVL armazena as palavras em ordem alfabética. Cada nó da árvore contém:

A palavra (chave);

Uma lista com os números das linhas onde a palavra ocorre;

Referências para os filhos esquerdo e direito;

A altura do nó, utilizada para controle do balanceamento.

Durante a inserção, caso a palavra já exista na árvore, apenas a linha correspondente é adicionada à lista de ocorrências. Caso contrário, um novo nó é criado.

O balanceamento da árvore é mantido por meio de rotações simples ou duplas, sempre que o fator de balanceamento ultrapassa os limites permitidos (-1, 0 ou 1).

3. Funcionamento do Índice Remissivo

O processo de construção do índice ocorre da seguinte forma:

O arquivo é lido linha por linha.

As palavras são separadas e normalizadas (conversão para minúsculas e remoção de pontuação).

Cada palavra é inserida na Árvore AVL juntamente com o número da linha.

Ao final, a árvore é percorrida em ordem (in-order), garantindo que as palavras sejam exibidas em ordem alfabética.

Esse procedimento gera um índice organizado e eficiente para consulta.

4. Documentação do Código
4.1 Arquivo avl.py

Contém a implementação da estrutura da árvore AVL.

Classe Node
Representa cada nó da árvore, armazenando a palavra, a lista de linhas e informações necessárias para o balanceamento.

Classe AVLTree
Responsável pelas operações principais:

insert() – Insere palavras e realiza o balanceamento.

left_rotate() – Executa rotação à esquerda.

right_rotate() – Executa rotação à direita.

get_height() – Retorna a altura do nó.

get_balance() – Calcula o fator de balanceamento.

in_order() – Percorre a árvore em ordem alfabética.

4.2 Arquivo main.py

Responsável por:

Ler o arquivo de entrada;

Processar e normalizar as palavras;

Inseri-las na árvore AVL;

Exibir o índice remissivo final.

5. Exemplo de Uso
Entrada:
Estruturas de dados são importantes.
Árvores são estruturas eficientes.

Saída:
arvores: 2
dados: 1
eficientes: 2
estruturas: 1, 2
importantes: 1
sao: 1, 2


As palavras são apresentadas em ordem alfabética, seguidas das linhas em que aparecem.

