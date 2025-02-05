from django.http import HttpResponseForbidden

def is_admin(view_func):
    def _wrapped_view(request, *args, **kwargs):
        if request.user.role != 'Manager':
            return HttpResponseForbidden("Você não tem permissão para acessar esta página.")
        return view_func(request, *args, **kwargs)
    return _wrapped_view

def is_manager(view_func):
    def _wrapped_view(request, *args, **kwargs):
        if request.user.role != 'Manager':
            return HttpResponseForbidden("Você não tem permissão para acessar esta página.")
        return view_func(request, *args, **kwargs)
    return _wrapped_view

def is_customer(view_func):
    def _wrapped_view(request, *args, **kwargs):
        if request.user.role != 'Customer':
            return HttpResponseForbidden("Você não tem permissão para acessar esta página.")
        return view_func(request, *args, **kwargs)
    return _wrapped_view
