# Organiza Casamento 1.0 - Backend

[![Linux](https://svgshare.com/i/Zhy.svg)](https://svgshare.com/i/Zhy.svg)
[![Windows](https://svgshare.com/i/ZhY.svg)](https://svgshare.com/i/ZhY.svg)

App que permitirá organizar casamentos para os noivos.

## 🚀 Sobre o desafio

O problema consiste em criar um sistema que permitirá que os noivos criem uma lista de convidados, com nome e e-mail, e
para cada convidado será possível informar se ele confirmou presença ou não. O sistema irá permitir que os noivos possam enviar RSVP para os convidados por Whatsapp ou Email, podendo também receber notificações das confirmações de presença.
Será possivel exportar a lista de convidados em PDF e uma planilha com dados do Evento cadastrado. O sistema tem como objetivo facilitar a organização de casamentos, permitindo que os noivos possam ter um controle de quantos convidados confirmaram presença, quantos não confirmaram, e quantos ainda não responderam.
Será possivel também adicionar artefatos do casamento, como fotos, vídeos, e músicas, que farão parte do casamento e podem ajudar a definir as preferências dos noivos.
No sistema existe um Checklist de atividades para os noivos com deadline e dicas.

## 📝 Descrição do projeto

Para entender melhor o funcionamento do projeto, segue abaixo uma imagem que representa o fluxo de comunicação entre os
dois projetos.

![Fluxo de comunicação entre os projetos](https://i.imgur.com/XUIyi9P.png)

## 🛠 Tecnologias utilizadas

As seguintes ferramentas foram usadas na construção do projeto:

### Backend

- [Django](https://www.djangoproject.com/)
- [Django Rest Framework](https://www.django-rest-framework.org/)
- [Django Knox](https://james1345.github.io/django-rest-knox/)
- [PyTest](https://docs.pytest.org/en/stable/)
- [Postman](https://www.postman.com/)
- [PostgreSQL](https://www.postgresql.org/)
- [Pep8](https://pypi.org/project/pep8/)
- [Flake8](https://flake8.pycqa.org/en/latest/)
- [PyLint](https://www.pylint.org/)
- [NGINX](https://www.nginx.com/)
- [Gunicorn](https://gunicorn.org/)
- [Certbot](https://certbot.eff.org/)

## 📦 Instalação

### Pré-requisitos

Antes de começar, você vai precisar ter instalado em sua máquina as seguintes ferramentas:

- [Git](https://git-scm.com/)
- [Python](https://www.python.org/)
- [Pip](https://pypi.org/project/pip/)
- [Virtualenv](https://pypi.org/project/virtualenv/)

Crie um ambiente virtual para instalar as dependências do projeto.

```bash
virtualenv venv
```

Ative o ambiente virtual.

```bash
source venv/bin/activate
```

### Instalação do projeto

Agora instale as dependências do projeto.

```bash
pip install -r requirements.txt
```

### Configuração do projeto

Rode as migrações

```bash
python manage.py migrate
```

Crie um super usuário

```bash
python manage.py createsuperuser
```

### Execução do projeto

Para executar o projeto, execute o comando abaixo.

```bash
python manage.py runserver
```

A aplicação estará rodando na porta 8000. Para acessar o painel administrativo, acesse a url abaixo:

```bash 
http://localhost:8000/admin
```

## 📝 Licença

Este projeto está sob a licença [MIT](https://opensource.org/licenses/MIT).

## 📝 Autor

<a href="#">
 <img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/7137962?v=4" width="100px;" alt=""/>
</a>
 <br />
 <sub><b>Caio Marinho</b></sub>
 <a href="#" title="Caio Marinho">🚀</a>

[![Linkedin Badge](https://img.shields.io/badge/-Caio%20Marinho-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/caiomarinho/)](https://www.linkedin.com/in/caiomarinho/)
[![Gmail Badge](https://img.shields.io/badge/-caiomarinho8@gmail.com-c14438?style=flat-square&logo=Gmail&logoColor=white&link=mailto:caiomarinho8@gmail.com)](mailto:caiomarinho8@gmail.com)

Made with ❤️ by [Caio Marinho!](https://caiomarinho.tech/) 👋🏽 [Get in Touch!](https://www.linkedin.com/in/caiomarinho/)
