Tecnologias utilizadas: 
  - Python com framework Django
  - HTML e CSS
  - Bootstrap
  - MySQL

Padrão Utilizado:
  - MVC

Modelagem do Banco de dados:
  - O Django cria vários campos necessários para utilizá-lo na tabela, mas as utilizadas no projeto são:
  - Inquilinos, Unidades e Despesas
  - Cada uma, contendo os campos pedidos no desafio e mais alguns que acrescentei ao projeto.

Eu implementei a solução do desafio em um site com os campos no cabeçalho. Acessando cada campo, você terá disponível as tabelas com as informações cadastradas
(se você iniciar o projeto pela primeira vez, não conterá nenhuma informação). E após ir cadastrando as informações, você já consegue vê-las nas tabelas
tendo as opções de edição e remoção em cada uma. Também implementei nas despesas, o campo "id da unidade" em que tem de ser informado para saber
à qual unidade a despesa se refere. Criei mais uma página de erro caso o usuário digite um id de uma unidade que não existe.

Você pode baixar o projeto clicando em CODE e Download ZIP

Lembrando que quando falo para você digitar os códigos no terminal, você tem que digitá-los sem as aspas. 
Botei as aspas para vocês saberem o que tem que digitar no terminal

Como rodar a aplicação:

VSCODE

1 - baixar vscode https://code.visualstudio.com/download

PYTHON

1 - baixar python https://www.python.org/downloads/ (marcar a caixinha add python 3.10 to path na instalação)
2 - após instalar, se tiver uma opção DISABLE PATH LIMIT, clique e termine a instalação

XAMPP

1 - baixar xampp https://www.apachefriends.org/pt_br/download.html

2 - abrir xampp e rodar apache e mysql

3 - abrir no navegador http://localhost/phpmyadmin/

4 - dentro do site acima, clicar em "novo" no canto superior esquerdo

5 - criar a base de dados com o nome "apcoders"

DJANGO

1 - abrir cmd ou terminal do vscode e digitar "pip install django" 

2 - caso não tenha reconhecido o pip e você tenha usado o terminal do vscode, tente no cmd ou vice e versa. Caso ainda não tenha funcionado, 
siga os passos desse site:
https://dicasdepython.com.br/resolvido-pip-nao-e-reconhecido-como-um-comando-interno/

3 - caso o pip peça para atualizar a versão, copie o código que o pip pede e atualize. Rode apenas se o pip não estiver atualizado

4 - dentro do vscode, aperte em "file" no canto superior esquerdo, depois "open folder" e abra a pasta "apcoders" que é o projeto. 
Caso você tenha baixado o arquivo zipado, você precisa tirar o projeto de dentro do arquivo zipado.

5 - com o terminal do vscode aberto ou o cmd, certifique-se que você está dentro da pasta "apcoders" no terminal ou cmd, 
a pasta contém o arquivo manage.py e pastas do projeto

6 - dentro da pasta do projeto no terminal ou cmd, digite os seguintes códigos:

7 - pip install mysqlclient

8 - python manage.py makemigrations

9 - python manage.py migrate

10 - Após o comando anterior, você pode acessar o site do localhost/phpmyadmin, clicar em cima da base de dados "apcoders" (localizada à esquerda do site)
e verificar que a base foi atualizada. Conterá vários campos que o django cria automaticamente para poder utilizá-lo sem problemas, mas principalmente, 
conterá os campos "inquilinos", "unidades" e "despesas"

11 - Volte ao terminal do vscode ou no cmd e digite "python manage.py runserver"

12 - com o server rodando sem erros, clique no link da penúltima linha que é o server com um ctrl + click em cima do link que no meu caso é "http://127.0.0.1:8000/".
Mas clique no seu link que apareceu no seu terminal

13 - se tudo deu certo, o link te levou para a página inicial do meu projeto em que contém um cabeçalho com as opções
Início, Inquilinos, Unidades, Despesas e minhas redes sociais na parte da direita. No corpo tem informações sobre mim e no rodapé tem meu nome
com um link para meu linkedin no nome.

obs: As despesas já estão ordenadas pelo id das unidades

Espero que você tenha conseguido abrir meu projeto na sua máquina com sucesso. Obrigado!

Fotos do projeto:
![Início](https://user-images.githubusercontent.com/79377858/149681404-8c8d5b2c-a9b4-497f-95b5-44a0237ba31d.png)
![Inquilinos](ht![Unidades](https://user-images.githubusercontent.com/79377858/149681408-5174a973-1739-4772-a8d4-d1081daf7ae8.png)
tps://user-images![Despesas](https://user-images.githubusercontent.com/79377858/149681413-2c94f6d0-d3fb-4ed7-b9e7-3cd00fe08bcb.png)
.githubusercontent.com/79377858/149681406-cfb71543-e278-4e1e-9bb0-d0e8564c8294.png)

