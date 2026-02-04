from django.http import JsonResponse

def verification_required(view_func):
    """
    Decorator that checks whether the user is authenticated.
    Returns a 401 error if the user is not authenticated.
    """
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated:
            from django.shortcuts import redirect
            from django.urls import reverse
            return redirect('login')
        return view_func(request, *args, **kwargs)
    return _wrapped_view

def admin_required(view_func):
    """
    Decorator that checks whether the user is authenticated and is an administrator.
    Returns a 403 error if the user is not an administrator.
    """
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return JsonResponse({'error': 'Authentication required'}, status=401)
        if not request.user.is_staff:
            return JsonResponse({'error': 'Admin access required'}, status=403)
        return view_func(request, *args, **kwargs)
    return _wrapped_view
