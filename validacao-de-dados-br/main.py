from acesso_cep import AcessaCep

cep = 36309538
objeto_cep = AcessaCep(cep)
print(objeto_cep)
bairro, cidade, uf = objeto_cep.acessa_via_cep()
print(bairro, cidade, uf)
