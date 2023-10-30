# Projeto de Estágio na Bioma

Este é um projeto desenvolvido como parte do meu estágio na Bioma, uma empresa focada em [
    desenvolvimento em python
]

## Tecnologias Utilizadas

- [FastAPI](https://fastapi.tiangolo.com/): Um moderno framework web em Python para construção de APIs rápidas e escaláveis.
- [Uvicorn](https://www.uvicorn.org/): Um servidor ASGI de alta performance, que é compatível com o FastAPI.
- [Python-Jose](https://github.com/mpdavis/python-jose): Uma biblioteca para trabalhar com JSON Web Tokens (JWT) em Python.
- [Pydantic](https://pydantic-docs.helpmanual.io/): Uma biblioteca para validação de dados em Python.
- [SQLAlchemy](https://www.sqlalchemy.org/): Uma poderosa biblioteca de SQL para Python, que facilita a interação com bancos de dados relacionais.
- [Docker](https://www.docker.com/): Plataforma que permite criar, implantar e executar aplicativos em contêineres.
- [PostgreSQL](https://www.postgresql.org/): Um sistema de gerenciamento de banco de dados relacional de código aberto e poderoso.

## Configuração do Ambiente

1. Clone este repositório: `git clone https://github.com/joaoBatistaDesenvolvedor/fastApiBioma.git.
2. Crie e ative um ambiente virtual: `python -m venv venv` e `source venv/bin/activate` (Linux/macOS) ou `venv\Scripts\activate` (Windows).
3. Instale as dependências: `pip install -r requirements.txt`.

## Executando o Projeto

- Certifique-se de ter o Docker e o Docker Compose instalados.
- Execute o projeto com o comando: `docker-compose up --build`, mais precisa definir o caminho do volume 

uvicorn main:app --reload

## Requisições HTTP

### Adicionar Empresa

- Método: POST
- URL: http://127.0.0.1:8000/company
- Body (JSON):
  ```json
  {
    "nome": "microsoft",
    "cnpj": "20320059000174",
    "descricao": "Descrição da Empresa"
  }

  ### Adicionar colaborador

- Método: POST
- URL: http://127.0.0.1:8000//colaborate
- Body (JSON):
  ```json
  {
  "nome": "paula",
  "sobrenome": "ferreira",
  "cargo": "telemarkiting",
  "password": "123",
  "idEmpresa": 3,
  "cpf": "1111111111111"
}

# Listar Todas as Empresas
Método: GET
URL: http://127.0.0.1:8000/company
Listar Todos os Colaboradores
Método: GET
URL: http://127.0.0.1:8000/colaborate
Obter Informações de uma Empresa Específica
Método: GET
URL: http://127.0.0.1:8000/company/20320059000174
# Obter Informações de Funcionários de uma Empresa
Método: GET
URL: http://127.0.0.1:8000/colaborate/12345678000190
Deletar Empresa
Método: DELETE
URL: http://127.0.0.1:8000/company/20320059000177
Deletar Colaborador
Método: DELETE
URL: http://127.0.0.1:8000/colaborate/1111111111111





## Licença

Este projeto é licenciado sob [descrever a licença, por exemplo: MIT License](LICENSE).
