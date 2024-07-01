from django.http import HttpResponseForbidden

class AdminOnlyMiddleware:
    
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        if not request.user.is_staff:
            return HttpResponseForbidden(
                "Acceso Prohibido.!Esta vista esta disponible solo para administradores"
                )
        return self.get_response(request)