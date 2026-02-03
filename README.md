# Assur'Aimant 🏦

A modern Django web application for health insurance management with complete authentication system and personalized user profile.

## 📋 Description

Assur'Aimant is an insurance platform developed with Django 5.2.10 that allows users to:
- Create a personal account with secure authentication
- Manage their profile and personal information
- Track their insurance data (BMI, age, smoking status, region, number of children)
- **Predict insurance costs** using machine learning models
- **Schedule appointments** with insurance advisors
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

### 🤖 Insurance Prediction
- **AI-powered cost prediction** using scikit-learn
- **Linear regression model** trained on insurance data
- **Real-time calculation** based on user parameters
- **Interactive form** with data validation

### 📅 Appointment System
- **Schedule appointments** with insurance advisors
- **Advisor management** with specialities
- **Time slot management** (9AM-6PM)
- **Appointment status tracking** (pending, confirmed, cancelled, completed)
- **Calendar view** for easy scheduling

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
- **Machine Learning**: scikit-learn 1.7.2, pandas 2.3.3, joblib 1.5.3
- **Environment variables management**: python-dotenv
- **Static files**: whitenoise 6.8.2
- **WSGI server**: gunicorn 23.0.0
- **Form enhancements**: django-widget-tweaks
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
│   ├── prediction/            # Insurance prediction app
│   │   ├── models.py          # Prediction models
│   │   ├── views.py           # Prediction views
│   │   ├── forms.py           # Prediction forms
│   │   ├── service.py         # ML model service
│   │   ├── resources/         # ML model files
│   │   │   └── linear_model.joblib  # Trained model
│   │   └── urls.py            # Prediction app URLs
│   ├── appointment/           # Appointment management app
│   │   ├── models.py          # Advisor and Appointment models
│   │   ├── views.py           # Appointment views
│   │   ├── forms.py           # Appointment forms
│   │   └── urls.py            # Appointment app URLs
│   ├── core/                  # Core utilities app
│   │   ├── models.py          # Core models
│   │   └── decorators.py      # Custom decorators
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
- **scikit-learn** 1.7.2 - Machine learning library
- **pandas** 2.3.3 - Data manipulation library
- **joblib** 1.5.3 - Model serialization

### Django Extensions
- **django-widget-tweaks** - Form field customization

### Frontend
- **TailwindCSS** - CSS framework (via CDN)

### Machine Learning Model
- **Pre-trained linear regression model** for insurance cost prediction
- Located at `prediction/resources/linear_model.joblib`

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

7. **Create insurance advisors (optional)**
   ```bash
   python create_advisors.py
   ```
   This will create 3 test advisors with different specialities:
   - Martin Durand (Assurance Vie)
   - Sophie Bernard (Assurance Auto) 
   - Pierre Martin (Assurance Habitation)

8. **Start the development server**
   ```bash
   python manage.py runserver
   ```

9. **Access the application**
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
5. **Insurance Prediction**: Calculate estimated insurance costs
6. **Appointments**: Schedule and manage advisor meetings

### Typical User Flow
1. User registers with email, first name, last name, and password
2. After validation, they can log in
3. They access their profile to complete their insurance information
4. They can use the prediction tool to estimate insurance costs
5. They can schedule appointments with insurance advisors
6. They can modify their personal information at any time

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