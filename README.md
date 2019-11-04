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


## Testando a aplicação


### Servidor

Para subir o servidor, rode o seguinte comando a partir de um shell na raiz do projeto:
`python manage.py serverup`


### URL's

As seguintes URL's estão disponiveis:
1. Listagem de clientes  (método GET)-> `127.0.0.1:8080/cliente/` ;
2. Detalhes do cliente de ID <cliente_id> (método GET)-> `127.0.0.1:8080/cliente/<cliente_id>/` ;
3. Criar um novo cliente (método POST) -> `127.0.0.1:8080/cliente/create/`. Formato do json esperado:
    ```
    {
      "name": "nome_do_cliente",
      "email": "email_do_cliente"
    }
    ```
4. Atualiza informações de um cliente (método PUT)-> `127.0.0.1:8080/cliente/<cliente_id>/update/`. Formato do json esperado:
    ```
    {
      "name": "novo_nome",
      "email: "novo_email"
    }
    ``` 
    (é possível atualizar somente um dos dois atributos também);
5. Deleta o cliente de id <cliente_id> (método DELETE)-> `127.0.0.1:8080/cliente/<cliente_id>/delete/`;
6. Exibe lista de produtos favoritos do cliente de id <cliente_id> (método GET) -> `127.0.0.1:8080/cliente/<cliente_id>/favorites-list/` ;
7. Adiciona um produto à lista de produtos do cliente de id <cliente_id> (método POST) -> `127.0.0.1:8080/cliente/<cliente_id>/favorites-list/create/`. Formato do json esperato:
    ```
    {
        "id_product": "product_id_from_challeng_api"
    }
    ```
    (O id do produto deve ser condizente com os produtos da api do desafio técnico da Luiza Labs. Para mais informações, consultar https://gist.github.com/Bgouveia/9e043a3eba439489a35e70d1b5ea08ec );
