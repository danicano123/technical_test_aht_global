# technical_test_aht_global v1.0.0

This test assesses a candidate's proficiency in developing a basic web application using Python, Flask, Docker, and SQLAlchemy.

## Installation

To get started with PlateToGrow Backend, follow these steps:

### 1. Install XAMPP (for MySQL Database only if don't want to use Docker container)

If you don't have MySQL installed, you can use XAMPP, a popular package that includes MySQL, Apache, and PHP. Follow these steps to install XAMPP:

- Download XAMPP from [https://www.apachefriends.org/index.html](https://www.apachefriends.org/index.html).
- Install XAMPP by following the installation wizard instructions.
- Start the Apache and MySQL services from the XAMPP Control Panel.

### 2. Clone the repository

```bash
git clone https://github.com/danicano123/technical_test_aht_global.git
cd technical_test_aht_global
```

### 3. Install dependencies

```bash
pip install virtualenv
```

```bash
python -m virtualenv venv
```

```bash
pip install -r requirements.txt
```

### 4. Set up environment variables

- Create a .env file in the root directory of the project.

- Configure the database connection in the .env file according to your MySQL setup or delivered credential by email:

FLASK_APP=
FLASK_ENV=
FLASK_DEBBUG=
MYSQL_USER=
MYSQL_PASSWORD=
MYSQL_HOST=
MYSQL_DATABSE=

### 5. Start the Docker development server

```bash
docker compose up --build
```

The development server will start running at http://localhost:8888. You can access the app from this endpoint.

### 5. Start the local development server

```bash
python index.py   
```

The development server will start running at http://localhost:8888. You can access the app from this endpoint.
