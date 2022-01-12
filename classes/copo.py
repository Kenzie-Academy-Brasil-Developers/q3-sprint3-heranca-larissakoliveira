# Desenvolva sua classe Copo aqui.
from .recipiente import Recipiente

class Copo(Recipiente):
    
    def __init__(self, tamanho: float):
        super().__init__(tamanho)


    def encher(self, bebida: str = 'água'):
        if not self.limpo:
            return 'Não se pode encher um copo sujo'
        else:
            self.sujar()
            self.conteudo = self.tamanho
            self.bebida = bebida

    def beber(self, quantidade: float):
        if quantidade < 0:
            return "Quantidade deve ser positiva"
        if quantidade > self.conteudo:
            return "Não há bebida suficiente no copo"
        else:
            self.conteudo -= quantidade
    
    def lavar(self):
        self.bebida = None
        self.esvaziar()
        self.limpo = True

    def __str__(self) -> None:
        if self.conteudo == 0:
            return f"Um copo vazio de {float(self.tamanho)}ml"
        else:
            return f"Um copo de {float(self.tamanho)}ml contendo {float(self.conteudo)}ml de {self.bebida}"
        
    def __repr__(self) -> None:
        if self.conteudo == 0:
             return f"Um copo vazio de {float(self.tamanho)}ml"
        else:
            return f"Um copo de {float(self.tamanho)}ml contendo {float(self.conteudo)}ml de {self.bebida}"


