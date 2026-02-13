import time
import re
from avl import AVL

def carregar_texto(nome_arquivo):
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as f:
            return f.readlines()
    except FileNotFoundError:
        print(f"Erro: Arquivo {nome_arquivo} não encontrado.")
        return []

def main():
    arvore = AVL()
    nome_arquivo = 'texto_origem.txt'
    linhas = carregar_texto(nome_arquivo)
    
    total_palavras_lidas = 0
    
    print("Construindo índice...")
    inicio = time.time()
    
    # Processamento do texto
    for numero_linha, conteudo in enumerate(linhas, start=1):
        # Substitui pontuação por espaço e converte para minúsculo
        # Mantém letras (a-z) e dígitos, remove o resto
        conteudo_limpo = re.sub(r'[^\w\s]', ' ', conteudo).lower()
        palavras = conteudo_limpo.split()
        
        for p in palavras:
            # Ignora palavras vazias ou muito curtas
            if p.strip() and len(p) > 1:
                arvore.inserir(p, numero_linha)
                total_palavras_lidas += 1
                
    fim = time.time()
    tempo_construcao = fim - inicio
    
    # Testes das Funcionalidades
    
    # 1. Busca ME
    termo_busca = "que" # Pode ser alterado para testar outros termos
    print(f"\nBusca ME para: '{termo_busca}'")
    res_me = arvore.busca_me(termo_busca)
    if res_me == -1:
        print("Resultado: Palavra não encontrada no texto.")
    elif res_me == 0:
        print("Resultado: A palavra está perfeitamente equilibrada (ME = 0).")
    else:
        print("Resultado: A palavra foi encontrada e não está equilibrada.")

    # 2. Busca Aproximada
    prefixo = "con" # Pode ser alterado para testar outros prefixos
    print(f"\nBusca Aproximada para prefixo: '{prefixo}'")
    lista_prefixo = arvore.busca_aproximada(prefixo)
    print(lista_prefixo)

    # 3. Palavra mais frequente
    top_palavra, qtd = arvore.palavra_mais_frequente()
    print(f"\nEstatística")
    print(f"Palavra mais frequente: '{top_palavra}' (aparece em {qtd} linhas)")

    # 4. Gerar Arquivo de Saída
    print(f"\nGerando arquivo de saída: indice_remissivo.txt")
    itens_indice = arvore.gerar_indice()
    
    total_descartadas = total_palavras_lidas - arvore.palavras_distintas
    
    with open('indice_remissivo.txt', 'w', encoding='utf-8') as f:
        f.write("Índice Remissivo:\n")
        for item in itens_indice:
            f.write(item + "\n")
            
        f.write("Estatísticas:\n")
        f.write(f"Total de palavras: {total_palavras_lidas}\n")
        f.write(f"Total de palavras distintas: {arvore.palavras_distintas}\n")
        f.write(f"Total de palavras descartadas: {total_descartadas}\n")
        f.write(f"Tempo de construção: {tempo_construcao:.4f}s\n")
        f.write(f"Total de rotações: {arvore.total_rotacoes}\n")

    print("Concluído!")

if __name__ == "__main__":
    main()