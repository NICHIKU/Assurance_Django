from django.http import JsonResponse
from django.core.exceptions import PermissionDenied

class VerificationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Logique de vérification avant la vue
        response = self.process_request(request)
        
        if response:
            return response
            
        # Continue vers la vue
        response = self.get_response(request)
        
        # Logique après la vue (optionnel)
        response = self.process_response(request, response)
        
        return response
    
    def process_request(self, request):
        # Vérifier seulement si l'utilisateur est authentifié
        if not request.user.is_authenticated:
            return JsonResponse({'error': 'Authentication required'}, status=401)
        
        return None  # Continue normalement
    
    def process_response(self, request, response):
        # Logique après traitement de la vue (optionnel)
        return response