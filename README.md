# Projeto_Integrador

- Sistema: Observatório da Juventude (OJ)

- Projeto desenvolvido por Ana Caroline, Emerson Bottega, Nicole Inaê de Oliveira na máteria de Projeto Integrador no curso de Tecnologia em Análise e Desenvolvimento de Sistemas (TADS), do Instituto Federal do Paraná - Campus Cascavel.

## Tecnologias Utilizadas:
-  Visual Studio Code
-  GitHub
-  Python
-  Django, Django restframework
-  HTML5 & CSS
-  JavaScript
-  Venv (Ambiente virtual python)

# Como executar a aplicação:
## 1. Clone o repositório
Execute o comando abaixo para clonar o repositório em sua máquina local:

```bash
git clone https://github.com/EmersonBottega/Projeto_Integrador.git
```

Substitua usuario e repo pelos valores reais.

## 2. Crie e ative o ambiente virtual
Navegue até o diretório do projeto clonado:

```bash
cd nome_do_diretorio
```

Crie um ambiente virtual utilizando venv:

```bash
python -m venv venv
```
Ative o ambiente virtual:

No Windows:
```bash
venv\Scripts\activate
```

No Linux ou macOS:
```bash
source venv/bin/activate
```

## 3. Instale as dependências
Com o ambiente virtual ativado, instale todas as dependências do projeto:

```bash
pip install django, djangorestframework, django-cors-headers
```

## 4. Realize as migrações do banco de dados
Execute os seguintes comandos para aplicar as migrações do banco de dados:

```bash
python manage.py migrate
```

## 5. Execute o servidor de desenvolvimento
Agora você pode rodar o servidor de desenvolvimento:

```bash
python manage.py runserver
```

## 6. Acesse a aplicação
Abra o navegador e acesse:
- http://127.0.0.1:8000/
  
## 7. (Opcional) Crie um superusuário
Se precisar acessar a área administrativa do Django, crie um superusuário:

```bash
python manage.py createsuperuser
```

## Parabéns! :tada:

Você Conseguiu. :partying_face:
