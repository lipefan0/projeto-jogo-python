# Personagem: classe mae
# Hero: controlado pelo jogador
# Enemy: adversario do jogador

import random


class Personagem:
    def __init__(self, nome, vida, nivel) -> None:
        self.__nome = nome
        self.__vida = vida
        self.__nivel = nivel
    
    def get_nome(self):
        return self.__nome
    
    def get_vida(self):
        return self.__vida
    
    def get_nivel(self):
        return self.__nivel
    
    def exibir_detalhes(self):
        return f"Nome: {self.get_nome()}\nVida: {self.get_vida()}\nNivel: {self.get_nivel()}"
    
    def receber_dano(self, dano):
        self.__vida -= dano
        if self.__vida <= 0:
            self.__vida = 0

    def atacar(self, alvo):
        dano = random.randint(self.get_nivel() * 2, self.get_nivel() * 4)
        alvo.receber_dano(dano)
        print(f"{self.get_nome()} atacou {alvo.get_nome()} e causou {dano} de dano")

    def habilidade_especial(self, alvo):
        dano = random.randint(self.get_nivel() * 5, self.get_nivel() * 7)
        alvo.receber_dano(dano)
        print(f"{self.get_nome()} usou habilidade especial {self.get_habilidade()} em {alvo.get_nome()} e causou {dano} de dano")
    
    
class Hero(Personagem):
    def __init__(self, nome, vida, nivel, habilidade):
        super().__init__(nome, vida, nivel)
        self.__habilidade = habilidade

    def get_habilidade(self):
        return self.__habilidade
    
    def exibir_detalhes(self):
        return f"{super().exibir_detalhes()}\nHabilidade: {self.get_habilidade()}\n"
    
class Enemy(Personagem):
    def __init__(self, nome, vida, nivel, tipo):
        super().__init__(nome, vida, nivel)
        self.__tipo = tipo

    def get_tipo(self):
        return self.__tipo
    
    def exibir_detalhes(self):
        return f"{super().exibir_detalhes()}\nTipo: {self.get_tipo()}"


class Jogo:
    """ Classe orquestradora do jogo """
    def __init__(self) -> None:
        self.heroi = Hero(nome="Heroi", vida=100, nivel=5, habilidade="Bola de fogo")
        self.inimigo = Enemy(nome="Morcego", vida=50, nivel=5, tipo="Voardor")

    def iniciar_batalha(self):
        """Fazer a gestão da batalha em turnos"""
        print("Batalha iniciada")
        while self.heroi.get_vida() > 0 and self.inimigo.get_vida() > 0:
            print("\nDetalhes dos personagens")
            print(self.heroi.exibir_detalhes())
            print(self.inimigo.exibir_detalhes())
            
            input("Pressione enter para atacar...")
            escolha = input("Escolha 1 - Ataque normal, 2 - Ataque Especial: ")

            if escolha == "1":
                self.heroi.atacar(self.inimigo)

            elif escolha == "2":
                self.heroi.habilidade_especial(self.inimigo)
            else:
                print("Escolha invalida, tente novamente")
                continue
            
            if self.inimigo.get_vida() > 0:
                self.inimigo.atacar(self.heroi)

        if self.heroi.get_vida() > 0:
            print("Heroi venceu a batalha")
        else:
            print("Inimigo venceu a batalha")
# Cria instancia do jogo e iniciar a batalha

jogo = Jogo()
jogo.iniciar_batalha()
