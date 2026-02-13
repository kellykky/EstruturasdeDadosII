README – Índice Remissivo com Árvore AVL

Introdução

O objetivo deste trabalho foi desenvolver um índice remissivo a partir de um texto, associando cada palavra às linhas em que ela aparece. 

O código foi feito com base em uma árvore binária de busca auto-balanceada do tipo AVL. A escolha dessa estrutura se justifica pela necessidade de manter as operações de inserção e busca com desempenho eficiente, mesmo com grande volume de palavras. A árvore AVL garante altura balanceada, mantendo a complexidade das operações principais em O(log n).

O problema do índice remissivo foi resolvido da seguinte forma: o texto é lido linha por linha; cada linha é normalizada (remoção de pontuação e conversão para minúsculas); as palavras são extraídas e inseridas na árvore juntamente com o número da linha correspondente. Quando uma palavra já existe na árvore, apenas a nova linha é adicionada à sua lista de ocorrências. Ao final, a árvore é percorrida em ordem (in-order), produzindo as palavras em ordem alfabética, cada uma acompanhada das linhas em que aparece.

Estruturas de Dados Utilizadas

A estrutura principal é a Árvore AVL, implementada com nós que armazenam:

A palavra (chave de ordenação);

Uma lista de números de linha onde a palavra ocorre;

Referências para os filhos esquerdo e direito;

A altura do nó, utilizada no cálculo do fator de balanceamento.

Cada nó é representado pela classe No, cujo construtor recebe a palavra e o número da linha inicial. A lista de linhas é iniciada com esse primeiro valor.

A classe AVL é responsável por todas as operações sobre a árvore, incluindo inserção, balanceamento por rotações, buscas e geração do índice final.

Documentação do Código

Arquivo no.py

A classe No define a estrutura básica de cada elemento da árvore. Seus atributos são:

palavra: string que funciona como chave de ordenação;

linhas: lista de inteiros com os números das linhas onde a palavra aparece;

esquerda e direita: referências para os filhos;

altura: inteiro que representa a altura do nó na árvore.

Essa classe não implementa lógica de balanceamento; ela apenas representa o elemento estrutural da árvore.

Arquivo avl.py

A classe AVL implementa a árvore propriamente dita. Entre suas principais responsabilidades estão:

Inserção de palavras: o método inserir(palavra, linha) posiciona a palavra conforme as regras de árvore binária de busca. Se a palavra já existir, apenas adiciona o número da linha à lista correspondente. Caso contrário, cria um novo nó.

Atualização de altura: após cada inserção, a altura dos nós é recalculada.

Cálculo do fator de balanceamento: a diferença entre as alturas das subárvores esquerda e direita é utilizada para verificar se o nó está desbalanceado.

Rotações: quando o fator de balanceamento ultrapassa os limites permitidos (-1, 0 ou 1), são realizadas rotações simples (à esquerda ou à direita) ou rotações duplas, garantindo que a árvore permaneça balanceada.

Busca de palavra: permite verificar se um termo está presente e obter informações associadas.

Busca aproximada: retorna palavras que começam com determinado prefixo, percorrendo a árvore e filtrando os termos.

Palavra mais frequente: percorre a árvore para identificar a palavra que aparece no maior número de linhas.

Geração do índice: realiza percurso em ordem (in-order), produzindo uma lista de strings no formato “palavra: linhas”.

A classe também mantém contadores, como o total de palavras distintas e o número total de rotações realizadas durante a construção da árvore.

Arquivo main.py

O arquivo principal coordena a execução do programa. Suas etapas são:

Leitura do arquivo de texto por meio da função carregar_texto, que retorna as linhas do arquivo.

Processamento de cada linha:

Remoção de pontuação com expressão regular;

Conversão para minúsculas;

Separação em palavras.

Inserção das palavras na árvore AVL, junto com o número da linha.

Execução de testes de funcionalidades:

Busca de um termo específico;

Busca por prefixo;

Identificação da palavra mais frequente.

Geração do arquivo de saída indice_remissivo.txt, contendo o índice e estatísticas como:

Total de palavras lidas;

Total de palavras distintas;

Palavras descartadas;

Tempo de construção;

Total de rotações realizadas.

Exemplos de Uso

Considere o seguinte texto de entrada:

Linha 1: Estruturas de dados são importantes
Linha 2: Árvores são estruturas eficientes

Durante o processamento, as palavras são normalizadas (minúsculas e sem pontuação) e inseridas na árvore:

arvore.inserir("estruturas", 1)
arvore.inserir("dados", 1)
arvore.inserir("sao", 1)
arvore.inserir("importantes", 1)
arvore.inserir("arvores", 2)
arvore.inserir("sao", 2)
arvore.inserir("estruturas", 2)
arvore.inserir("eficientes", 2)

Como “sao” e “estruturas” já existiam, apenas a linha 2 é adicionada às suas listas.

Ao gerar o índice (percurso em ordem), a saída será:

arvores: 2
dados: 1
eficientes: 2
estruturas: 1, 2
importantes: 1
sao: 1, 2

Exemplo de busca aproximada:

arvore.busca_aproximada("es")

Possível saída:

["estruturas", "eficientes"]

Exemplo de palavra mais frequente:

arvore.palavra_mais_frequente()

Saída possível:

("estruturas", 2)

