# MyBookList

Aplicação de gerenciamento de acervo pessoal de livros. Teste para seleção de Dev Django na [Conceptu](https://www.conceptu.ind.br/).

![image](https://user-images.githubusercontent.com/52494917/124398823-2968e700-dcee-11eb-964c-d9f928b1fd16.png)

Demo da aplicação rodando no [Heroku](https://www.heroku.com/):

https://mybooklist-django.herokuapp.com/

## Tecnologias utilizadas:

* Python
* [Django](https://www.djangoproject.com/)
* [Django Rest Framework](https://www.django-rest-framework.org/)
* [PostgreSQL](https://www.postgresql.org/)
* Testes automatizados para as API's
* [Docker](https://www.docker.com/) (ambiente de desenvolvimento)
* [Bootstrap](https://getbootstrap.com/)
* Javascript

## Execução da aplicação
### Iniciar aplicação usando [Docker](https://www.docker.com/) (recomendado):
```bash
 docker-compose up --build
```
O docker fará o build de uma imagem personalizada, já instalando as dependências necessárias (requirements.txt), em seguida, o servidor de desenvolvimento estará acessível em: [http://localhost:8000](http://localhost:8000). Além do container rodando o servidor Django, o docker-compose também cria um container para o PostgreSQL (banco de dados usado pela aplicação).

### Iniciar a aplicação sem usar Docker:

- Instalação das dependências (é recomendado usar um virtual env):
```bash
 pip install -r requirements.txt
```
Em seguida, é preciso [baixar e instalar o PostgreSQL](https://www.postgresql.org/download/), criar uma base de dados para a aplicação e configurar as credenciais do banco como variáveis de ambiente no arquivo .env.

- Rodar migrations e iniciar servidor de desenvolvimento:
```bash
 python manage.py migrate 
 python manage.py runserver 0.0.0.0:8000
```
O servidor de desenvolvimento estará acessível em: [http://localhost:8000](http://localhost:8000).

## Documentação das API's (swagger)

Uma documentação básica das rotas gerada usando o swagger está disponível em:

https://mybooklist-django.herokuapp.com/swagger

## Detalhes da solução proposta

### Descrição geral
O projeto Django criado possui 3 apps, eles são:

* User: Responsável pela criação e autenticação de usuários (SessionAuthentication) 
   * Rota de login: ```/api/user/login```
   * Rota de registro de um novo usuário: ```/api/user/register```
   * Rota de logout: ```/api/user/logout```
   * Rota pro usuário visualizar e editar o próprio perfil: ```/api/user/me``` (não foi criada tela de perfil, apenas a rota)
* Books: Responsável pelo CRUD de livros e de categorias (book-gender)
   * CRUD livros ```/api/books```
   * CRUD categorias (book-gender) ```/api/book-gender```
* Core: Responsável por cuidar das requisições das páginas (Login, registro, landing page e home page), nesse app estão os templates, migrations e models da aplicação.


### Features:
* Login e registro de usuários
* Autenticação para acessar as API's - Autenticação por sessão do próprio Django (SessionAuthentication)
* CRUD de livros e categorias (book-gender) 
* Filtragem de livros por status (completados, lendo, planeja ler e desistiu de ler) e por categoria (gêneros de livros adicionados pelo usuário)
* Testes automatizados para todas as API's
* Estatísticas de leitura do usuário
* Usuário pode dar uma nota para os livros que terminou de ler 

## Deploy
O deploy da aplicação foi feito usando o Heroku. Para tal, o pacote para python django-heroku foi usado, esse pacote facilita o processo de deploy de uma aplicação Django para o heroku, com poucas modificações no código e adição de dois arquivos (Procfile e runtime.txt) o deploy da aplicação pode ser feito.  
Demo da aplicação rodando no [Heroku](https://www.heroku.com/):

https://mybooklist-django.herokuapp.com/




