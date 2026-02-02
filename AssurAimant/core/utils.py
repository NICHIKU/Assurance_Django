import json
from django.http import JsonResponse
from django.core.serializers.json import DjangoJSONEncoder

class ApiResponse:
    """
    Classe utilitaire pour standardiser les réponses API.
    """
    
    @staticmethod
    def success(data=None, message="Success", status=200):
        """Retourne une réponse de succès."""
        response_data = {
            'success': True,
            'message': message,
        }
        if data is not None:
            response_data['data'] = data
        return JsonResponse(response_data, status=status, encoder=DjangoJSONEncoder)
    
    @staticmethod
    def error(message="Error", status=400, errors=None):
        """Retourne une réponse d'erreur."""
        response_data = {
            'success': False,
            'message': message,
        }
        if errors:
            response_data['errors'] = errors
        return JsonResponse(response_data, status=status)
    
    @staticmethod
    def created(data=None, message="Resource created successfully"):
        """Retourne une réponse de création (201)."""
        return ApiResponse.success(data=data, message=message, status=201)
    
    @staticmethod
    def not_found(message="Resource not found"):
        """Retourne une réponse 404."""
        return ApiResponse.error(message=message, status=404)
    
    @staticmethod
    def unauthorized(message="Authentication required"):
        """Retourne une réponse 401."""
        return ApiResponse.error(message=message, status=401)
    
    @staticmethod
    def forbidden(message="Access denied"):
        """Retourne une réponse 403."""
        return ApiResponse.error(message=message, status=403)

def get_client_ip(request):
    """
    Récupère l'adresse IP du client.
    """
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def validate_required_fields(data, required_fields):
    """
    Valide la présence des champs requis dans les données.
    """
    missing_fields = [field for field in required_fields if field not in data]
    if missing_fields:
        return False, f"Missing required fields: {', '.join(missing_fields)}"
    return True, None
