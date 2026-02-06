# Assur'Aimant 🏦

A modern Django web application for health insurance management with complete authentication system and personalized user profile.

## 📋 Description

Assur'Aimant is an insurance platform developed with Django 5.2.10 that allows users to:
- Create a personal account with secure authentication
- Manage their profile and personal information
- Track their insurance data (BMI, age, smoking status, region, number of children)
- Benefit from a modern and responsive interface with TailwindCSS

## 🚀 Features

### 🔐 Authentication & Security
- **Custom registration** with data validation
- **Secure login** via email
- **Automatic logout**
- **Custom user model** with unique email
- **Password validation** (minimum 8 characters, 1 uppercase, 1 digit)

### 👤 Profile Management
- **User profile visualization**
- **Personal information editing**
- **Insurance information**:
  - BMI (Body Mass Index)
  - Age
  - Smoking status
  - Region
  - Number of children

### 🎨 User Interface
- **Modern design** with TailwindCSS
- **Responsive interface** for all devices
- **Intuitive navigation** with header/footer
- **Professional navy blue theme**

## 🛠️ Tech Stack

- **Backend**: Django 5.2.10
- **Database**: SQLite3
- **Frontend**: HTML5, TailwindCSS
- **Authentication**: Custom Django Auth System
- **Environment variables management**: python-dotenv
- **Python**: 3.11+

## 📁 Project Structure

```
Assurance_Django/
├── AssurAimant/                 # Main project directory
│   ├── AssurAimant/            # Django configuration
│   │   ├── settings.py         # Configuration settings
│   │   ├── urls.py            # Main URLs
│   │   ├── wsgi.py            # WSGI interface
│   │   └── asgi.py            # ASGI interface
│   ├── account/               # Account management app
│   │   ├── models.py          # CustomUser models
│   │   ├── views.py           # Authentication and profile views
│   │   ├── forms.py           # Custom forms
│   │   ├── urls.py            # Account app URLs
│   │   └── templates/         # HTML templates
│   ├── home/                  # Home page app
│   │   ├── views.py           # Home page view
│   │   └── templates/         # Home templates
│   ├── templates/             # Global templates
│   │   └── base.html          # Base template
│   ├── static/                # Static files
│   ├── gunicorn_config.py     # Gunicorn configuration
│   └── manage.py              # Django management script
├── requirements.txt            # Python dependencies
├── .gitignore                 # Files ignored by Git
└── README.md                  # Project documentation
```

## 📦 Dependencies

The `requirements.txt` file contains all necessary dependencies:

### Python Packages
- **Django** 5.2.10 - Web framework
- **python-dotenv** 1.0.1 - Environment variables management
- **whitenoise** 6.8.2 - Static files serving in production
- **gunicorn** 23.0.0 - WSGI server for production

### Frontend
- **TailwindCSS** - CSS framework (via CDN)

## 🚀 Installation

### Prerequisites
- Python 3.11+
- pip (Python package manager)

### Installation Steps

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd Assurance_Django
   ```

2. **Create and activate virtual environment**
   ```bash
   cd AssurAimant
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   cd ..
   pip install -r requirements.txt
   ```

4. **Configure environment variables**
   ```bash
   # Create a .env file in the root of the AssurAimant/ project
   echo "SECRET_KEY=your_secret_key_here" > .env
   echo "DEBUG=True" >> .env
   ```

5. **Apply migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create a superuser (optional)**
   ```bash
   python manage.py createsuperuser
   ```

7. **Start the development server**
   ```bash
   python manage.py runserver
   ```

8. **Access the application**
   - Application: http://127.0.0.1:8000/
   - Administration: http://127.0.0.1:8000/admin/

## 🔧 Configuration

### Environment Variables
- `SECRET_KEY`: Django secret key (automatically generated in production)
- `DEBUG`: Debug mode (True/False)

### Database
The project uses SQLite3 by default. The `db.sqlite3` file is automatically created during migrations.

## 📝 Usage

### Navigation
1. **Home page**: Main application homepage
2. **Account creation**: Registration with data validation
3. **Login**: Authentication via email
4. **Profile**: View and edit information

### Typical User Flow
1. User registers with email, first name, last name, and password
2. After validation, they can log in
3. They access their profile to complete their insurance information
4. They can modify their personal information at any time

## 🧪 Tests

To run tests:
```bash
python manage.py test
```

## 🚀 Deployment

### Collect static files
```bash
python manage.py collectstatic --noinput
```

### Start the project in production
```bash
gunicorn -c gunicorn_config.py AssurAimant.wsgi:application
```

### Stop the server
```bash
pkill gunicorn
```

### Complete production configuration
1. **Disable debug mode**: `DEBUG=False`
2. **Configure `ALLOWED_HOSTS`**
3. **Use a robust database** (PostgreSQL, MySQL)
4. **Configure static files**
5. **Use a WSGI server** (Gunicorn, uWSGI)

### Production configuration example
```python
# settings.py
DEBUG = False
ALLOWED_HOSTS = ['yourdomain.com']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'assuraimant_db',
        'USER': 'db_user',
        'PASSWORD': 'db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

---

**Assur'Aimant** © 2026 - All rights reserved