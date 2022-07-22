import requests

class AcessaCep:
    def __init__(self, cep):
        cep = str(cep)
        if self.valida_cep(cep):
            self.cep = cep

    def __str__(self):
        return self.formata_cep()

    def valida_cep(self, cep):
        if len(cep) == 8:
            return True
        else:
            raise ValueError("Cep inválido!")

    def formata_cep(self):
        return f"{self.cep[:5]}-{self.cep[5:]}"

    def acessa_via_cep(self):
        url = f"https://viacep.com.br/ws/{self.cep}/json/"
        consulta_recebida = requests.get(url)
        dados_consulta = consulta_recebida.json()
        return (
            dados_consulta['bairro'],
            dados_consulta['localidade'],
            dados_consulta['uf']
        )