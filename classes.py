# superclasse, classe-pai, classe base
class Pessoa:
    # atributos
    def __init__(self, endereco, email, telefone):
        self.endereco = endereco
        self.email = email
        self.telefone = telefone

    # metodo
    def mostrar_cartao_visitas(self):
        print(f'Endereço: {self.endereco}.')
        print(f'E-mail: {self.email}.')
        print(f'Telefone: {self.telefone}.')

# sub-classe, classe-filha, classe derivada Pessoa Fesica
class PessoaFisica(Pessoa):
    # polimorfismo do construtor
    def __init__(self,  nome, cpf, profissao, endereco, email, telefone,):
        self.nome = nome
        self.cpf = cpf
        self.profissao = profissao
        super(). __init__(endereco, email, telefone)
    
    def mostrar_cartao_visitas(self):
        print(f'Nome de usuário: {self.nome}.')
        print(f'CPF do usuário: {self.cpf}.')
        print(f'Profissão do usuário: {self.profissao}.')
        super().mostrar_cartao_visitas()      

class PessoaJuridica(Pessoa):
    # polimorfismo do construtor
    def __init__(self, nome_fantasia, razao_social, cnpj, endereco, email, telefone):
        self.nome_fantasia = nome_fantasia
        self.razao_social = razao_social
        self.cnpj = cnpj
        super().__init__(endereco, email, telefone)

         
    def mostrar_cartao_visitas(self):
        print(f'Nome_fantasia de usuário: {self.nome_fantasia}.')
        print(f'CNPJ do usuário: {self.cnpj}.')
        print(f'Razão social do usuário: {self.razao_social}.')
        super().mostrar_cartao_visitas()      
    
