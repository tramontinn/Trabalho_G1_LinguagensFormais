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


estados = {'q0', 'q1', 'q2', 'q3'}
simbolos = {'0', '1', '2'}
transicoes = {('q0', '0'): 'q1', ('q0', '1'): 'q0', ('q1', '0'): 'q2', ('q1', '1'): 'q0', ('q2', '0'): 'q2', ('q2', '1'): 'q2'}
estado_inicial = 'q0'
estados_finais = {'q3'}

automato = AFD(estados, simbolos, transicoes, estado_inicial, estados_finais)

entrada = input("Digite uma sequência de 0 e 1s: ")

if automato.executar(entrada):
    print("A sequência é aceita pelo autômato.")
else:
    print("A sequência não é aceita pelo autômato.")
