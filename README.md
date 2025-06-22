# Projeto To-Do List em Django

Este é um simples projeto de uma aplicação de lista de tarefas (To-Do List) desenvolvido com o framework Django.

## Funcionalidades

- Adicionar novas tarefas.
- Listar todas as tarefas.
- Marcar tarefas como concluídas.
- Remover tarefas.

## Tecnologias Utilizadas

- Python
- Django
- HTML
- CSS (pode ser integrado com frameworks como Bootstrap)
- SQLite (banco de dados padrão do Django)

## Como Executar o Projeto

Siga as instruções abaixo para configurar e executar o projeto em seu ambiente local.

### Pré-requisitos

- Python 3.8 ou superior
- `pip` (gerenciador de pacotes do Python)

### Passos para Instalação

1.  **Clone o repositório ou baixe o projeto**

    Se o projeto estiver em um repositório Git, clone-o. Caso contrário, apenas navegue até o diretório raiz do projeto (`Projeto-NovasTecnologias-AT1`).

2.  **Crie e ative um ambiente virtual**

    É uma boa prática usar um ambiente virtual para isolar as dependências do projeto.

    ```bash
    # Navegue até a pasta do projeto (ex: Projeto_AT1)
    cd .\Projeto-NovasTecnologias-AT1\

    # Crie o ambiente virtual
    python -m venv venv

    # Ative o ambiente virtual
    # No Windows:
    .\venv\Scripts\activate
    # No macOS/Linux:
    # source venv/bin/activate
    ```

3.  **Instale as dependências**

    Este projeto requer o Django. Instale-o usando o pip.

    ```bash
    pip install Django
    ```

4.  **Aplique as migrações do banco de dados**

    As migrações criam as tabelas necessárias no banco de dados. Execute o comando a partir do diretório que contém o `manage.py` (`todoApp`).

    ```bash
    cd todoApp
    python manage.py migrate
    ```

5.  **Crie um superusuário (Opcional)**

    Isso permite que você acesse a área administrativa do Django.

    ```bash
    python manage.py createsuperuser
    ```
    Você precisará fornecer um nome de usuário, e-mail e senha.

6.  **Inicie o servidor de desenvolvimento**

    Agora você pode iniciar o servidor local.

    ```bash
    python manage.py runserver
    ```

7.  **Acesse a aplicação**

    Abra seu navegador e acesse a seguinte URL:
    [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

    Você deverá ver a página inicial da sua aplicação de lista de tarefas. Para acessar a área de administração, vá para `http://127.0.0.1:8000/admin`.

