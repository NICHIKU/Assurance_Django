import json
from django.http import JsonResponse
from django.core.serializers.json import DjangoJSONEncoder

class ApiResponse:
    """
    Utility class for standardizing API responses.
    """
    
    @staticmethod
    def success(data=None, message="Success", status=200):
        """Returns a success response."""
        response_data = {
            'success': True,
            'message': message,
        }
        if data is not None:
            response_data['data'] = data
        return JsonResponse(response_data, status=status, encoder=DjangoJSONEncoder)
    
    @staticmethod
    def error(message="Error", status=400, errors=None):
        """Returns an error response."""
        response_data = {
            'success': False,
            'message': message,
        }
        if errors:
            response_data['errors'] = errors
        return JsonResponse(response_data, status=status)
    
    @staticmethod
    def created(data=None, message="Resource created successfully"):
        """Returns a creation response (201)."""
        return ApiResponse.success(data=data, message=message, status=201)
    
    @staticmethod
    def not_found(message="Resource not found"):
        """Returns a 404 response."""
        return ApiResponse.error(message=message, status=404)
    
    @staticmethod
    def unauthorized(message="Authentication required"):
        """Returns a 401 response.""" 
        return ApiResponse.error(message=message, status=401)
    
    @staticmethod
    def forbidden(message="Access denied"):
        """Returns a 403 response."""
        return ApiResponse.error(message=message, status=403)

def get_client_ip(request):
    """
    Retrieves the client's IP address.
    """
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def validate_required_fields(data, required_fields):
    """
    Validates the presence of required fields in the data.
    """
    missing_fields = [field for field in required_fields if field not in data]
    if missing_fields:
        return False, f"Missing required fields: {', '.join(missing_fields)}"
    return True, None
