# Desenvolva sua classe Recipiente aqui.


class Recipiente:
    def __init__(self, tamanho: float) -> None:
        self.tamanho = tamanho if tamanho > 0 else 0
        self.conteudo = float(0)
        self.limpo = True

    def esvaziar(self) -> None:
        self.conteudo = 0
    
    def esta_vazio(self) -> bool:
        if self.conteudo == 0:
            return True

    def lavar(self) -> None:
        self.conteudo = 0
        self.limpo = True

    def esta_limpo(self) -> bool:
        if self.limpo:
            return True

    def estado(self) -> str:
        if self.limpo:
            return 'limpo'
        else:
            return 'sujo'

    def sujar(self) -> None:
        self.limpo = False

    def __str__(self) -> str:
        return f'Um recipiente {self.estado()} não especificado'

    def __repr__(self) -> str:
        return f'Um recipiente {self.estado()} não especificado'