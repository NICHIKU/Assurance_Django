from django.http import JsonResponse

def verification_required(view_func):
    """
    Décorateur qui vérifie si l'utilisateur est authentifié.
    Retourne une erreur 401 si l'utilisateur n'est pas authentifié.
    """
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return JsonResponse({'error': 'Authentication required'}, status=401)
        return view_func(request, *args, **kwargs)
    return _wrapped_view

def admin_required(view_func):
    """
    Décorateur qui vérifie si l'utilisateur est authentifié et est admin.
    Retourne une erreur 403 si l'utilisateur n'est pas admin.
    """
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return JsonResponse({'error': 'Authentication required'}, status=401)
        if not request.user.is_staff:
            return JsonResponse({'error': 'Admin access required'}, status=403)
        return view_func(request, *args, **kwargs)
    return _wrapped_view
