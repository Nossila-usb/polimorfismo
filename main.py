import  classes as cl

if __name__ == '__main__':
    # entrada de dados
    nome = input('Informe o nome do usuário: ')
    email = input('Informe o e-mail do usuário: ')
    cpf = input('Informe o CPF do usuário: ')
    profissao = input('Informe a profissão do usuário: ')
    endereco = input('Informe o endereco do usuário: ')
    telefone = input('Informe o telefone do usuário: ')

    # instacia a classes pessoa fisica
    usuario = cl.PessoaFisica(nome, cpf, profissao, endereco, email, telefone, )

    # entrada de dados
    nome = input('Informe o nome da empresa: ')
    email = input('Informe o e-mail da empresa: ')
    cnpj = input('Informe o CNPJ da empresa: ')
    razao_social = input('Informe a Razão social da empresa: ')
    endereco = input('Informe o endereco da empresa: ')
    telefone = input('Infoeme o telefone da empresa: ')
    # instancia a classe pessoa juridica
    empresa = cl.PessoaJuridica(nome, razao_social, cnpj, endereco, email, telefone)

    # saida de dados
    print(f'{'-'*30} DADOS DO USUÁRIO {'-'*30}\n')
    usuario.mostrar_cartao_visitas()
    print(f'{'-'*30} DADOS DE EMPRESA {'-'*30}\n')
    empresa.mostrar_cartao_visitas()
    