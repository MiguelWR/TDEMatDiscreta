#Nomes: Marcelo Eduardo Lins; Maria Luiza Barbosa Gandin; Miguel Wihby Rezende

from collections import OrderedDict  # Importa a classe OrderedDict do módulo collections

class OrderedSet(OrderedDict):  # Define uma classe OrderedSet que herda de OrderedDict
    def __init__(self, iterable=None):  # Define o método de inicialização da classe
        super().__init__((item, None) for item in iterable or [])  # Chama o método de inicialização da classe pai

    def add(self, item):  # Define um método para adicionar elementos ao conjunto
        self[item] = None  # Adiciona o elemento ao conjunto

    def UniaoOrdem(self, other):  # Define um método para realizar a união ordenada de conjuntos
        return OrderedSet(self.keys() | other.keys())  # Retorna a união dos conjuntos mantendo a ordem

    def IntersecaoOrdem(self, other):  # Define um método para realizar a interseção ordenada de conjuntos
        return OrderedSet(self.keys() & other.keys())  # Retorna a interseção dos conjuntos mantendo a ordem

    def DiferncaOrdem(self, other):  # Define um método para realizar a diferença ordenada de conjuntos
        return OrderedSet(self.keys() - other.keys())  # Retorna a diferença dos conjuntos mantendo a ordem

    def ProdutoCartesianoOrdem(self, other):  # Define um método para calcular o produto cartesiano ordenado de conjuntos
        return OrderedSet((x, y) for x in self for y in other)  # Retorna o produto cartesiano dos conjuntos mantendo a ordem

def LerArquivo(ArquivoTxt):  # Define uma função para ler um arquivo de texto
    with open(ArquivoTxt, 'r') as arquivo:  # Abre o arquivo em modo de leitura
        linhas = arquivo.readlines()  # Lê todas as linhas do arquivo
        NumOpercaoes = int(linhas[0])  # Obtém o número de operações do arquivo
        operacoes = []  # Inicializa uma lista para armazenar as operações
        for i in range(1, len(linhas), 3):  # Itera sobre as linhas do arquivo em grupos de três
            tipo_op = linhas[i].strip()  # Obtém o tipo de operação
            conjunto1 = OrderedSet(map(str.strip, linhas[i+1].split(',')))  # Cria um conjunto ordenado a partir da segunda linha do grupo
            conjunto2 = OrderedSet(map(str.strip, linhas[i+2].split(',')))  # Cria outro conjunto ordenado a partir da terceira linha do grupo
            operacoes.append((tipo_op, conjunto1, conjunto2))  # Adiciona a operação à lista de operações
        return NumOpercaoes, operacoes  # Retorna o número de operações e a lista de operações

# Definições de funções para realizar operações entre conjuntos
def uniao(conjunto1, conjunto2):  # Define uma função para realizar a união entre conjuntos
    return conjunto1.UniaoOrdem(conjunto2)  # Retorna a união ordenada dos conjuntos

def intersecao(conjunto1, conjunto2):  # Define uma função para realizar a interseção entre conjuntos
    return conjunto1.IntersecaoOrdem(conjunto2)  # Retorna a interseção ordenada dos conjuntos

def diferenca(conjunto1, conjunto2):  # Define uma função para calcular a diferença entre conjuntos
    return conjunto1.DiferncaOrdem(conjunto2)  # Retorna a diferença ordenada dos conjuntos

def ProdutoCartesiano(conjunto1, conjunto2):  # Define uma função para calcular o produto cartesiano entre conjuntos
    return conjunto1.ProdutoCartesianoOrdem(conjunto2)  # Retorna o produto cartesiano ordenado dos conjuntos

def RealizarOperacoes(operacoes):  # Define uma função para realizar as operações especificadas
    resultados = []  # Inicializa uma lista para armazenar os resultados das operações
    for TipoOperacao, conjunto1, conjunto2 in operacoes:  # Itera sobre as operações
        if TipoOperacao == 'U':  # Se a operação for uma união
            resultado = OrderedSet(list(conjunto1) + list(conjunto2))  # Calcula a união dos conjuntos
            NomeOp = "União"  # Define o nome da operação
        elif TipoOperacao == 'I':  # Se a operação for uma interseção
            resultado = OrderedSet([item for item in conjunto1 if item in conjunto2])  # Calcula a interseção dos conjuntos
            NomeOp = "Interseção"  # Define o nome da operação
        elif TipoOperacao == 'D':  # Se a operação for uma diferença
            resultado = OrderedSet([item for item in conjunto1 if item not in conjunto2])  # Calcula a diferença dos conjuntos
            NomeOp = "Diferença"  # Define o nome da operação
        elif TipoOperacao == 'C':  # Se a operação for um produto cartesiano
            resultado = OrderedSet(ProdutoCartesiano(conjunto1, conjunto2))  # Calcula o produto cartesiano dos conjuntos
            NomeOp = "PD"  # Define o nome da operação
        ResultadoStr = ", ".join(map(str, resultado))  # Converte o resultado para uma string
        resultados.append(f"{NomeOp}: conjunto 1 {{{', '.join(map(str, conjunto1))}}}, conjunto 2 {{{', '.join(map(str, conjunto2))}}}. Resultado: {{{ResultadoStr}}}")  # Adiciona o resultado à lista de resultados
    return resultados  # Retorna a lista de resultados das operações

def main():  # Define a função principal do programa
    NomeArquivo = input("Coloque o nome do arquivo desejado: ")  # Solicita ao usuário o nome do arquivo
    NumOperacoes, operacoes = LerArquivo(NomeArquivo)  # Lê as operações do arquivo
    resultados = RealizarOperacoes(operacoes)  # Realiza as operações especificadas
    for resultado in resultados:  # Itera sobre os resultados das operações
        print(resultado)  # Imprime cada resultado

if __name__ == "__main__":  # Se este script estiver sendo executado como o programa principal
    main()  # Chama a função principal
