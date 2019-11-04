# luiza_labs_challenge
Repositório destinado ao desafio para vaga de desenvolvedor na Luiza Labs.
- Vitor Lorente

## Preparando o ambiente


Primeiro, clone o repositório:
`git clone https://github.com/VitorLorente/luiza_labs_challenge.git`


### Dependências

Em seguida, instale as dependências no ambiente virtual:
`pipenv install`


### PostgreSQL

1. Crie um banco de dados vazio no postgreSQL (e guarde bem seu nome, pois iremos precisar):
2. `sudo -su postgres` ;
3. `psql` ;
4. `CREATE DATABASE database_name OWNER your_user` ;


### Variáveis de ambiente

1. Crie um arquivo chamado `env.py` na raíz do projeto;
2. Copie o conteúdo do arquivo `env-sample.py` (também na raiz do projeto) e cole no arquivo `env.py`;
3. No dicionário `env_datas`, preencha os valore de `db` com o nome do seu banco de dados, `user` com o nome do usuário para se conectar ao postgreSQL e `psswd` com a senha de acesso ao postgreSQL;


### Criando tabelas no banco de dados
A partir de um shell na raiz do projeto, rode o comando:
`python manage.py migrate <customers_number>`,
onde `<customer_number>` é um valor inteiro opcional, representando o número de clientes a serem criados. Caso o argumento não seja passado para o comando, a tabela de clientes não será populada.
