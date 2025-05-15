# Bitcoin Relatory API

Api criada seguindo a aula do Di Dev ![Link do vídeo](https://www.youtube.com/watch?v=1CZZAhwqyco&t=6570s), a API utiliza PostgreSQL, SQLAlquemy e FastAPI.

Para testar o aplicativo, apenas clone o repositório, altere a .env para as credênciais do seu banco de dados e execute o main.py, acessando a URL mostrada podemos ir em localhost:8000/docs, para verificar todos os endpoints do projeto, sendo eles:

* **/users/create**: Utilizado para criar um usuário no módelo:
  `````
  "name": "string"

* **/users/delete/{user_id}**: Deletar o usuário a partir do ID.

* **/users/list**: Listar usuários e criptos.

* **/users/favorite/add**: Cria uma cripto favorita para um usuário no módelo:
  `````
  "user_id": 0,
  "symbol": "string"

* **/users/favorite/remove/{user_id}?symbol={nomeDaMoeda}**: Remove uma cripto favorita utilizando o id de usuário e nome da moeda.

* **/assets/day_summary/{user_id}**: Mostra um relátorio do maior e menos preço das cripto do usuario selecionado {user_id}.

