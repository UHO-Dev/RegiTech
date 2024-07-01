from django.shortcuts import redirect

# dispatch_decorator_admin
def admin_required(function):
    
    def wrap(request, *args, **kwargs):
        if request.user.rol != "Administrador":
            return redirect('Estadisticas')
        return function(request, *args, **kwargs)
    
    return wrap

def soporte_tecnico_required(function):
    
    def wrap(request, *args, **kwargs):
        if request.user.rol != "Soporte Tecnico":
            return redirect('Estadisticas')
        return function(request, *args, **kwargs)
    
    return wrap

def supervision_required(function):
    
    def wrap(request, *args, **kwargs):
        if request.user.rol != "Supervisor":
            return redirect('Estadisticas')
        return function(request, *args, **kwargs)
    
    return wrap

def jefe_area_required(function):
    
    def wrap(request, *args, **kwargs):
        if request.user.rol != "Jefe de Area":
            return redirect('Estadisticas')
        return function(request, *args, **kwargs)
    
    return wrap

def responsable_required(function):
    
    def wrap(request, *args, **kwargs):
        if request.user.rol != "Responsable":
            return redirect('Estadisticas')
        return function(request, *args, **kwargs)
    
    return wrap