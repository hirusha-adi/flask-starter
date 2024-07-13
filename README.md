# Flask Starter Application

This is a starter template for a Flask application with SQLAlchemy, Flask-Migrate, Flask-Login, Flask-Sitemap, Docker, and Gunicorn. It includes a sample project structure with a `main` and `admin` blueprint.

## Table of Contents

- [Requirements](#requirements)
- [Initial Setup](#initial-setup)
- [Development Usage](#development-usage)
- [Production Usage](#production-usage)
- [Database Migration](#database-migration)
- [Project Structure](#project-structure)
- [Environment Variables](#environment-variables)

## Requirements

- Python 3.9+
- Docker
- Docker Compose
- PostgreSQL (for production)
- SQLite (for development/testing)

## Initial Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/flask-starter.git
   cd flask-starter
   ```

2. **Create a virtual environment and activate it:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**

   Create a `.env` file in the root directory of the project and add the following:

   ```plaintext
   FLASK_APP=wsgi.py
   FLASK_ENV=development
   DATABASE_URL=sqlite:///app.db
   SECRET_KEY=your_secret_key
   ```

## Development Usage

1. **Initialize the database:**

   ```bash
   flask db init
   flask db migrate -m "Initial migration."
   flask db upgrade
   ```

2. **Run the application:**

   ```bash
   flask run
   ```

   The application will be available at `http://127.0.0.1:5000`.

## Production Usage

1. **Build the Docker image:**

   ```bash
   docker build -t flask-starter .
   ```

2. **Run the Docker container:**

   ```bash
   docker-compose up -d
   ```

   The application will be available at `http://127.0.0.1:5000`.

3. **Run migrations in Docker:**

   ```bash
   docker-compose run web flask db upgrade
   ```

## Database Migration

1. **Initialize the migrations directory:**

   ```bash
   flask db init
   ```

2. **Create a new migration:**

   ```bash
   flask db migrate -m "Description of changes."
   ```

3. **Apply the migration:**

   ```bash
   flask db upgrade
   ```

## Project Structure

```
flask-starter/
├── app/
│   ├── __init__.py
│   ├── extensions.py
│   ├── models.py
│   ├── templates/
│   │   ├── base.html
│   │   └── index.html
│   ├── views/
│   │   ├── __init__.py
│   │   ├── main.py
│   │   └── admin.py
├── migrations/
├── static/
├── .env
├── .gitignore
├── Dockerfile
├── docker-compose.yml
├── manage.py
├── migrate.py
├── requirements.txt
└── wsgi.py
```

## Environment Variables

- `FLASK_APP`: The entry point of the application (default: `wsgi.py`).
- `FLASK_ENV`: The environment in which the application is running (default: `development`).
- `DATABASE_URL`: The database URL for SQLAlchemy.
- `SECRET_KEY`: The secret key for the Flask application.

## Additional Information

- **Admin Blueprint:** The admin blueprint is mounted at the `/admin` URL prefix.
- **Main Blueprint:** The main blueprint is mounted at the root URL (`/`).

For further customization and additional features, please refer to the Flask, SQLAlchemy, and Flask-Login documentation.
