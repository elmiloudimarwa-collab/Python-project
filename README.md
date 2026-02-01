# E-Shop Project
A Django-based E-commerce platform with a modern glassmorphism design.
## Team
- **Ilyass Sif**
- **Yassmine El Harrab**
- **Marwa El Miloudi**
- **Mohamed Faddad**
## Prerequisites
- Python 3.8+
- SQLite (included)
## Installation
1.  **Clone the repository** (if not already done).
2.  **Activate the virtual environment**:
    ```bash
    source .venv/bin/activate
    # On Windows: .venv\Scripts\activate
    ```
3.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
4.  **Apply database migrations**:
    ```bash
    python manage.py migrate
    ```
5.  **Create a superuser** (optional, for admin access):
    ```bash
    python manage.py createsuperuser
    ```
## Running the Server
To start the development server:
```bash
python manage.py runserver
```
Access the site at: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
## Features
- **Products**: Browse catalog with categories and search.
- **Cart**: Session-based shopping cart with toast notifications.
- **Orders**: complete checkout flow and order history.
- **Accounts**: User registration and authentication.
## Project Structure
- `products/`: Catalogue management.
- `cart/`: Shopping cart logic.
- `orders/`: Order processing.
- `accounts/`: User authentication.
- `static/`: CSS, JS, and images (reorganized by app).
