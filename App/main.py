import os

# NIM - Jogo de estratégia
# Consiste em dois jogadores irem tirando bolinhas dentro de um conjunto
# O ultimo que tira a bolinha ganha
# Mas, tem uma estrategia de ganhar sempre...

class Main:
    def __init__(
        self
    ):
        self.clear_page # limpar a tela
        self.ganhos_computador: int = 0 # ganhos do computador no campeonato
        self.ganhos_usuario: int = 0 # ganhos do usuario no campeonato
        self.partida_total: int = 1 # total de partidas jogas por campeonato

        self.inicir() # inicio da aplicação
    
    # Início da partida
    def inicir(self):
        texto = 'Bem Vindo ao NIM\n\n1. Campeonato\n2. Partida Unica\n0. Sair: '

        while True:
            opcao = input(texto)
            
            self.clear_page
            if opcao in ['0', '1', '2']:
                if opcao == '0':
                    exit()
                
                elif opcao == '1':
                    self.campeonato()
                
                elif opcao == '2':
                    self.escolher_jogadas()

            else:
                self.clear_page
                print('Opção inválida, tente novamente\n')
    

    # Lógica para escolha de jogadas e escolha do primeiro jogador
    def escolher_jogadas(self, campeonato: bool = False) -> tuple[int, int]:

        while True:
            try:
                pecas = int(input('Quantas peças?: '))

                if pecas <= 0:
                    self.clear_page
                    print('Peças inválidas, tente novamente\n')

                else:
                    break
            
            except:
                self.clear_page
                print('Peças inválidas, tente novamente\n')
        
        while True:
            try:
                jogadas = int(input('Quantas jogadas?: '))

                if jogadas <= 0:
                    self.clear_page
                    print('Jogadas inválidas, tente novamente\n')
                
                elif jogadas > pecas:
                    self.clear_page
                    print('As jogadas não devem superar as peças, tente novamente\n')

                else:
                    break
            
            except:
                self.clear_page
                print('Jogadas inválidas, tente novamente\n')
        
        self.clear_page
        if pecas % (jogadas + 1) == 0: # com base no resto da divisão analisa quem deve começar
            return self.usuario_escolhe_jogada(pecas, jogadas, campeonato)

        else:
            return self.computador_escolhe_jogada(pecas, jogadas, campeonato)

    # Gestão do campeonato (tres partidas no máximo)
    def campeonato(self):
        if self.partida_total <= 3:
            print(f'=====PARTIDA {self.partida_total} de 3=====')
            self.escolher_jogadas(campeonato=True)
        
        else:
            print(f'Plagar: Computador: {self.ganhos_computador} x {self.ganhos_usuario} Usuário\n')
            
            self.jogar_de_novo(campeonato=True)

    # Jogadas do usuário
    def usuario_escolhe_jogada(self, pecas: int, jogadas: int, campeonato: bool):
        
        while True:
            try:
                n = int(input(f'Resta(m) {pecas} peça(s) no tabuleiro\nQuantas peças vai tirar?: '))

                if n > jogadas:
                    self.clear_page
                    print('O número não pode ser superior ao máximo de jogadas, tente novamente\n')
                
                elif n > pecas:
                    self.clear_page
                    print('O número de peças escolhido está acima das peças restantes\n')
                
                else:
                    break

            except:
                self.clear_page
                print('Número inválido, tente novamente\n')
        
        self.clear_page

        pecas -= n
        if pecas == 0:
            print('O Usuário ganhou a partida🎉\n')

            if campeonato == True:
                self.ganhos_usuario += 1
                self.partida_total += 1
                return self.campeonato()

            else:
                self.jogar_de_novo(campeonato)
        
        else:
            return self.computador_escolhe_jogada(pecas, jogadas, campeonato)

    # Jogadas do computador
    def computador_escolhe_jogada(self, pecas: int, jogadas: int, campeonato: bool):
        
        n = 1
        while n <= jogadas:

            if (pecas - n) % (jogadas + 1) == 0: # mesma lógica do escolher jogadas
                break
            
            else:
                n += 1
        
        pecas -= n
        print(f'O computador jogou {n} peça(s)\n')

        if pecas == 0:
            self.clear_page
            print('O computador ganhou🎉\n')

            if campeonato == True:
                self.ganhos_computador += 1
                self.partida_total += 1
                return self.campeonato()

            else:
                self.jogar_de_novo(campeonato)
        
        else:
            return self.usuario_escolhe_jogada(pecas, jogadas, campeonato)
    
    # Jogar de novo
    def jogar_de_novo(self, campeonato: bool):

        while True:
            opcao = input('Deseja jogar de novo? (S/N): ').upper()
            
            self.clear_page
            if opcao == 'S':
                

                if campeonato == True:
                    self.ganhos_computador = 0
                    self.ganhos_usuario = 0
                    self.partida_total = 1
                    return self.campeonato()
                
                else:
                    return self.escolher_jogadas(campeonato)
                
            else:
                exit()
        
    @property
    def clear_page(self):
        try:
            os.system('cls')
        
        except:
            os.system('clear')

if __name__ == '__main__':
    Main()