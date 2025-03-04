# Aplicação de Blog em Django

Esta é uma aplicação web baseada em Django para criar e gerenciar um blog. A aplicação permite que os usuários criem, editem e excluam postagens de blog, além de visualizar uma lista de todas as postagens e detalhes de postagens individuais.

## Funcionalidades

- Autenticação de usuário (registro, login, logout)
- Criar, editar e excluir postagens de blog
- Visualizar uma lista de todas as postagens de blog
- Visualizar detalhes de postagens individuais
- Design responsivo para dispositivos móveis e desktop

## Instalação

1. Clone o repositório:
    ```bash
    git clone https://github.com/yourusername/django-blog.git
    cd django-blog
    ```

2. Crie um ambiente virtual e ative-o:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Instale as dependências necessárias:
    ```bash
    pip install -r requirements.txt
    ```

4. Aplique as migrações do banco de dados:
    ```bash
    python manage.py migrate
    ```

5. Crie um superusuário para acessar o admin do Django:
    ```bash
    python manage.py createsuperuser
    ```

6. Execute o servidor de desenvolvimento:
    ```bash
    python manage.py runserver
    ```

7. Abra seu navegador web e vá para `http://127.0.0.1:8000/` para ver a aplicação em ação.

## Uso

- Para criar uma nova postagem de blog, faça login com sua conta de usuário e navegue até a página "Nova Postagem".
- Para editar ou excluir uma postagem de blog, navegue até a página de detalhes da postagem e use as opções fornecidas.
- Para visualizar todas as postagens de blog, vá para a página inicial.

## Contribuindo

Se você gostaria de contribuir para este projeto, por favor siga estes passos:

1. Faça um fork do repositório.
2. Crie um novo branch para sua funcionalidade ou correção de bug.
3. Faça suas alterações e comite-as com mensagens descritivas.
4. Faça push das suas alterações para o seu fork.
5. Crie um pull request para o repositório principal.

## Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo LICENSE para mais detalhes.

## Contato

Se você tiver alguma dúvida ou feedback, por favor sinta-se à vontade para me contatar em [emanuelangelo@outlook.com.br].