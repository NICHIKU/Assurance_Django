# Assur'Aimant 🏦

Une application web Django moderne pour la gestion d'assurance santé avec système d'authentification complet et profil utilisateur personnalisé.

## 📋 Description

Assur'Aimant est une plateforme d'assurance développée avec Django 5.2.10 qui permet aux utilisateurs de :
- Créer un compte personnel avec authentification sécurisée
- Gérer leur profil et informations personnelles
- Suivre leurs données d'assurance (IMC, âge, statut fumeur, région, nombre d'enfants)
- Bénéficier d'une interface moderne et responsive avec TailwindCSS

## 🚀 Fonctionnalités

### 🔐 Authentification & Sécurité
- **Inscription personnalisée** avec validation des données
- **Connexion sécurisée** via email
- **Déconnexion automatique**
- **Modèle utilisateur personnalisé** avec email unique
- **Validation des mots de passe** (8 caractères minimum, 1 majuscule, 1 chiffre)

### 👤 Gestion du Profil
- **Visualisation du profil utilisateur**
- **Modification des informations personnelles**
- **Informations d'assurance** :
  - IMC (Indice de Masse Corporelle)
  - Âge
  - Statut fumeur
  - Région
  - Nombre d'enfants

### 🎨 Interface Utilisateur
- **Design moderne** avec TailwindCSS
- **Interface responsive** pour tous les appareils
- **Navigation intuitive** avec header/footer
- **Thème professionnel** bleu marine

## 🛠️ Stack Technique

- **Backend** : Django 5.2.10
- **Base de données** : SQLite3
- **Frontend** : HTML5, TailwindCSS
- **Authentification** : Django Auth System personnalisé
- **Gestion des variables d'environnement** : python-dotenv
- **Python** : 3.11+

## 📁 Structure du Projet

```
Assurance_Django/
├── AssurAimant/                 # Répertoire principal du projet
│   ├── AssurAimant/            # Configuration Django
│   │   ├── settings.py         # Paramètres de configuration
│   │   ├── urls.py            # URLs principales
│   │   ├── wsgi.py            # Interface WSGI
│   │   └── asgi.py            # Interface ASGI
│   ├── account/               # App de gestion des comptes
│   │   ├── models.py          # Modèles CustomUser
│   │   ├── views.py           # Vues d'authentification et profil
│   │   ├── forms.py           # Formulaires personnalisés
│   │   ├── urls.py            # URLs de l'app account
│   │   └── templates/         # Templates HTML
│   ├── home/                  # App page d'accueil
│   │   ├── views.py           # Vue de la page d'accueil
│   │   └── templates/         # Templates home
│   ├── templates/             # Templates globaux
│   │   └── base.html          # Template de base
│   ├── static/                # Fichiers statiques
│   └── manage.py              # Script de gestion Django
├── .gitignore                 # Fichiers ignorés par Git
└── README.md                  # Documentation du projet
```

## 📦 Dépendances

### Python Packages
- **Django** 5.2.10 - Framework web
- **python-dotenv** - Gestion des variables d'environnement

### Frontend
- **TailwindCSS** - Framework CSS (via CDN)

## 🚀 Installation

### Prérequis
- Python 3.11+
- pip (gestionnaire de paquets Python)

### Étapes d'installation

1. **Cloner le repository**
   ```bash
   git clone <repository-url>
   cd Assurance_Django
   ```

2. **Créer et activer l'environnement virtuel**
   ```bash
   cd AssurAimant
   python -m venv venv
   source venv/bin/activate  # Sur Windows: venv\Scripts\activate
   ```

3. **Installer les dépendances**
   ```bash
   pip install django==5.2.10 python-dotenv
   ```

4. **Configurer les variables d'environnement**
   ```bash
   # Créer un fichier .env à la racine du projet AssurAimant/
   echo "SECRET_KEY=votre_cle_secrete_ici" > .env
   echo "DEBUG=True" >> .env
   ```

5. **Appliquer les migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Créer un superutilisateur (optionnel)**
   ```bash
   python manage.py createsuperuser
   ```

7. **Lancer le serveur de développement**
   ```bash
   python manage.py runserver
   ```

8. **Accéder à l'application**
   - Application : http://127.0.0.1:8000/
   - Administration : http://127.0.0.1:8000/admin/

## 🔧 Configuration

### Variables d'environnement
- `SECRET_KEY` : Clé secrète Django (générée automatiquement en production)
- `DEBUG` : Mode debug (True/False)

### Base de données
Le projet utilise SQLite3 par défaut. Le fichier `db.sqlite3` est créé automatiquement lors des migrations.

## 📝 Utilisation

### Navigation
1. **Page d'accueil** : Accueil principal de l'application
2. **Création de compte** : Inscription avec validation des données
3. **Connexion** : Authentification via email
4. **Profil** : Visualisation et modification des informations

### Flux utilisateur typique
1. L'utilisateur s'inscrit avec email, nom, prénom et mot de passe
2. Après validation, il peut se connecter
3. Il accède à son profil pour compléter ses informations d'assurance
4. Il peut modifier ses informations personnelles à tout moment

## 🧪 Tests

Pour exécuter les tests :
```bash
python manage.py test
```

## 🚀 Déploiement

### En production
1. **Désactiver le mode debug** : `DEBUG=False`
2. **Configurer les `ALLOWED_HOSTS`**
3. **Utiliser une base de données robuste** (PostgreSQL, MySQL)
4. **Configurer les fichiers statiques**
5. **Utiliser un serveur WSGI** (Gunicorn, uWSGI)

### Exemple de configuration production
```python
# settings.py
DEBUG = False
ALLOWED_HOSTS = ['votredomaine.com']
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

**Assur'Aimant** © 2026 - Tous droits réservés