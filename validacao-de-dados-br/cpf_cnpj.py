from validate_docbr import CPF, CNPJ

class Documento:

    @staticmethod
    def cria_documento(documento):
        documento = str(documento)
        if len(documento) == 11:
            return DocCpf(documento)
        elif len(documento) == 14:
            return DocCnpj(documento)
        else:
            raise ValueError("Número de caracteres do documento inválido!")

class DocCpf:

    def __init__(self, documento):
        if self.cpf_e_valido(documento):
            self.cpf = documento
        else:
            raise ValueError("CPF inválido!")

    def cpf_e_valido(self, cpf):
        validador = CPF()
        return validador.validate(cpf)

    def formata_cpf(self):
        formata = CPF()
        return formata.mask(self.cpf)

    def __str__(self):
        return self.formata_cpf()

class DocCnpj:

    def __init__(self, documento):
        if self.cnpj_e_valido(documento):
            self.cnpj = documento
        else:
            raise ValueError("CNPJ inválido!")

    def cnpj_e_valido(self, cnpj):
        validador = CNPJ()
        return validador.validate(cnpj)

    def formata_cnpj(self):
        formata = CNPJ()
        return formata.mask(self.cnpj)

    def __str__(self):
        return self.formata_cnpj()
