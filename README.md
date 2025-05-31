Este é projeto é um sistema web desenvolvido com django que gerencia alunos de uma academia e prevê a chance de desistência com base em dados comportamentais, utilizando o modelo de IA ML (Random Forest) 
--
# Funcionalidades
 - Cadastro de Alunos.
 - Registro de relatórios de desempenho.
 - IA que estima a probabilidade de desistência dos alunos.
 - Interface amigável com Bootstrap 5.

# Tecnologias Utilizadas
 - Python 3.13.
 - Django.
 - Pandas.
 - Scikit-Learn..
 - Bootstrap 5.3.
 - SQlite (Padrão Django).

--

/Academia

 clientes/ # App Principal com os modelos e views

 ml/ # Pasta onde está o modelo IA ( Pkl ) 
 
 templates/ # HTML
 
 manage.py # Arquivo principal do Django
 
 modelo_desistencia.pkl # modelo treinado ( pode ser recriado ) 

--

# Como rodar o projeto Localmente.

-- 1. Clone o Repositório 
```bash
git clone https://github.com/IsAparecida01/Django-Ia-Academia.git
cd Django-Ia-Academia

-- 2. Crie um ambiente virtual
python -m venv venv
venv/Scripts/activate # Windows
source venv/bin/activate # Linux/Mac

-- 3. Instale as dependências
pip install -r requirements.txt

-- 4. Rode as migrações do banco de dados.

python manage.py makemigrations
python manage.py migrate

-- 5. Treine o modelo de IA ( opcional, já existe o PKL treinado )

cd ml ( deve retornar para cd Academia após ) 
python treinar_modelo.py
cd Academia

-- 6. Crie um Admin

python manage.py createsuperuser

-- 7. Rode o Servidor local. 

python manage.py runserver

Por fim, acesse no navegador http://127.0.0.1:8000/

Neste App é possível adicionar alunos e registrar relatórios via interface ou admin
Foi utilizado o algoritmo Random Forest Classifier para prever a chance de desistência com base nos seguintes dados: 
Gênero
Idade
Frequência Semanal
Estação 
Objetivo Alcançado
Satisfação
Lesões
