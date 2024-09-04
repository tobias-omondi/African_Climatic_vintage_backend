# African_Climatic_vintage


# African Climatic Vintage Backend

## Overview

The African Climatic Vintage Backend is a RESTful API built using Flask and SQLAlchemy. This application serves as the backend for managing various resources related to climate issues in Africa. It includes user authentication, news articles, podcasts, panel discussions, multimedia content, interviews, and documentation. The application is designed to provide a robust and scalable solution for handling climate-related data and resources.

## Features

- **User Management**: Create and manage user accounts with authentication.
- **News Management**: Create, update, delete, and retrieve news articles related to climate issues.
- **Podcast Management**: Manage podcast episodes discussing various climate topics.
- **Panel Discussions**: Organize and manage panel discussions featuring experts in the field.
- **Multimedia Content**: Upload and manage multimedia resources such as images and videos.
- **Interviews**: Store and manage interviews with climate experts.
- **Documentation**: Provide access to important documents and reports.
- **Admin Panel**: An administrative interface for managing users and content.

## Technologies Used

- **Flask**: A lightweight WSGI web application framework.
- **SQLAlchemy**: An ORM (Object Relational Mapper) for database interactions.
- **Flask-Migrate**: For handling database migrations.
- **Flask-RESTful**: For building REST APIs.
- **Flask-Bcrypt**: For password hashing.
- **Flask-Login**: For user session management.
- **Flask-Admin**: for admin pannel

## Installation

### Prerequisites

Make sure you have Python 3.6+ and pip installed on your machine.

### Clone the Repository

```bash
git clone git@github.com:tobias-omondi/African_Climatic_vintage_backend.git
cd African_Climatic_vintage_backend/

python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

pip install -r requirements.txt

~### Initalizing Database
-**flask db init**:
migratin creating
-**flask db migrate -m "Initial migration."**:
applying migration
-##flask db upgrade

Running the Application
To run the application, use the following command:
bash
flask run