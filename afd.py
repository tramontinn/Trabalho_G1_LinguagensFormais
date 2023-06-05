class AFD:
    def __init__(self, estados, simbolos, transicoes, estado_inicial, estados_finais):
        self.estados = estados
        self.simbolos = simbolos
        self.transicoes = transicoes
        self.estado_inicial = estado_inicial
        self.estados_finais = estados_finais

    def executar(self, entrada):
        estado_atual = self.estado_inicial

        for simbolo in entrada:
            if (estado_atual, simbolo) in self.transicoes:
                estado_atual = self.transicoes[(estado_atual, simbolo)]
            else:
                return False

        return estado_atual in self.estados_finais


estados = input("Informe os estados do autômato separados por vírgula: ").split(',')
simbolos = input("Informe os símbolos do autômato separados por vírgula: ").split(',')

transicoes = {}
print("Informe as transições de estados:")
while True:
    entrada = input("Estado atual (ou digite 'sair' para finalizar): ")
    if entrada == 'sair':
        break
    simbolo = input("Símbolo: ")
    proximo_estado = input("Próximo estado: ")
    transicoes[(entrada, simbolo)] = proximo_estado

estado_inicial = input("Informe o estado inicial do autômato: ")
estados_finais = input("Informe os estados finais do autômato separados por vírgula: ").split(',')

automato = AFD(estados, simbolos, transicoes, estado_inicial, estados_finais)

while True:
    entrada = input("Digite uma palavra (ou digite 'sair' para finalizar): ")
    if entrada == 'sair':
        break
    if automato.executar(entrada):
        print("A palavra é aceita pelo autômato.")
    else:
        print("A palavra não é aceita pelo autômato.")
