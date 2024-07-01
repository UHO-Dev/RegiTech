from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.utils.decorators import method_decorator
from .decorators import admin_required
from django.db.models import Count
from django.views.generic import (
    UpdateView, 
    DeleteView,
    )
from .models import (
    OrdenServicio, 
    Mantenimiento,
    Recursos,
    Incidencias,
    Perfil,
    TipoRecurso, 
    CentroCosto,
    Motherboard,
    CPU,
    Disco,
    Optica,
    Fuente,
    Video,
    Memoria,
    Componentes,
    TipoOrden,
    TipoIncidencia,
    # NEW MODELS
    Sede,
    Area,
    Departamento,
    CentrosCostos,
    # END NEW MODELS
)
from .forms import (
    RecursosForm, 
    ResponsableForm, 
    EstadoTecnicoForm, 
    AprobacionForm,
    SuministradorForm,
    UserCreationForm, 
    PassChangeForm,
    TipoRecursoForm,
    TipoIncidenciaForm,
    TipoOrdenForm,
    CentroCostoForm,
    UbicacionForm,
    LoginForm,
    PerfilForm,
    MotherboardForm,
    CPUForm,
    DiscoForm,
    OpticaForm,
    FuenteForm,
    VideoForm,
    MemoriaForm,
    ComponentesForm,
    IncidenciasForm,
    MantenimientoForm, 
    OrdenServicioForm,
    OrdenServicioEstadoForm,
    UserEditForm,
    # NEW FORMS MODELS #
    SedeForm,
    AreaForm,
    DepartamentoForm,
    CentrosCostosForm,
    # END NEW MODELS FORMS #
    )
from django.contrib.auth.views import ( 
    LogoutView, 
    PasswordChangeView, 
    PasswordChangeDoneView, 
    PasswordResetView, 
    PasswordResetDoneView, 
    PasswordResetConfirmView, 
    PasswordResetCompleteView,
    )

# -----------Admin Site---------------
@login_required
@admin_required
def adminSite(request):
    users = Perfil.objects.all()
    context = {
        'users': users,
        'section': 'Usuarios',
    }
    return render(request, "main/administracion_main.html", context)

# -----------Usuarios---------------
class UserDelete(DeleteView):
    model = Perfil
    template_name = 'usuarios/user_delete.html'
    success_url = reverse_lazy('AdminSite')
    
    @method_decorator(login_required, admin_required)
    def dispatch(self, request, *args, **kwargs):
        return super(UserDelete, self).dispatch(request, *args, **kwargs)

@login_required
@admin_required
def userCreate(request):
    if request.method == "GET":
        form = UserCreationForm()
        context = {
            'form':form,
            'section':'User',
        }
    else:
        form = UserCreationForm(request.POST)
        context = {
            'form':form,
        }
        if form.is_valid():
            form.save()
            return redirect('AdminSite')
        else:
            msg = "El nombre de usuario coincide con uno registrado con anterioridad."
            context = {
                'msg':msg,
                'form':form,
                'section':'User',
            }
    return render(request, 'usuarios/user_create.html', context)

@login_required
@admin_required
def userDetail(request, pk):
    perfil = Perfil.objects.get(id = pk)
    context = {
        'perfil':perfil,
        'section':'User',
    }
    return render(request, 'usuarios/user_detail.html', context)


@login_required
@admin_required
def userUpdate(request,pk):
    user = Perfil.objects.get(id = pk)
    if request.method == "GET":
        form = UserEditForm(instance = user)
        context = {
            'form': form,
            'section':'User',
        }
    else:
        form = UserEditForm(request.POST, instance = user)
        context = {
            'form':form,
        }
        if form.is_valid():
            form.save()
            return redirect('AdminSite')
        else:
            msg = "El email no tiene el formato correcto."
            context = {
                'msg':msg,
                'form':form,
                'section':'User',
            }
    return render(request, 'usuarios/user_update.html', context)
    
# -----------User Publico---------------
@login_required
@admin_required
def userDetailPublico(request, pk):
    perfil = Perfil.objects.get(id = pk)
    context = {
        'perfil':perfil,
        'section':'User',
    }
    return render(request, 'usuarios/user_detail_publico.html', context)
    
# -----------Autenticacion---------------
def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('Estadisticas')
            else:
                msg = 'Credenciales Inválidas.'
        else:
            msg = 'Error en la Validación del Formulario.'
    return render(request, "registration/login.html", {
        'form':form,
        'msg':msg,
        }
    )

class Logout(LogoutView):
    template_name = 'registration/logout.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(Logout, self).dispatch(request, *args, **kwargs)

# -----------Password Change---------------
class PasswordChange(PasswordChangeView):
    form_class = PassChangeForm
    template_name = "registration/password_change/passwordChange.html"

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(PasswordChange, self).dispatch(request, *args, **kwargs)
    
class PasswordChangeDone(PasswordChangeDoneView):
    template_name = "registration/password_change/passwordChangeDone.html"

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(PasswordChangeDone, self).dispatch(request, *args, **kwargs)
  
# -----------Password Reset---------------
class PasswordReset(PasswordResetView):
    email_template_name = "registration/password_reset/password_reset_email.html"
    success_url = reverse_lazy("password_reset_done")
    template_name = "registration/password_reset/password_reset_form.html"
    
class PasswordResetDone(PasswordResetDoneView):
    template_name = "registration/password_reset/password_reset_done.html"
    
class PasswordResetConfirm(PasswordResetConfirmView):
    template_name = "registration/password_reset/password_reset_confirm.html"
    success_url = reverse_lazy("password_reset_complete")
    
class PasswordResetComplete(PasswordResetCompleteView):
    template_name = "registration/password_reset/password_reset_complete.html"

# -----------Tipo de Recursos-------------------
@login_required
@admin_required
def tipoRecursoList(request):
    tipos = TipoRecurso.objects.all()
    context = {
        'tipos':tipos,
        'section': 'Tipo'
    }
    return render(request, "tipo/tipo_list.html", context)

@login_required
@admin_required
def tipoRecursoCreate(request):
    if request.method == "GET":
        form = TipoRecursoForm()
        context = {
            'form':form,
            'section':'Tipo',
        }
    else:
        form = TipoRecursoForm(request.POST)
        context = {
            'form':form,
        }
        if form.is_valid():
            form.save()
            return redirect('TipoRecursoList')
        else:
            msg = "El código coincide con un recurso registrado con anterioridad."
            context = {
                'msg':msg,
                'form':form,
                'section':'Tipo',
            }
    return render(request, 'tipo/tipo_create.html', context)

@login_required
@admin_required
def tipoRecursoUpdate(request,pk):
    tipo = TipoRecurso.objects.get(id = pk)
    if request.method == "GET":
        form = TipoRecursoForm(instance = tipo)
        context = {
            'form': form,
            'section':'Tipo',
        }
    else:
        form = TipoRecursoForm(request.POST, instance = tipo)
        context = {
            'form':form,
        }
        if form.is_valid():
            form.save()
            return redirect('TipoRecursoList')
        else:
            msg = "El código coincide con un recurso registrado con anterioridad."
            context = {
                'msg':msg,
                'form':form,
                'section':'Tipo',
            }
    return render(request, 'tipo/tipo_update.html', context)

class TipoRecursoDelete(DeleteView):
    model = TipoRecurso
    template_name = 'tipo/tipo_delete.html'
    success_url = reverse_lazy('TipoRecursoList')
    extra_context={'section': 'Tipo'}

    @method_decorator(login_required, admin_required)
    def dispatch(self, request, *args, **kwargs):
        return super(TipoRecursoDelete, self).dispatch(request, *args, **kwargs)

@login_required
@admin_required
def tipoRecursoDetail(request, pk):
    tipo = TipoRecurso.objects.get(id=pk)
    context = {
        'tipo':tipo,
        'section': 'Tipo'
    }
    return render(request, 'tipo/tipo_detail.html', context)

# -------------Tipo de Orden----------------------
@login_required
@admin_required
def tipoRecursoList(request):
    tipos = TipoRecurso.objects.all()
    context = {
        'tipos':tipos,
        'section': 'Tipo'
    }
    return render(request, "tipo/tipo_list.html", context)

@login_required
@admin_required
def tipoRecursoCreate(request):
    if request.method == "GET":
        form = TipoRecursoForm()
        context = {
            'form':form,
            'section':'Tipo',
        }
    else:
        form = TipoRecursoForm(request.POST)
        context = {
            'form':form,
        }
        if form.is_valid():
            form.save()
            return redirect('TipoRecursoList')
        else:
            msg = "El código coincide con un recurso registrado con anterioridad."
            context = {
                'msg':msg,
                'form':form,
                'section':'Tipo',
            }
    return render(request, 'tipo/tipo_create.html', context)

@login_required
@admin_required
def tipoRecursoUpdate(request,pk):
    tipo = TipoRecurso.objects.get(id = pk)
    if request.method == "GET":
        form = TipoRecursoForm(instance = tipo)
        context = {
            'form': form,
            'section':'Tipo',
        }
    else:
        form = TipoRecursoForm(request.POST, instance = tipo)
        context = {
            'form':form,
        }
        if form.is_valid():
            form.save()
            return redirect('TipoRecursoList')
        else:
            msg = "El código coincide con un recurso registrado con anterioridad."
            context = {
                'msg':msg,
                'form':form,
                'section':'Tipo',
            }
    return render(request, 'tipo/tipo_update.html', context)

class TipoRecursoDelete(DeleteView):
    model = TipoRecurso
    template_name = 'tipo/tipo_delete.html'
    success_url = reverse_lazy('TipoRecursoList')
    extra_context={'section': 'Tipo'}

    @method_decorator(login_required, admin_required)
    def dispatch(self, request, *args, **kwargs):
        return super(TipoRecursoDelete, self).dispatch(request, *args, **kwargs)

@login_required
@admin_required
def tipoRecursoDetail(request, pk):
    tipo = TipoRecurso.objects.get(id=pk)
    context = {
        'tipo':tipo,
        'section': 'Tipo'
    }
    return render(request, 'tipo/tipo_detail.html', context)

# -----------Tipo de Incidencia-------------------
@login_required
@admin_required
def tipoIncidenciaList(request):
    tipos = TipoIncidencia.objects.all()
    context = {
        'tipos':tipos,
        'section': 'Incidencia'
    }
    return render(request, "tipo_incidencia/tipo_incidencia_list.html", context)

@login_required
@admin_required
def tipoIncidenciaCreate(request):
    if request.method == "GET":
        form = TipoIncidenciaForm()
        context = {
            'form':form,
            'section':'Incidencia',
        }
    else:
        form = TipoIncidenciaForm(request.POST)
        context = {
            'form':form,
        }
        if form.is_valid():
            form.save()
            return redirect('TipoIncidenciaList')
        else:
            msg = "El nómbre de la Incidencia coincide con una registrada con anterioridad."
            context = {
                'msg':msg,
                'form':form,
                'section':'Incidencia',
            }
    return render(request, 'tipo_incidencia/tipo_incidencia_create.html', context)

@login_required
@admin_required
def tipoIncidenciaUpdate(request,pk):
    tipo = TipoIncidencia.objects.get(id = pk)
    if request.method == "GET":
        form = TipoIncidenciaForm(instance = tipo)
        context = {
            'form': form,
            'section':'Incidencia',
        }
    else:
        form = TipoIncidenciaForm(request.POST, instance = tipo)
        context = {
            'form':form,
        }
        if form.is_valid():
            form.save()
            return redirect('TipoIncidenciaList')
        else:
            msg = "El nómbre de la Incidencia coincide con una registrada con anterioridad."
            context = {
                'msg':msg,
                'form':form,
                'section':'Incidencia',
            }
    return render(request, 'tipo_incidencia/tipo_incidencia_update.html', context)

class TipoIncidenciaDelete(DeleteView):
    model = TipoIncidencia
    template_name = 'tipo_incidencia/tipo_incidencia_delete.html'
    success_url = reverse_lazy('TipoIncidenciaList')
    extra_context={'section': 'Incidencia'}

    @method_decorator(login_required, admin_required)
    def dispatch(self, request, *args, **kwargs):
        return super(TipoIncidenciaDelete, self).dispatch(request, *args, **kwargs)

@login_required
@admin_required
def tipoIncidenciaDetail(request, pk):
    tipo = TipoIncidencia.objects.get(id=pk)
    context = {
        'tipo':tipo,
        'section': 'Incidencia'
    }
    return render(request, 'tipo_incidencia/tipo_incidencia_detail.html', context)


# -----------Tipo de Orden-------------------
@login_required
@admin_required
def tipoOrdenList(request):
    tipos = TipoOrden.objects.all()
    context = {
        'tipos':tipos,
        'section': 'Orden'
    }
    return render(request, "tipo_orden/tipo_orden_list.html", context)

@login_required
@admin_required
def tipoOrdenCreate(request):
    if request.method == "GET":
        form = TipoOrdenForm()
        context = {
            'form':form,
            'section':'Orden',
        }
    else:
        form = TipoOrdenForm(request.POST)
        context = {
            'form':form,
        }
        if form.is_valid():
            form.save()
            return redirect('TipoOrdenList')
        else:
            msg = "El nómbre de la Orden de Servicio coincide con una registrada con anterioridad."
            context = {
                'msg':msg,
                'form':form,
                'section':'Orden',
            }
    return render(request, 'tipo_orden/tipo_orden_create.html', context)

@login_required
@admin_required
def tipoOrdenUpdate(request,pk):
    tipo = TipoOrden.objects.get(id = pk)
    if request.method == "GET":
        form = TipoOrdenForm(instance = tipo)
        context = {
            'form': form,
            'section':'Orden',
        }
    else:
        form = TipoOrdenForm(request.POST, instance = tipo)
        context = {
            'form':form,
        }
        if form.is_valid():
            form.save()
            return redirect('TipoOrdenList')
        else:
            msg = "El nómbre de la Orden de Servicio coincide con una registrada con anterioridad."
            context = {
                'msg':msg,
                'form':form,
                'section':'Orden',
            }
    return render(request, 'tipo_orden/tipo_orden_update.html', context)

class TipoOrdenDelete(DeleteView):
    model = TipoOrden
    template_name = 'tipo_orden/tipo_orden_delete.html'
    success_url = reverse_lazy('TipoOrdenList')
    extra_context={'section': 'Orden'}

    @method_decorator(login_required, admin_required)
    def dispatch(self, request, *args, **kwargs):
        return super(TipoOrdenDelete, self).dispatch(request, *args, **kwargs)

@login_required
@admin_required
def tipoOrdenDetail(request, pk):
    tipo = TipoOrden.objects.get(id=pk)
    context = {
        'tipo':tipo,
        'section': 'Orden'
    }
    return render(request, 'tipo_orden/tipo_orden_detail.html', context)

# -----------Centro_Costo---------------
@login_required
@admin_required
def centroCostoList(request):
    centros = CentroCosto.objects.all()
    context = {
        'centros':centros,
        'section': 'Ubicacion'
    }
    return render(request, "centro_costo/centro_costo_list.html", context)
    
class CentroCostoDelete(DeleteView):
    model = CentroCosto
    template_name = 'centro_costo/centro_costo_delete.html'
    success_url = reverse_lazy('CentroCostoList')
    extra_context={'section': 'Ubicacion'}

    @method_decorator(login_required, admin_required)
    def dispatch(self, request, *args, **kwargs):
        return super(CentroCostoDelete, self).dispatch(request, *args, **kwargs)
    
@login_required
@admin_required
def centroCostoUpdate(request,pk):
    centro = CentroCosto.objects.get(id = pk)
    if request.method == "GET":
        form = UbicacionForm(instance = centro)
        context = {
            'form': form,
            'section': 'Tipo',
        }
    else:
        form = UbicacionForm(request.POST, instance = centro)
        context = {
            'form': form,
        }
        if form.is_valid():
            form.save()
            return redirect('CentroCostoList')
        else:
            msg = "El código coincide con un centro de costo registrado con anterioridad."
            context = {
                'msg': msg,
                'form': form,
                'section': 'Ubicacion',
            }
    return render(request, 'centro_costo/centro_costo_update.html', context)

@login_required
@admin_required
def centroCostoCreate(request):
    if request.method == "GET":
        form = UbicacionForm()
        context = {
            'form': form,
            'section': 'Ubicacion',
        }
    else:
        form = CentroCostoForm(request.POST)
        context = {
            'form': form,
        }
        if form.is_valid():
            form.save()
            return redirect('CentroCostoList')
        else:
            msg = "El código coincide con un centro de costo registrado con anterioridad."
            context = {
                'msg': msg,
                'form': form,
                'section': 'Ubicacion'
            }
    return render (request, 'centro_costo/centro_costo_create.html', context)

@login_required
@admin_required
def centroCostoDetail(request, pk):
    centro = CentroCosto.objects.get(id = pk)
    context = {
        'centro':centro,
        'section':'Ubicacion',
    }
    return render(request, 'centro_costo/centro_costo_detail.html', context)

# ----------------NEW MODELS VIEWS--------------------
# ----------------------Sede--------------------------
@login_required
def sedeList(request):
    sedes = Sede.objects.all()
    context = {
        'sedes':sedes,
        'section': 'Sede'
    }
    return render(request, "sede/sede_list.html", context)
    
class SedeDelete(DeleteView):
    model = Sede
    template_name = 'sede/sede_delete.html'
    success_url = reverse_lazy('SedeList')
    extra_context={'section': 'Sede'}

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(SedeDelete, self).dispatch(request, *args, **kwargs)
    
@login_required
def sedeUpdate(request,pk):
    sede = Sede.objects.get(id = pk)
    if request.method == "GET":
        form = SedeForm(instance = sede)
        context = {
            'form': form,
            'section': 'Sede',
        }
    else:
        form = SedeForm(request.POST, instance = sede)
        context = {
            'form': form,
        }
        if form.is_valid():
            form.save()
            return redirect('SedeList')
        else:
            msg = "El nombre coincide con una sede registrada con anterioridad."
            context = {
                'msg': msg,
                'form': form,
                'section': 'Sede',
            }
    return render(request, 'sede/sede_update.html', context)

@login_required
@admin_required
def sedeCreate(request):
    if request.method == "GET":
        form = SedeForm()
        context = {
            'form': form,
            'section': 'Sede',
        }
    else:
        form = SedeForm(request.POST)
        context = {
            'form': form,
        }
        if form.is_valid():
            form.save()
            return redirect('SedeList')
        else:
            msg = "El nombre coincide con una sede registrada con anterioridad."
            context = {
                'msg': msg,
                'form': form,
                'section': 'Sede'
            }
    return render (request, 'sede/sede_create.html', context)

# ----------------------Area--------------------------
@login_required
@admin_required
def areaList(request):
    areas = Area.objects.all()
    context = {
        'areas':areas,
        'section': 'Area',
    }
    return render(request, "area/area_list.html", context)
    
class AreaDelete(DeleteView):
    model = Area
    template_name = 'area/area_delete.html'
    success_url = reverse_lazy('AreaList')
    extra_context={'section': 'Area'}

    @method_decorator(login_required, admin_required)
    def dispatch(self, request, *args, **kwargs):
        return super(AreaDelete, self).dispatch(request, *args, **kwargs)
    
@login_required
@admin_required
def areaUpdate(request,pk):
    area = Area.objects.get(id = pk)
    if request.method == "GET":
        form = AreaForm(instance = area)
        context = {
            'form': form,
            'section': 'Area',
        }
    else:
        form = AreaForm(request.POST, instance = area)
        context = {
            'form': form,
        }
        if form.is_valid():
            form.save()
            return redirect('AreaList')
        else:
            msg = "El nombre coincide con una area registrada con anterioridad o los usuarios estan asignados a otras areas."
            context = {
                'msg': msg,
                'form': form,
                'section': 'Area',
            }
    return render(request, 'area/area_update.html', context)

@login_required
@admin_required
def areaCreate(request):
    if request.method == "GET":
        form = AreaForm()
        context = {
            'form': form,
            'section': 'Area',
        }
    else:
        form = AreaForm(request.POST)
        context = {
            'form': form,
        }
        if form.is_valid():
            form.save()
            return redirect('AreaList')
        else:
            msg = "El nombre coincide con una area registrada con anterioridad o los usuarios estan asignados a otras areas."
            context = {
                'msg': msg,
                'form': form,
                'section': 'Area'
            }
    return render (request, 'area/area_create.html', context)
# ------------------Departamento----------------------
@login_required
@admin_required
def departamentoList(request):
    departamentos = Departamento.objects.all()
    context = {
        'departamentos':departamentos,
        'section': 'Departamento'
    }
    return render(request, "departamento/departamento_list.html", context)
    
class DepartamentoDelete(DeleteView):
    model = Departamento
    template_name = 'departamento/departamento_delete.html'
    success_url = reverse_lazy('DepartamentoList')
    extra_context={'section': 'Departamento'}

    @method_decorator(login_required, admin_required)
    def dispatch(self, request, *args, **kwargs):
        return super(DepartamentoDelete, self).dispatch(request, *args, **kwargs)
    
@login_required
@admin_required
def departamentoUpdate(request,pk):
    departamento = Departamento.objects.get(id = pk)
    if request.method == "GET":
        form = DepartamentoForm(instance = departamento)
        context = {
            'form': form,
            'section': 'Departamento',
        }
    else:
        form = DepartamentoForm(request.POST, instance = departamento)
        context = {
            'form': form,
        }
        if form.is_valid():
            form.save()
            return redirect('DepartamentoList')
        else:
            msg = "El nombre coincide con un departamento registrado con anterioridad."
            context = {
                'msg': msg,
                'form': form,
                'section': 'Departamento',
            }
    return render(request, 'departamento/departamento_update.html', context)

@login_required
@admin_required
def departamentoCreate(request):
    if request.method == "GET":
        form = DepartamentoForm()
        context = {
            'form': form,
            'section': 'Departamento',
        }
    else:
        form = DepartamentoForm(request.POST)
        context = {
            'form': form,
        }
        if form.is_valid():
            form.save()
            return redirect('DepartamentoList')
        else:
            msg = "El nombre coincide con un departamento registrado con anterioridad."
            context = {
                'msg': msg,
                'form': form,
                'section': 'Departamento'
            }
    return render (request, 'departamento/departamento_create.html', context)

@login_required
@admin_required
def departamentoDetail(request, pk):
    departamento = Departamento.objects.get(id = pk)
    context = {
        'departamento':departamento,
        'section':'Departamento',
    }
    return render(request, 'departamento/departamento_detail.html', context)


#--------------------CentrosCostos--------------------
@login_required
@admin_required
def centrosCostosList(request):
    centros = CentrosCostos.objects.all()
    context = {
        'centros':centros,
        'section': 'Ubicacion'
    }
    return render(request, "centros_costos/centros_costos_list.html", context)
    
class CentrosCostosDelete(DeleteView):
    model = CentrosCostos
    template_name = 'centros_costos/centros_costos_delete.html'
    success_url = reverse_lazy('CentrosCostosList')
    extra_context={'section': 'Ubicacion'}

    @method_decorator(login_required, admin_required)
    def dispatch(self, request, *args, **kwargs):
        return super(CentrosCostosDelete, self).dispatch(request, *args, **kwargs)
    
@login_required
@admin_required
def centrosCostosUpdate(request,pk):
    centros = CentrosCostos.objects.get(id = pk)
    if request.method == "GET":
        form = CentrosCostosForm(instance = centros)
        context = {
            'form': form,
            'section': 'Ubicacion',
        }
    else:
        form = CentrosCostosForm(request.POST, instance = centros)
        context = {
            'form': form,
        }
        if form.is_valid():
            form.save()
            return redirect('CentrosCostosList')
        else:
            msg = "El código coincide con un centro de costo registrado con anterioridad."
            context = {
                'msg': msg,
                'form': form,
                'section': 'Ubicacion',
            }
    return render(request, 'centros_costos/centros_costos_update.html', context)

@login_required
@admin_required
def centrosCostosCreate(request):
    if request.method == "GET":
        form = CentrosCostosForm()
        context = {
            'form': form,
            'section': 'Ubicacion',
        }
    else:
        form = CentrosCostosForm(request.POST)
        context = {
            'form': form,
        }
        if form.is_valid():
            form.save()
            return redirect('CentrosCostosList')
        else:
            msg = "El código coincide con un centro de costo registrado con anterioridad."
            context = {
                'msg': msg,
                'form': form,
                'section': 'Ubicacion'
            }
    return render (request, 'centros_costos/centros_costos_create.html', context)

@login_required
@admin_required
def centrosCostosDetail(request, pk):
    centros = CentrosCostos.objects.get(id = pk)
    context = {
        'centros':centros,
        'section':'Ubicacion',
    }
    return render(request, 'centros_costos/centros_costos_detail.html', context)

# --------------END NEW MODELS VIEWS------------------
@login_required
@admin_required
def centroCostoList(request):
    centros = CentroCosto.objects.all()
    context = {
        'centros':centros,
        'section': 'Ubicacion'
    }
    return render(request, "centro_costo/centro_costo_list.html", context)
    
class CentroCostoDelete(DeleteView):
    model = CentroCosto
    template_name = 'centro_costo/centro_costo_delete.html'
    success_url = reverse_lazy('CentroCostoList')
    extra_context={'section': 'Ubicacion'}

    @method_decorator(login_required, admin_required)
    def dispatch(self, request, *args, **kwargs):
        return super(CentroCostoDelete, self).dispatch(request, *args, **kwargs)
    
@login_required
@admin_required
def centroCostoUpdate(request,pk):
    centro = CentroCosto.objects.get(id = pk)
    if request.method == "GET":
        form = UbicacionForm(instance = centro)
        context = {
            'form': form,
            'section': 'Tipo',
        }
    else:
        form = UbicacionForm(request.POST, instance = centro)
        context = {
            'form': form,
        }
        if form.is_valid():
            form.save()
            return redirect('CentroCostoList')
        else:
            msg = "El código coincide con un centro de costo registrado con anterioridad."
            context = {
                'msg': msg,
                'form': form,
                'section': 'Ubicacion',
            }
    return render(request, 'centro_costo/centro_costo_update.html', context)

@login_required
@admin_required
def centroCostoCreate(request):
    if request.method == "GET":
        form = UbicacionForm()
        context = {
            'form': form,
            'section': 'Ubicacion',
        }
    else:
        form = CentroCostoForm(request.POST)
        context = {
            'form': form,
        }
        if form.is_valid():
            form.save()
            return redirect('CentroCostoList')
        else:
            msg = "El código coincide con un centro de costo registrado con anterioridad."
            context = {
                'msg': msg,
                'form': form,
                'section': 'Ubicacion'
            }
    return render (request, 'centro_costo/centro_costo_create.html', context)

@login_required
@admin_required
def centroCostoDetail(request, pk):
    centro = CentroCosto.objects.get(id = pk)
    context = {
        'centro':centro,
        'section':'Ubicacion',
    }
    return render(request, 'centro_costo/centro_costo_detail.html', context)

# --------------Perfil------------------
@login_required
def perfilUpdate(request,pk):
    perfil = Perfil.objects.get(id = pk)
    if request.method == "GET":
        form = PerfilForm(instance = perfil)
        context = {
            'form': form,
        }
    else:
        form = PerfilForm(request.POST, instance = perfil)
        context = {
            'form': form,
        }
        if form.is_valid():
            form.save()
            return redirect('UserDetailPublico', pk)
        else:
            msg = "El carnet de identidad coincide con un usuario registrado con anterioridad."
            context = {
                'msg': msg,
                'form': form,
            }
    return render(request, 'usuarios/user_profile_update.html', context)
# -----------Historial-------------------
@login_required
@admin_required
def AdminLogs(request):
    recursos = Recursos.objects.all()
    ordenes = OrdenServicio.objects.all()
    mantenimientos = Mantenimiento.objects.all()
    incidencias = Incidencias.objects.all()
    usuarios = Perfil.objects.all()
    logs = []
    logs = list(logs)

    for recurso in recursos:
        [logs.append((log,"Recursos")) for log in recurso.historial.all()]
    for orden in ordenes:
        [logs.append((log,"Orden Servicio")) for log in orden.historial.all()]
    for mantenimiento in mantenimientos:
        [logs.append((log,"Mantenimiento")) for log in mantenimiento.historial.all()]
    for incidencia in incidencias:
        [logs.append((log,"Incidencias")) for log in incidencia.historial.all()]
    for user in usuarios:
        [logs.append((log,"Usuarios")) for log in user.historial.all()]
    context={
        'admin_logs':logs,
    }
    return render(request, 'logs/administracion_logs.html', context)

# FICHA TECNICA
@login_required
def ficha_tecnica(request, pk):
    recurso = Recursos.objects.get(id = pk)
    historial = recurso.historial.all()
    context = {
        'historial':historial,
        'recurso':recurso,
    }
    return render(request, 'ficha_tecnica/ficha_tecnica.html', context)

# LISTADO DE COMPONENTES #
@login_required
@admin_required
def AlmacenComponentes(request):
    motherboard = Motherboard.objects.all()
    motherboard_c = Motherboard.objects.count()
    cpu = CPU.objects.all()
    cpu_c = CPU.objects.count()
    disco = Disco.objects.all()
    disco_c = Disco.objects.count()
    optica = Optica.objects.all()
    optica_c = Optica.objects.count()
    fuente = Fuente.objects.all()
    fuente_c = Fuente.objects.count()
    video = Video.objects.all()
    video_c = Video.objects.count()
    memoria = Memoria.objects.all()
    memoria_c = Memoria.objects.count()
    
    context = {
        'motherboard':motherboard,
        'motherboard_c':motherboard_c,
        'cpu':cpu,
        'cpu_c':cpu_c,
        'disco':disco,
        'disco_c':disco_c,
        'optica':optica,
        'optica_c':optica_c,
        'fuente':fuente,
        'fuente_c':fuente_c,
        'video':video,
        'video_c':video_c,
        'memoria':memoria,
        'memoria_c':memoria_c,
        'section': 'Almacen',
    }
    return render(request, 'almacen/almacen.html', context)

#-------------------------MOTHERBOARD--------------------------------#
class MotherboardDelete(DeleteView):
    model = Motherboard
    template_name = 'motherboard/motherboard_delete.html'
    success_url = reverse_lazy('AlmacenList')

    @method_decorator(login_required, admin_required)
    def dispatch(self, request, *args, **kwargs):
        return super(MotherboardDelete, self).dispatch(request, *args, **kwargs)
    
@login_required
@admin_required
def motherboardCreate(request):
    if request.method == "GET":
        form = MotherboardForm()
        context = {
            'form': form,
            'section': 'Almacen',
        }
    else:
        form = MotherboardForm(request.POST)
        context = {
            'form': form,
        }
        if form.is_valid():
            form.save()
            return redirect('AlmacenList')
        else:
            msg = "El número de serie coincide con una motherboard registrada con anterioridad."
            context = {
                'msg': msg,
                'form': form,
                'section': 'Almacen',
            }
    return render(request, 'motherboard/motherboard_create.html', context)

@login_required
@admin_required
def motherboardUpdate(request,pk):
    motherboard = Motherboard.objects.get(id = pk)
    if request.method == "GET":
        form = MotherboardForm(instance = motherboard)
        context = {
            'form': form,
            'section': 'Almacen'
        }
    else:
        form = MotherboardForm(request.POST, instance = motherboard)
        context = {
            'form': form,
        }
        if form.is_valid():
            form.save()
            return redirect('AlmacenList')
        else:
            msg = "El número de serie coincide con una motherboard registrada con anterioridad."
            context = {
                'msg': msg,
                'form': form,
                'section': 'Almacen',
            } 
    return render(request, 'motherboard/motherboard_update.html', context)


    
#-----------------------------CPU------------------------------------#
class CPUDelete(DeleteView):
    model = CPU
    template_name = 'cpu/cpu_delete.html'
    success_url = reverse_lazy('AlmacenList')

    @method_decorator(login_required, admin_required)
    def dispatch(self, request, *args, **kwargs):
        return super(CPUDelete, self).dispatch(request, *args, **kwargs)

@login_required
@admin_required
def cpuCreate(request):
    if request.method == "GET":
        form = CPUForm()
        context = {
            'form': form,
            'section': 'Almacen',
        }
    else:
        form = CPUForm(request.POST)
        context = {
            'form': form,
        }
        if form.is_valid():
            form.save()
            return redirect('AlmacenList')
        else:
            msg = "El número de serie coincide con una CPU registrada con anterioridad."
            context = {
                'msg': msg,
                'form': form,
                'section': 'Almacen',
            }
    return render(request, 'cpu/cpu_create.html', context)

@login_required
@admin_required
def cpuUpdate(request,pk):
    cpu = CPU.objects.get(id = pk)
    if request.method == "GET":
        form = CPUForm(instance = cpu)
        context = {
            'form': form,
            'section': 'Almacen'
        }
    else:
        form = CPUForm(request.POST, instance = cpu)
        context = {
            'form': form,
        }
        if form.is_valid():
            form.save()
            return redirect('AlmacenList')
        else:
            msg = "El número de serie coincide con una cpu registrada con anterioridad."
            context = {
                'msg': msg,
                'form': form,
                'section': 'Almacen',
            } 
    return render(request, 'cpu/cpu_update.html', context)

#----------------------------DISCO-----------------------------------#
class DiscoDelete(DeleteView):
    model = Disco
    template_name = 'disco/disco_delete.html'
    success_url = reverse_lazy('AlmacenList')

    @method_decorator(login_required, admin_required)
    def dispatch(self, request, *args, **kwargs):
        return super(DiscoDelete, self).dispatch(request, *args, **kwargs)

@login_required
@admin_required
def discoCreate(request):
    if request.method == "GET":
        form = DiscoForm()
        context = {
            'form': form,
            'section': 'Almacen',
        }
    else:
        form = DiscoForm(request.POST)
        context = {
            'form': form,
        }
        if form.is_valid():
            form.save()
            return redirect('AlmacenList')
        else:
            msg = "El número de serie coincide con un Disco registrado con anterioridad."
            context = {
                'msg': msg,
                'form': form,
                'section': 'Almacen',
            }
    return render(request, 'disco/disco_create.html', context)

@login_required
@admin_required
def discoUpdate(request,pk):
    disco = Disco.objects.get(id = pk)
    if request.method == "GET":
        form = DiscoForm(instance = disco)
        context = {
            'form': form,
            'section': 'Almacen'
        }
    else:
        form = DiscoForm(request.POST, instance = disco)
        context = {
            'form': form,
        }
        if form.is_valid():
            form.save()
            return redirect('AlmacenList')
        else:
            msg = "El número de serie coincide con un disco registrado con anterioridad."
            context = {
                'msg': msg,
                'form': form,
                'section': 'Almacen',
            } 
    return render(request, 'disco/disco_update.html', context)

#----------------------------OPTICA----------------------------------#
class OpticaDelete(DeleteView):
    model = Optica
    template_name = 'optica/optica_delete.html'
    success_url = reverse_lazy('AlmacenList')

    @method_decorator(login_required, admin_required)
    def dispatch(self, request, *args, **kwargs):
        return super(OpticaDelete, self).dispatch(request, *args, **kwargs)

@login_required
@admin_required
def opticaCreate(request):
    if request.method == "GET":
        form = OpticaForm()
        context = {
            'form': form,
            'section': 'Almacen',
        }
    else:
        form = OpticaForm(request.POST)
        context = {
            'form': form,
        }
        if form.is_valid():
            form.save()
            return redirect('AlmacenList')
        else:
            msg = "El número de serie coincide con una Unidad Optica registrada con anterioridad."
            context = {
                'msg': msg,
                'form': form,
                'section': 'Almacen',
            }
    return render(request, 'optica/optica_create.html', context)

@login_required
@admin_required
def opticaUpdate(request,pk):
    optica = Optica.objects.get(id = pk)
    if request.method == "GET":
        form = OpticaForm(instance = optica)
        context = {
            'form': form,
            'section': 'Almacen'
        }
    else:
        form = OpticaForm(request.POST, instance = optica)
        context = {
            'form': form,
        }
        if form.is_valid():
            form.save()
            return redirect('AlmacenList')
        else:
            msg = "El número de serie coincide con una unidad &ocute;ptica registrada con anterioridad."
            context = {
                'msg': msg,
                'form': form,
                'section': 'Almacen',
            } 
    return render(request, 'optica/optica_update.html', context)

#----------------------------FUENTE----------------------------------#
class FuenteDelete(DeleteView):
    model = Fuente
    template_name = 'fuente/fuente_delete.html'
    success_url = reverse_lazy('AlmacenList')

    @method_decorator(login_required, admin_required)
    def dispatch(self, request, *args, **kwargs):
        return super(FuenteDelete, self).dispatch(request, *args, **kwargs)

@login_required
@admin_required
def fuenteCreate(request):
    if request.method == "GET":
        form = FuenteForm()
        context = {
            'form': form,
            'section': 'Almacen',
        }
    else:
        form = FuenteForm(request.POST)
        context = {
            'form': form,
        }
        if form.is_valid():
            form.save()
            return redirect('AlmacenList')
        else:
            msg = "El número de serie coincide con una Fuente registrada con anterioridad."
            context = {
                'msg': msg,
                'form': form,
                'section': 'Almacen',
            }
    return render(request, 'fuente/fuente_create.html', context)

@login_required
@admin_required
def fuenteUpdate(request,pk):
    fuente = Fuente.objects.get(id = pk)
    if request.method == "GET":
        form = FuenteForm(instance = fuente)
        context = {
            'form': form,
            'section': 'Almacen'
        }
    else:
        form = FuenteForm(request.POST, instance = fuente)
        context = {
            'form': form,
        }
        if form.is_valid():
            form.save()
            return redirect('AlmacenList')
        else:
            msg = "El número de serie coincide con una fuente registrada con anterioridad."
            context = {
                'msg': msg,
                'form': form,
                'section': 'Almacen',
            } 
    return render(request, 'fuente/fuente_update.html', context)
    
#----------------------------VIDEO-----------------------------------#
class VideoDelete(DeleteView):
    model = Video
    template_name = 'video/video_delete.html'
    success_url = reverse_lazy('AlmacenList')

    @method_decorator(login_required, admin_required)
    def dispatch(self, request, *args, **kwargs):
        return super(VideoDelete, self).dispatch(request, *args, **kwargs)

@login_required
@admin_required
def videoCreate(request):
    if request.method == "GET":
        form = VideoForm()
        context = {
            'form': form,
            'section': 'Almacen',
        }
    else:
        form = VideoForm(request.POST)
        context = {
            'form': form,
        }
        if form.is_valid():
            form.save()
            return redirect('AlmacenList')
        else:
            msg = "El número de serie coincide con una Tarjeta de Video registrada con anterioridad."
            context = {
                'msg': msg,
                'form': form,
                'section': 'Almacen',
            }
    return render(request, 'video/video_create.html', context)

@login_required
@admin_required
def videoUpdate(request,pk):
    video = Video.objects.get(id = pk)
    if request.method == "GET":
        form = VideoForm(instance = video)
        context = {
            'form': form,
            'section': 'Almacen'
        }
    else:
        form = VideoForm(request.POST, instance = video)
        context = {
            'form': form,
        }
        if form.is_valid():
            form.save()
            return redirect('AlmacenList')
        else:
            msg = "El número de serie coincide con una tarjeta de video registrada con anterioridad."
            context = {
                'msg': msg,
                'form': form,
                'section': 'Almacen',
            } 
    return render(request, 'video/video_update.html', context)

#-----------------------------RAM------------------------------------#
class RAMDelete(DeleteView):
    model = Memoria
    template_name = 'ram/ram_delete.html'
    success_url = reverse_lazy('AlmacenList')

    @method_decorator(login_required, admin_required)
    def dispatch(self, request, *args, **kwargs):
        return super(RAMDelete, self).dispatch(request, *args, **kwargs)

@login_required
@admin_required
def ramCreate(request):
    if request.method == "GET":
        form = MemoriaForm()
        context = {
            'form': form,
            'section': 'Almacen',
        }
    else:
        form = MemoriaForm(request.POST)
        context = {
            'form': form,
        }
        if form.is_valid():
            form.save()
            return redirect('AlmacenList')
        else:
            msg = "El número de serie coincide con una Memoria RAM registrada con anterioridad."
            context = {
                'msg': msg,
                'form': form,
                'section': 'Almacen',
            }
    return render(request, 'ram/ram_create.html', context)

@login_required
@admin_required
def ramUpdate(request,pk):
    ram = Memoria.objects.get(id = pk)
    if request.method == "GET":
        form = MemoriaForm(instance = ram)
        context = {
            'form': form,
            'section': 'Almacen'
        }
    else:
        form = MemoriaForm(request.POST, instance = ram)
        context = {
            'form': form,
        }
        if form.is_valid():
            form.save()
            return redirect('AlmacenList')
        else:
            msg = "El número de serie coincide con una memoria RAM registrada con anterioridad."
            context = {
                'msg': msg,
                'form': form,
                'section': 'Almacen',
            } 
    return render(request, 'ram/ram_update.html', context)

#---------------------------COMPONENTES----------------------------------#
@login_required
def componentesList(request):
    componentes = Componentes.objects.all()
    context = {
        'componentes': componentes,
        'section':[
            'Expedientes',
        ]
    }
    return render(request, 'expedientes/expedientes_list.html', context)

@login_required
def componentesCreate(request):
    if request.method == "GET":
        form = ComponentesForm()
        context = {
            'form': form,
            'section': 'Componentes',
        }
    else:
        form = ComponentesForm(request.POST)
        context = {
            'form': form,
        }
        if form.is_valid():
            form.save()
            return redirect('ComponentesList')
        else:
            msg = "Algun componente esta registrado en otro equipo o el MAC no tiene el formato correcto."
            context = {
                'msg': msg,
                'form': form,
                'section': 'Almacen',
            }
    return render(request, 'expedientes/expedientes_create.html', context)

@login_required
def componentesUpdate(request,pk):
    componente = Componentes.objects.get(id = pk)
    if request.method == "GET":
        form = ComponentesForm(instance = componente)
        context = {
            'form': form,
            'section': 'Almacen'
        }
    else:
        form = ComponentesForm(request.POST, instance = componente)
        context = {
            'form': form,
        }
        if form.is_valid():
            form.save()
            return redirect('ComponentesList')
        else:
            msg = "Algun componente esta registrado en otro equipo o el MAC no tiene el formato correcto."
            context = {
                'msg': msg,
                'form': form,
                'section': 'Almacen',
            } 
    return render(request, 'expedientes/expedientes_update.html', context)

@login_required
def componentesDetail(request, pk):
    componente = Componentes.objects.get(id = pk)
    context = {
        'componente':componente,
    }
    return render(request, 'expedientes/expedientes_detail.html', context)

class ComponentesDelete(DeleteView):
    model = Componentes
    template_name = 'expedientes/expedientes_delete.html'
    success_url = reverse_lazy('ComponentesList')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(ComponentesDelete, self).dispatch(request, *args, **kwargs)
    
@login_required
def incidenciasList(request):
    incidencias = Incidencias.objects.all()
    context = {
        'incidencias':incidencias,
        'section': 'Incidencias'
    }
    return render(request, "incidencias/incidencias_list.html", context)
    
class IncidenciasDelete(DeleteView):
    model = Incidencias
    template_name = 'incidencias/incidencias_delete.html'
    success_url = reverse_lazy('IncidenciasList')
    extra_context={'section': 'Incidencias'}

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(IncidenciasDelete, self).dispatch(request, *args, **kwargs)
    
@login_required
def incidenciasUpdate(request,pk):
    incidencia = Incidencias.objects.get(id = pk)
    if request.method == "GET":
        form = IncidenciasForm(instance = incidencia)
        context = {
            'form': form,
            'section': 'Incidencias'
        }
    else:
        form = IncidenciasForm(request.POST, instance = incidencia)
        context = {
            'form': form,
        }
        if form.is_valid():
            form.save()
            return redirect('IncidenciasList')
    return render(request, 'incidencias/incidencias_update.html', context)

@login_required
def incidenciasCreate(request):
    if request.method == "GET":
        form = IncidenciasForm()
        context = {
            'form':form,
            'section':'Incidencias',
        }
    else:
        form = IncidenciasForm(request.POST)
        context = {
            'form':form
        }
        if form.is_valid():
            form.save()
            return redirect('IncidenciasList')
    return render(request, 'incidencias/incidencias_create.html', context)

@login_required
def incidenciasDetail(request, pk):
    incidencias = Incidencias.objects.get(id = pk)
    context = {
        'incidencias':incidencias,
        'section': 'Incidencias',
    }
    return render(request, 'incidencias/incidencias_detail.html', context)

@login_required
def Estadisticas(request):
    # Pendientes #
    pendientes = Recursos.objects.filter(aprobacion = 'Pendiente').count()

    # Usuarios #
    usuarios = Perfil.objects.all().count()

    # Tipos Recursos #
    tipos = TipoRecurso.objects.all().count()

    # Centros de Costos #
    ubicaciones = CentroCosto.objects.all().count()

    # Recursos #
    recurso = Recursos.objects.all()
    recurso_resumen = Recursos.objects.all().count()

    # Ordenes de Servicio #
    orden = OrdenServicio.objects.all().count()
    orden_resumen = OrdenServicio.objects.values('orden','estado')
            
    # RESUMEN ESTADO #
    pre_data_estado = {}
    for i in recurso:
        try:
            if not(str(i.estado) in list(pre_data_estado.keys())):
                pre_data_estado[f'{i.estado}'] = {}
            pre_data_estado[f'{i.estado}'][f'{i.tipo}'] += 1
        except:
            pre_data_estado[f'{i.estado}'][f'{i.tipo}'] = 1

    data_estado = []
    
    for estado in pre_data_estado.keys():
        for tipo in pre_data_estado[estado].keys():
            data_estado.append((estado,tipo,pre_data_estado[estado][tipo]))
    
    # RESUMEN DEPARTAMENTO #
    pre_data_dep = {}
    for i in recurso:
        try:
            if not(str(i.centro_costo) in list(pre_data_dep.keys())):
                pre_data_dep[f'{i.centro_costo}'] = {}
                pre_data_dep[f'{i.centro_costo}'][f'{i.tipo}'] += 1
        except:
           pre_data_dep[f'{i.centro_costo}'][f'{i.tipo}'] = 1
		
    data_dep = []
	
    for centro_costo in pre_data_dep.keys():
        for tipo in pre_data_dep[centro_costo].keys():
            data_dep.append((centro_costo,tipo,pre_data_dep[centro_costo][tipo]))
    
    # CANTIDAD RECURSOS x TIPOS
    count_tipo = Recursos.objects.values('tipo').annotate(total=Count('tipo'))
    count_tipo = list(count_tipo)
    for i, j in enumerate(count_tipo):
        tipo_i = TipoRecurso.objects.get(pk = j['tipo'])
        count_tipo[i]['tipo'] = tipo_i


    # CANTIDAD TIPOS x CC
    count_cc = Recursos.objects.values('tipo', 'centro_costo').annotate(total=Count('tipo'))

    count_cc = list(count_cc)
    for i, j in enumerate(count_cc):
        tipo_i = TipoRecurso.objects.get(pk = j['tipo'])
        centro_costo_i = CentroCosto.objects.get(pk = j['centro_costo'])
        count_cc[i]['tipo'] = tipo_i
        count_cc[i]['centro_costo'] = centro_costo_i

    # CANTIDAD RECURSOS x ESTADO
    count_estado = Recursos.objects.values('estado').annotate(total=Count('estado'))
    
    # CANTIDAD RECURSOS x ESTADO
    count_estado_t = Recursos.objects.filter(estado = 'Por Definir').count()
    
    # CANTIDAD RECURSOS x SUMINISTRADO
    count_suministrador = Recursos.objects.filter(suministrador = 'Por Definir').count()

    context = {
        'section': 'Main',
        'pendientes': pendientes,
        'usuarios': usuarios,
        'tipos': tipos,
        'ubicaciones': ubicaciones,
        'recursos': recurso_resumen,
        'orden': orden,
        'data_estado': data_estado,
        'data_dep': data_dep,
        'orden_resumen': orden_resumen,
        'count_tipo': count_tipo,
        'count_cc': count_cc,
        'count_estado': count_estado,
        'count_estado_t': count_estado_t,
        'count_suministrador': count_suministrador,
    }
    
    return render(request, 'estadisticas/estadisticas.html', context)

# -----------Solicitud Baja--------------
@login_required
def dictamenTecnicoList(request):
    exp_pendientes = Recursos.objects.filter(aprobacion = 'Pendiente')
    exp_baja = exp_pendientes.filter(estado = 'Solicitud de Baja')
    context = {
        'exp_baja':exp_baja,
        'section':[
            'Aprobacion',
            'Dictamen'
        ]
    }
    return render(request, 'dictamen/dictamen_list.html', context)


@login_required
def mantenimientoList(request):
    mantenimientos = Mantenimiento.objects.all()
    context = {
        'mantenimientos':mantenimientos,
        'section':[
            'Soporte',
            'Mantenimiento',
        ]
    }
    return render(request, "mantenimiento/mantenimiento_list.html", context)

# -----------Mantenimiento---------------
@login_required
def mantenimientoCreate(request):
    if request.method == "GET":
        form = MantenimientoForm()
        context = {
            'form':form,
            'section':[
                'Soporte',
                'Mantenimiento',
            ]
        }
    else:
        form = MantenimientoForm(request.POST)
        context = {
            'form':form,
        }
        if form.is_valid():
            form.save()
            return redirect('MantenimientoList')
    return render(request, 'mantenimiento/mantenimiento_create.html', context)

@login_required
def mantenimientoList(request):
    mantenimientos = Mantenimiento.objects.all()
    context = {
        'mantenimientos':mantenimientos,
        'section':[
            'Soporte',
            'Mantenimiento',
        ]
    }
    return render(request, "mantenimiento/mantenimiento_list.html", context)
    
@login_required
def mantenimientoUpdate(request,pk):
    mantenimiento = Mantenimiento.objects.get(id = pk)
    if request.method == "GET":
        form = MantenimientoForm(instance = mantenimiento)
        context = {
            'form': form,
            'section': [
                'Soporte',
                'Mantenimiento',
            ]
        }
    else:
        form = MantenimientoForm(request.POST, instance = mantenimiento)
        context = {
            'form': form,
        }
        if form.is_valid():
            form.save()
            return redirect('MantenimientoList')
    return render(request, 'mantenimiento/mantenimiento_update.html', context)
	
@login_required
def mantenimientoDetail(request, pk):
    mantenimiento = Mantenimiento.objects.get(id = pk)
    context = {
        'mantenimiento':mantenimiento,
        'section': [
            'Soporte',
            'Mantenimiento',
        ]
    }
    return render(request, 'mantenimiento/mantenimiento_detail.html', context)

# -----------Orden de Servicio---------------
@login_required
def ordenServicioCreate(request):
    if request.method == "GET":
        form = OrdenServicioForm()
        context = {
            'form': form,
            'section': [
                'Soporte',
                'Orden',
            ]
        }
    else:
        form = OrdenServicioForm(request.POST)
        context = {
            'form': form,        
        }
        if form.is_valid():
            form.save()
            return redirect('OrdenServicioList')     
    return render (request, 'orden_servicio/orden_servicio_create.html', context)

@login_required
def ordenServicioList(request):
    ordenes = OrdenServicio.objects.all()
    context = {
        'ordenes':ordenes,
        'section':[
            'Soporte',
            'Orden',
        ]
    }
    return render(request, "orden_servicio/orden_servicio_list.html", context)
    
@login_required
def ordenServicioUpdate(request,pk):
    orden = OrdenServicio.objects.get(orden = pk)
    if request.method == "GET":
        form = OrdenServicioForm(instance = orden)
        context = {
            'form': form,
            'section': [
                'Soporte',
                'Orden',
            ]
        }
    else:
        form = OrdenServicioForm(request.POST, instance = orden)
        context = {
            'form': form,
        }
        if form.is_valid():
            form.save()
            return redirect('OrdenServicioList')
    return render(request, 'orden_servicio/orden_servicio_update.html', context)

@login_required
def estadoOrdenServicioUpdate(request,pk):
    orden = OrdenServicio.objects.get(orden = pk)
    if request.method == "GET":
        form = OrdenServicioEstadoForm(instance = orden)
        context = {
            'form': form,
            'section': [
                'Soporte',
                'Orden',
            ]
        }
    else:
        form = OrdenServicioEstadoForm(request.POST, instance = orden)
        context = {
            'form': form,
        }
        if form.is_valid():
            form.save()
            return redirect('OrdenServicioList')
    return render(request, 'orden_servicio/orden_servicio_estado.html', context)

@login_required
def ordenServicioDetail(request, pk):
    orden = OrdenServicio.objects.get(orden = pk)
    context = {
        'orden':orden,
        'section': [
            'Soporte',
            'Orden',
        ]
    }
    return render(request, 'orden_servicio/orden_servicio_detail.html', context)

class OrdenServicioDelete(DeleteView):
    model = OrdenServicio
    template_name = 'orden_servicio/orden_servicio_delete.html'
    success_url = reverse_lazy('OrdenServicioList')
    extra_context={'section': ['Soporte', 'Orden']}

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(OrdenServicioDelete, self).dispatch(request, *args, **kwargs)

# -----------Recursos---------------
@login_required
def recursosList(request):
    user = request.user
    recursos = Recursos.objects.filter(responsable=user)
    context = {
        'recursos': recursos,
        'section': 'Recursos',
    }
    return render(request, 'recursos/recursos_list.html', context)
    
class RecursoDelete(DeleteView):
    model = Recursos
    template_name = 'recursos/recursos_delete.html'
    success_url = reverse_lazy('RecursoList')
    extra_context={'section': 'Recursos'}

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(RecursoDelete, self).dispatch(request, *args, **kwargs)

@login_required
def recursoUpdate(request, id):
    recurso = Recursos.objects.get(pk=id)
    if request.method == "GET":
        form = RecursosForm(instance=recurso)
        form.initial['fecha_entrada'] = recurso.fecha_entrada.strftime('%Y-%m-%d')
        form.initial['fecha_alta'] = recurso.fecha_alta.strftime('%Y-%m-%d')
        context = {
            'form': form,
            'section': 'Recursos',
        }
    else:
        form = RecursosForm(request.POST, instance = recurso)
        context = {
            'form': form,
        }
        if form.is_valid():
            form.save()
            recurso.aprobacion = "Pendiente"
            recurso.save()
            return redirect('RecursoList')
        else:
            msg = "El código de inventario coincide con un recurso registrado con anterioridad."
            context = {
                'msg': msg,
                'form': form,
                'section': 'Recursos',
            }
    return render(request, 'recursos/recursos_update.html', context)

@login_required
def recursoCreate(request):
    if request.method == "GET":
        form = RecursosForm()
        context = {
            'form': form,
            'section': 'Recursos',
        }
    else:
        form = RecursosForm(request.POST)
        context = {
            'form': form,
        }
        if form.is_valid():
            form.save()
            return redirect('RecursoList')
        else:
            msg = "El código de inventario coincide con un recurso registrado con anterioridad."
            context = {
                'msg': msg,
                'form': form,
                'section': 'Recursos',
            }
    return render(request, 'recursos/recursos_create.html', context)


@login_required
def recursoDetail(request, pk):
    recursos = Recursos.objects.get(id = pk)
    context = {
        'recursos':recursos,
        'section': 'Recursos',
    }
    return render(request, 'recursos/recursos_detail.html', context)
	
# -----------Estado Tecnico---------------
@login_required
def estadoTecnicoList(request):
    user = request.user
    recursos = Recursos.objects.filter(responsable=user)
    context = {
        'recursos': recursos,
        'section':[
            'Recursos',
            'Estado',
        ]
    }
    return render(request, 'estado/estado_list.html', context)
    
class EstadoTecnicoUpdate(UpdateView):
    model = Recursos
    form_class = EstadoTecnicoForm
    template_name = 'estado/estado_update.html'
    success_url = reverse_lazy('EstadoTecnicoList')
    extra_context={'section': ['Recursos','Estado']}

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(EstadoTecnicoUpdate, self).dispatch(request, *args, **kwargs)

# -----------Responsable---------------
@login_required
def responsableList(request):
    user = request.user
    recursos = Recursos.objects.filter(responsable=user)
    context = {
        'recursos': recursos,
        'section':[
            'Recursos',
            'Responsable',
        ]
    }
    return render(request, 'responsable/responsable_list.html', context)
    
class ResponsableUpdate(UpdateView):
    model = Recursos
    form_class = ResponsableForm
    template_name = 'responsable/responsable_update.html'
    success_url = reverse_lazy('ResponsableList')
    extra_context={'section': ['Recursos','Responsable']}

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(ResponsableUpdate, self).dispatch(request, *args, **kwargs)

# -----------Aprobacion--------------------
@login_required
def aprobacionList(request):
    user = request.user
    recursos = Recursos.objects.filter(responsable=user)
    context = {
        'recursos': recursos,
        'section': 'Aprobacion',
    }
    return render(request, 'aprobacion/aprobacion_list.html', context)
    
class AprobacionUpdate(UpdateView):
    model = Recursos
    form_class = AprobacionForm
    template_name = 'aprobacion/aprobacion_update.html'
    success_url = reverse_lazy('ExpedientePendientes')
    extra_context={'section': 'Aprobacion'}

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(AprobacionUpdate, self).dispatch(request, *args, **kwargs)
    
# -----------Suministrador-------------------
@login_required
def suministradorList(request):
    user = request.user
    recursos = Recursos.objects.filter(responsable=user)
    context = {
        'recursos': recursos,
        'section':[
            'Recursos',
            'Suministrador',
        ]
    }
    return render(request, 'suministrador/suministrador_list.html', context)
	
class SuministradorUpdate(UpdateView):
    model = Recursos
    form_class = SuministradorForm
    template_name = 'suministrador/suministrador_update.html'
    success_url = reverse_lazy('SuministradorList')
    extra_context={'section': ['Recursos','Suministrador']}

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(SuministradorUpdate, self).dispatch(request, *args, **kwargs)

class SuministradorDelete(DeleteView):
    model = Recursos
    template_name = 'suministrador/suministrador_delete.html'
    success_url = reverse_lazy('SuministradorList')
    extra_context={'section': ['Recursos','Suministrador']}

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(SuministradorDelete, self).dispatch(request, *args, **kwargs)

# -----------Lista Aprobacion------------------------------
@login_required
def ExpedientesRevisados(request):
    exp_revisados = Recursos.objects.exclude(aprobacion = 'Pendiente')
    context = {
        'exp_revisados':exp_revisados,
        'section':[
            'Revisados', 
            'Aprobacion',
        ]
    }
    return render(request, 'aprobacion/revisados_list.html', context)

@login_required
def ExpedientePendientes(request):
    exp_pendientes = Recursos.objects.filter(aprobacion = 'Pendiente')
    exp_pendientes = exp_pendientes.exclude(estado = 'Solicitud de Baja')
    context = {
        'exp_pendientes':exp_pendientes,
        'section':[
            'Pendientes', 
            'Aprobacion',
        ]
    }
    return render(request, 'aprobacion/pendientes_list.html', context)

