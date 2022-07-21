from cpf_cnpj import Documento

cpf = 12354367996
objeto_cpf = Documento.cria_documento(cpf)
print(objeto_cpf)

cnpj = 99789348000177
objeto_cnpj = Documento.cria_documento(cnpj)
print(objeto_cnpj)
