README - Sistema de Times de Futebol
Sobre
Sistema Django para gerenciar e exibir times de futebol.

Instalação Rápida
bash
 Ambiente
 
python -m venv venv
venv\Scripts\activate
pip install django

 Projeto
 
django-admin startproject meuprojeto .
python manage.py migrate
python manage.py createsuperuser
python manage.py startapp times
Configuração
settings.py - Adicionar 'times' no INSTALLED_APPS

models.py

python
class Time(models.Model):
    nome = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    fundacao = models.DateField()
admin.py - admin.site.register(Time)

views.py - Função lista_times que busca e renderiza os dados

urls.py (app) - Rota para a view

urls.py (projeto) - Incluir as URLs do app

Executar
bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
Acessar
Sistema: http://127.0.0.1:8000/

Admin: http://127.0.0.1:8000/admin/

Funcionalidades

Lista todos os times

Mostra total de times

Exibe time mais antigo

Data formatada e tempo de fundação

Interface estilizada

coloque em formato de texto
README - Sistema de Times de Futebol
Sobre: Sistema Django para gerenciar e exibir times de futebol.

Instalação Rápida:

Ambiente

python -m venv venv
venv\Scripts\activate
pip install django

Projeto
django-admin startproject meuprojeto .
python manage.py migrate
python manage.py createsuperuser
python manage.py startapp times

Configuração:

settings.py - Adicionar 'times' no INSTALLED_APPS

models.py:
class Time(models.Model):
nome = models.CharField(max_length=100)
cidade = models.CharField(max_length=100)
fundacao = models.DateField()


admin.py - admin.site.register(Time)

views.py - Função lista_times que busca e renderiza os dados

urls.py (app) - Rota para a view

urls.py (projeto) - Incluir as URLs do app

Executar:

python manage.py makemigrations
python manage.py migrate
python manage.py runserver


Acessar:
Sistema: http://127.0.0.1:8000/
Admin: http://127.0.0.1:8000/admin/

Funcionalidades:

Lista todos os times

Mostra total de times

Exibe time mais antigo

Data formatada e tempo de fundação

Interface estilizada

