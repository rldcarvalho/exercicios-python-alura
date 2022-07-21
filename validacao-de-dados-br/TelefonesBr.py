import re

class TelefonesBR:

    def __init__(self, telefone):
        telefone = str(telefone)
        if self.valida_numero(telefone):
            self.telefone = telefone
        else:
            raise ValueError("Número incorreto!")

    def __str__(self):
        return self.formata_numero()

    def valida_numero(self, telefone):
        padrao = "(([0-9]{2})?([0-9]{2})([0-9]{4,5})([0-9]{4}))"
        resposta = re.findall(padrao, telefone)
        if resposta:
            return True
        else: return False

    def formata_numero(self):
        padrao = "(([0-9]{2})?([0-9]{2})([0-9]{4,5})([0-9]{4}))"
        resposta = re.search(padrao, self.telefone)
        print(resposta.group(2))
        return f"+{resposta.group(2)} ({resposta.group(3)}) {resposta.group(4)}-{resposta.group(5)}"