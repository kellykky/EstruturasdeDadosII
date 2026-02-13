from no import No

class AVL:
    def __init__(self):
        self.raiz = None
        self.total_rotacoes = 0
        self.palavras_distintas = 0

    # Utilitários de Altura e Balanceamento
    def _get_altura(self, no):
        if not no:
            return 0
        return no.altura

    def _get_balanceamento(self, no):
        if not no:
            return 0
        return self._get_altura(no.esquerda) - self._get_altura(no.direita)

    # Rotações
    def _rotacao_direita(self, z):
        self.total_rotacoes += 1
        y = z.esquerda
        T3 = y.direita

        y.direita = z
        z.esquerda = T3

        z.altura = 1 + max(self._get_altura(z.esquerda), self._get_altura(z.direita))
        y.altura = 1 + max(self._get_altura(y.esquerda), self._get_altura(y.direita))

        return y

    def _rotacao_esquerda(self, z):
        self.total_rotacoes += 1
        y = z.direita
        T2 = y.esquerda

        y.esquerda = z
        z.direita = T2

        z.altura = 1 + max(self._get_altura(z.esquerda), self._get_altura(z.direita))
        y.altura = 1 + max(self._get_altura(y.esquerda), self._get_altura(y.direita))

        return y

    # Inserção
    def inserir(self, palavra, linha):
        self.raiz = self._inserir_recursivo(self.raiz, palavra, linha)

    def _inserir_recursivo(self, no, palavra, linha):
        # 1. Inserção normal de BST
        if not no:
            self.palavras_distintas += 1
            return No(palavra, linha)

        if palavra < no.palavra:
            no.esquerda = self._inserir_recursivo(no.esquerda, palavra, linha)
        elif palavra > no.palavra:
            no.direita = self._inserir_recursivo(no.direita, palavra, linha)
        else:
            # Palavra já existe: apenas adiciona a linha se não for repetida
            if linha not in no.linhas:
                no.linhas.append(linha)
            return no # Não altera altura nem precisa balancear se só add linha

        # 2. Atualizar altura
        no.altura = 1 + max(self._get_altura(no.esquerda), self._get_altura(no.direita))

        # 3. Balancear
        balance = self._get_balanceamento(no)

        # Caso Esquerda-Esquerda
        if balance > 1 and palavra < no.esquerda.palavra:
            return self._rotacao_direita(no)
        # Caso Direita-Direita
        if balance < -1 and palavra > no.direita.palavra:
            return self._rotacao_esquerda(no)
        # Caso Esquerda-Direita
        if balance > 1 and palavra > no.esquerda.palavra:
            no.esquerda = self._rotacao_esquerda(no.esquerda)
            return self._rotacao_direita(no)
        # Caso Direita-Esquerda
        if balance < -1 and palavra < no.direita.palavra:
            no.direita = self._rotacao_direita(no.direita)
            return self._rotacao_esquerda(no)

        return no

    # Remoção
    def remover(self, palavra, linha):
        self.raiz = self._remover_recursivo(self.raiz, palavra, linha)

    def _get_min_value_node(self, no):
        atual = no
        while atual.esquerda is not None:
            atual = atual.esquerda
        return atual

    def _remover_recursivo(self, no, palavra, linha):
        if not no:
            return no

        # Busca do nó
        if palavra < no.palavra:
            no.esquerda = self._remover_recursivo(no.esquerda, palavra, linha)
        elif palavra > no.palavra:
            no.direita = self._remover_recursivo(no.direita, palavra, linha)
        else:
            # Nó encontrado
            if linha in no.linhas:
                no.linhas.remove(linha)
            
            # Se ainda houver linhas, o nó não deve ser removido da árvore
            if len(no.linhas) > 0:
                return no

            # Se a lista de linhas está vazia, removemos o nó da árvore
            self.palavras_distintas -= 1
            
            # Caso 1: Nó com apenas um filho ou nenhum
            if no.esquerda is None:
                temp = no.direita
                no = None
                return temp
            elif no.direita is None:
                temp = no.esquerda
                no = None
                return temp

            # Caso 2: Nó com dois filhos
            temp = self._get_min_value_node(no.direita)
            no.palavra = temp.palavra
            no.linhas = temp.linhas # Copia as linhas do sucessor
            no.direita = self._remover_no_fisico(no.direita, temp.palavra)

        if no is None:
            return no

        # Atualizar altura e Balancear
        no.altura = 1 + max(self._get_altura(no.esquerda), self._get_altura(no.direita))
        balance = self._get_balanceamento(no)

        if balance > 1 and self._get_balanceamento(no.esquerda) >= 0:
            return self._rotacao_direita(no)
        if balance > 1 and self._get_balanceamento(no.esquerda) < 0:
            no.esquerda = self._rotacao_esquerda(no.esquerda)
            return self._rotacao_direita(no)
        if balance < -1 and self._get_balanceamento(no.direita) <= 0:
            return self._rotacao_esquerda(no)
        if balance < -1 and self._get_balanceamento(no.direita) > 0:
            no.direita = self._rotacao_direita(no.direita)
            return self._rotacao_esquerda(no)

        return no

    # Função auxiliar para remover o nó fisicamente quando tem 2 filhos
    def _remover_no_fisico(self, no, palavra):
        if not no: return no
        if palavra < no.palavra: no.esquerda = self._remover_no_fisico(no.esquerda, palavra)
        elif palavra > no.palavra: no.direita = self._remover_no_fisico(no.direita, palavra)
        else:
            if no.esquerda is None: return no.direita
            elif no.direita is None: return no.esquerda
        return no

    # Busca Aproximada (Prefixo)
    def busca_aproximada(self, prefixo):
        resultados = []
        self._busca_prefixo_rec(self.raiz, prefixo, resultados)
        return resultados

    def _busca_prefixo_rec(self, no, prefixo, res):
        if not no:
            return
        
        self._busca_prefixo_rec(no.esquerda, prefixo, res)
        if no.palavra.startswith(prefixo):
            res.append(no.palavra)
        self._busca_prefixo_rec(no.direita, prefixo, res)

    # Busca com Medidor de Equilíbrio (ME)
    def contar_elementos(self, no):
        if not no:
            return 0
        return 1 + self.contar_elementos(no.esquerda) + self.contar_elementos(no.direita)

    def busca_me(self, palavra):
        no_encontrado = self._buscar_no(self.raiz, palavra)
        
        if not no_encontrado:
            return -1 # Palavra não encontrada
        
        qtd_esq = self.contar_elementos(no_encontrado.esquerda)
        qtd_dir = self.contar_elementos(no_encontrado.direita)
        me = qtd_esq - qtd_dir
        
        if me == 0:
            return 0
        else:
            print(f"Valor de ME para '{palavra}': {me}")
            return 1

    def _buscar_no(self, no, palavra):
        if not no:
            return None
        if palavra == no.palavra:
            return no
        elif palavra < no.palavra:
            return self._buscar_no(no.esquerda, palavra)
        else:
            return self._buscar_no(no.direita, palavra)

    # Palavra Mais Frequente
    def palavra_mais_frequente(self):
        self.max_linhas = -1
        self.palavra_top = ""
        
        def _percorrer(no):
            if not no: return
            _percorrer(no.esquerda)
            if len(no.linhas) > self.max_linhas:
                self.max_linhas = len(no.linhas)
                self.palavra_top = no.palavra
            _percorrer(no.direita)
            
        _percorrer(self.raiz)
        return self.palavra_top, self.max_linhas

    # Gerar Relatório
    def gerar_indice(self):
        lista_saida = []
        self._gerar_indice_rec(self.raiz, lista_saida)
        return lista_saida

    def _gerar_indice_rec(self, no, lista):
        if not no:
            return
        self._gerar_indice_rec(no.esquerda, lista)
        # Formata a string "palavra: 1, 2, 3"
        linhas_str = ",".join(map(str, no.linhas))
        lista.append(f"{no.palavra} {linhas_str}")
        self._gerar_indice_rec(no.direita, lista)