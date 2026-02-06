# Core App

Cette application contient les composants réutilisables pour tout le projet AssurAimant.

## Contenu

### Decorators (`core.decorators`)
- `verification_required`: Vérifie si l'utilisateur est authentifié
- `admin_required`: Vérifie si l'utilisateur est authentifié et est administrateur

### Middleware (`core.middleware`)
- `AuthenticationMiddleware`: Protège les routes spécifiées en vérifiant l'authentification
- `AdminRequiredMiddleware`: Protège les routes admin en vérifiant les droits d'administrateur  
- `RequestLoggingMiddleware`: Journalise les requêtes pour le débogage et la surveillance

### Utils (`core.utils`)
- `ApiResponse`: Classe utilitaire pour standardiser les réponses API
- `get_client_ip`: Récupère l'adresse IP du client
- `validate_required_fields`: Valide la présence des champs requis

## Configuration

Les middlewares sont déjà configurés dans `settings.py` :
```python
MIDDLEWARE = [
    ...
    'core.middleware.RequestLoggingMiddleware',
    'core.middleware.AuthenticationMiddleware', 
    'core.middleware.AdminRequiredMiddleware',
]
```

## Utilisation

### Decorators
```python
from core.decorators import verification_required, admin_required

@verification_required
def my_view(request):
    # L'utilisateur est authentifié
    pass

@admin_required  
def admin_view(request):
    # L'utilisateur est authentifié et admin
    pass
```

### Utils
```python
from core.utils import ApiResponse

# Réponse de succès
return ApiResponse.success(data={'key': 'value'}, message='Opération réussie')

# Réponse d'erreur
return ApiResponse.error(message='Erreur lors du traitement', status=400)
```

## Patterns protégés par défaut

### AuthenticationMiddleware
- `/api/`
- `/prediction/`
- `/account/profile/`

### AdminRequiredMiddleware
- `/api/admin/`
- `/admin/api/`

### Patterns exclus
- `/api/auth/`
- `/api/public/`
- `/admin/`
