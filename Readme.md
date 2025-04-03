# Django Project Installation Guide

## Prerequisites
Ensure you have the following installed on your system:
- Python (>=3.x)
- Git
- pip (comes with Python)
- Virtual environment (`venv`)

## Installation Steps

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo
```

### 2. Create and Activate Virtual Environment
#### On macOS/Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
```
#### On Windows (CMD):
```bash
python -m venv .venv
.venv\Scripts\activate
```
#### On Windows (PowerShell):
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Apply Migrations
```bash
python manage.py migrate
```

### 5. Run the Development Server
```bash
python manage.py runserver
```

Your Django project will now be running at:
```
http://127.0.0.1:8000/
```

### 6. (Optional) Create a Superuser
If your project has Django Admin, create a superuser:
```bash
python manage.py createsuperuser
```
Follow the prompts to set up login credentials.

## Additional Commands
- **Deactivate Virtual Environment**:
  ```bash
  deactivate
  ```
- **Install Additional Packages**:
  ```bash
  pip install package-name
  pip freeze > requirements.txt
  ```

## Troubleshooting
- If you get a `ModuleNotFoundError`, ensure the virtual environment is activated.
- If the database is not working, run:
  ```bash
  python manage.py makemigrations
  python manage.py migrate
  ```

---

You're all set! 🎉 Happy coding!

