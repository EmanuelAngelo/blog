# Django Blog Application

This is a Django-based web application for creating and managing a blog. The application allows users to create, edit, and delete blog posts, as well as view a list of all posts and individual post details.

## Features

- User authentication (registration, login, logout)
- Create, edit, and delete blog posts
- View a list of all blog posts
- View individual blog post details
- Responsive design for mobile and desktop

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/django-blog.git
    cd django-blog
    ```

2. Create a virtual environment and activate it:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Apply the database migrations:
    ```bash
    python manage.py migrate
    ```

5. Create a superuser to access the Django admin:
    ```bash
    python manage.py createsuperuser
    ```

6. Run the development server:
    ```bash
    python manage.py runserver
    ```

7. Open your web browser and go to `http://127.0.0.1:8000/` to see the application in action.

## Usage

- To create a new blog post, log in with your user account and navigate to the "New Post" page.
- To edit or delete a blog post, navigate to the post's detail page and use the provided options.
- To view all blog posts, go to the home page.

## Contributing

If you would like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Make your changes and commit them with descriptive messages.
4. Push your changes to your fork.
5. Create a pull request to the main repository.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contact

If you have any questions or feedback, please feel free to contact me at [your-email@example.com].