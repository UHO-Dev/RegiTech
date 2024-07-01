from django.contrib.auth.forms import forms
from django.contrib.auth.forms import (
    UserCreationForm, 
    PasswordChangeForm,
    )
from .models import (
    TipoRecurso, 
    CentroCosto,
    Perfil,
    Motherboard,
    CPU,
    Disco,
    Optica,
    Fuente,
    Video,
    Memoria,
    Componentes,
    Incidencias,
    OrdenServicio,
    Mantenimiento,    
    Recursos,
    TipoIncidencia,
    TipoOrden,
    # New Models
    Sede,
    Area,
    Departamento,
    CentrosCostos,
    # END NEW MODELS
    )


class LoginForm(forms.Form):
    username = forms.CharField(
        widget = forms.TextInput(
            attrs = {
                "class":"form-control"
            }
        )
    )
    password = forms.CharField(
        widget = forms.PasswordInput(
            attrs = {
                "class":"form-control"
            }
        )
    )


class UserCreationForm(UserCreationForm):
    
    class Meta:
        model = Perfil
        fields = [
            'username',
            'email',
            'rol',
            'password1',
            'password2',
        ]
        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control','id':'username','placeholder':'Ingrese su nombre de Usuario'}),
            'rol': forms.Select(attrs={'class':'form-control','id':'rol'}),
            'email': forms.TextInput(attrs={'class':'form-control','id':'email','type':'email','placeholder':'Ingrese su correo coorporativo'})
        }
        

class UserEditForm(UserCreationForm):
    
    class Meta:
        model = Perfil
        fields = [
            'username',
            'email',
            'rol',
        ]
        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control','id':'username','placeholder':'Ingrese su nombre de Usuario'}),
            'email': forms.TextInput(attrs={'class':'form-control','id':'email','type':'email','placeholder':'Ingrese su correo coorporativo'}),
            'rol': forms.Select(attrs={'class':'form-control','id':'rol'}),
        }
        

class PerfilForm(forms.ModelForm):

    class Meta:
        model = Perfil
        fields = [
            'first_name',
            'last_name',
            'ci',
            'cargo',
            'telefono',
            'celular',
            'whatsapp',
        ]
        widgets = {
            'first_name': forms.TextInput(attrs={'class':'form-control','id':'nombre','placeholder':'Ingrese su nombre'}),
            'last_name': forms.TextInput(attrs={'class':'form-control','id':'apellido','placeholder':'Ingrese sus apellidos'}),
            'ci': forms.NumberInput(attrs={'class':'form-control','id':'ci','placeholder':'Ingrese su carnet de identidad'}),
            'cargo': forms.TextInput(attrs={'class':'form-control','id':'cargo','placeholder':'Ingrese su cargo'}),
            'telefono': forms.TextInput(attrs={'class':'form-control','id':'telefono','type':'number','placeholder':'Ingrese el teléfono de su area'}),
            'celular': forms.NumberInput(attrs={'class':'form-control','id':'celular','placeholder':'Ingrese su número de teléfono'}),
            'whatsapp': forms.NumberInput(attrs={'class':'form-control','id':'whatsapp','placeholder':'Ingrese su número de whatsapp'}),
        }
      
class PassChangeForm(PasswordChangeForm):
    
    class Meta:
        model = Perfil
        fields = [
            'old_password',
            'new_password1',
            'new_password2',
        ]
        
class TipoRecursoForm(forms.ModelForm):
    
    class Meta:
        model = TipoRecurso
        fields = {
            'nombre',
            'descripcion',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control','id':'nombre','placeholder':'Introduzca el Nombre del Recurso'}),
            'descripcion': forms.Textarea(attrs={'class':'form-control','id':'descripcion','placeholder':'Introduzca una breve descripción del tipo de recurso a registrar'}),
        }

class TipoIncidenciaForm(forms.ModelForm):
    
    class Meta:
        model = TipoIncidencia
        fields = {
            'nombre',
            'descripcion',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control','id':'nombre','placeholder':'Introduzca el Nombre de la Incidencia'}),
            'descripcion': forms.Textarea(attrs={'class':'form-control','id':'descripcion','placeholder':'Introduzca una breve descripción del tipo de Incidencia a registrar'}),
        }

class TipoOrdenForm(forms.ModelForm):
    
    class Meta:
        model = TipoOrden
        fields = {
            'nombre',
            'descripcion',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control','id':'nombre','placeholder':'Introduzca el Nombre de la Orden'}),
            'descripcion': forms.Textarea(attrs={'class':'form-control','id':'descripcion','placeholder':'Introduzca una breve descripción del tipo de Orden de Servicio a registrar'}),
        }

class UbicacionForm(forms.ModelForm):
    
    class Meta:
        model = CentroCosto
        fields = {
            'codigo',
            'cede',
            'facultad',
            'departamento',
            'responsable',
        }
        widgets = {
            'codigo': forms.TextInput(attrs={'class':'form-control','id':'codigo','placeholder':'Introduzca el codigo del Centro de Costo'}),
            'cede': forms.Select(attrs={'class':'form-control','id':'cede','placeholder':'Seleccione la cede de la Universidad de Holguín'}),
            'facultad': forms.TextInput(attrs={'class':'form-control','id':'facultad','placeholder':'Introduzca el nombre de la facultad'}),
            'departamento': forms.TextInput(attrs={'class':'form-control','id':'departamento','placeholder':'Introduzca el nombre del departamento'}),
            'responsable': forms.TextInput(attrs={'class':'form-control','id':'responsable','placeholder':'Introduzca el responsable del departamento'}),
        }

# NEW FORMS MODELS #
class SedeForm(forms.ModelForm):

    class Meta:
        model = Sede
        fields = {
            'nombre',
            'responsable_soporte',
        }
        widgets = {
            'nombre': forms.Select(attrs={'class':'form-control','id':'nombre','placeholder':'Introduzca el codigo del Centro de Costo'}),
            'responsable_soporte': forms.Select(attrs={'class':'form-control','id':'responsable_soporte','placeholder':'Introduzca el codigo del Centro de Costo'}),
        }

class AreaForm(forms.ModelForm):

    class Meta:
        model = Area
        fields = {
            'nombre',
            'jefe_area',
            'supervisor_area',
            'responsable_area',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control','id':'nombre','placeholder':'Introduzca el codigo del Centro de Costo'}),
            'jefe_area': forms.Select(attrs={'class':'form-control','id':'jefe_area','placeholder':'Introduzca el codigo del Centro de Costo'}),
            'supervisor_area': forms.Select(attrs={'class':'form-control','id':'supervisor_area','placeholder':'Introduzca el codigo del Centro de Costo'}),
            'responsable_area': forms.Select(attrs={'class':'form-control','id':'responsable_area','placeholder':'Introduzca el codigo del Centro de Costo'}),
        }

class DepartamentoForm(forms.ModelForm):

    class Meta:
        model = Departamento
        fields = {
            'nombre',
            'sede',
            'area',
            'jefe',
            'supervisor',
            'responsable',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control','id':'nombre','placeholder':'Introduzca el codigo del Centro de Costo'}),
            'sede': forms.Select(attrs={'class':'form-control','id':'sede','placeholder':'Introduzca el codigo del Centro de Costo'}),
            'area': forms.Select(attrs={'class':'form-control','id':'area','placeholder':'Introduzca el codigo del Centro de Costo'}),
            'jefe': forms.Select(attrs={'class':'form-control','id':'jefe','placeholder':'Introduzca el codigo del Centro de Costo'}),
            'supervisor': forms.Select(attrs={'class':'form-control','supervisor':'nombre','placeholder':'Introduzca el codigo del Centro de Costo'}),
            'responsable': forms.Select(attrs={'class':'form-control','id':'responsable','placeholder':'Introduzca el codigo del Centro de Costo'}),
        }

class CentrosCostosForm(forms.ModelForm):

    class Meta:
        model = CentrosCostos
        fields = {
            'nombre',
            'codigo',
            'departamento',
            'jefe',
            'supervisor',
            'responsable',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control','id':'nombre','placeholder':'Introduzca el codigo del Centro de Costo'}),
            'codigo': forms.TextInput(attrs={'class':'form-control','id':'codigo','placeholder':'Introduzca el codigo del Centro de Costo'}),
            'departamento': forms.Select(attrs={'class':'form-control','id':'departamento','placeholder':'Introduzca el codigo del Centro de Costo'}),
            'jefe': forms.Select(attrs={'class':'form-control','id':'jefe','placeholder':'Introduzca el codigo del Centro de Costo'}),
            'supervisor': forms.Select(attrs={'class':'form-control','id':'supervisor','placeholder':'Introduzca el codigo del Centro de Costo'}),
            'responsable': forms.Select(attrs={'class':'form-control','id':'responsable','placeholder':'Introduzca el codigo del Centro de Costo'}),
        }
# END NEW FORMS MODELS #

class MotherboardForm(forms.ModelForm):
    
    class Meta:
        model = Motherboard
        fields = {
			'marca',
            'modelo',
            'serie',
		}
        widgets = {
            'marca': forms.TextInput(attrs={'class':'form-control','id':'marca','placeholder':'Introduzca la marca de la placa'}),
            'modelo': forms.TextInput(attrs={'class':'form-control','id':'modelo','placeholder':'Introduzca el modelo de la placa'}),
            'serie': forms.TextInput(attrs={'class':'form-control','id':'serie','placeholder':'Introduzca el número de serie de la placa'}),
        }
        
        
class CPUForm(forms.ModelForm):
    
    class Meta:
        model = CPU
        fields = {
			'marca',
            'nombre',
            'serie',
		}
        widgets = {
            'marca': forms.TextInput(attrs={'class':'form-control','id':'marca','placeholder':'Introduzca la marca de la CPU'}),
            'nombre': forms.TextInput(attrs={'class':'form-control','id':'nombre','placeholder':'Introduzca el nómbre de la CPU'}),
            'serie': forms.TextInput(attrs={'class':'form-control','id':'serie','placeholder':'Introduzca el número de serie de la CPU'}),
        }


class DiscoForm(forms.ModelForm):
    
    class Meta:
        model = Disco
        fields = {
			'marca',
            'modelo',
            'serie',
		}
        widgets = {
            'marca': forms.TextInput(attrs={'class':'form-control','id':'marca','placeholder':'Introduzca la marca del disco'}),
            'modelo': forms.TextInput(attrs={'class':'form-control','id':'modelo','placeholder':'Introduzca el modelo del disco'}),
            'serie': forms.TextInput(attrs={'class':'form-control','id':'serie','placeholder':'Introduzca el número de serie del disco'}),
        }
      
        
class OpticaForm(forms.ModelForm):
    
    class Meta:
        model = Optica
        fields = {
			'marca',
            'modelo',
            'serie',
		}
        widgets = {
            'marca': forms.TextInput(attrs={'class':'form-control','id':'marca','placeholder':'Introduzca la marca de la Unidad Óptica'}),
            'modelo': forms.TextInput(attrs={'class':'form-control','id':'modelo','placeholder':'Introduzca el modelo de la Unidad Óptica'}),
            'serie': forms.TextInput(attrs={'class':'form-control','id':'serie','placeholder':'Introduzca el número de serie de la Unidad Óptica'}),
        }

  
class FuenteForm(forms.ModelForm):
    
    class Meta:
        model = Fuente
        fields = {
			'marca',
            'modelo',
            'serie',
		}
        widgets = {
            'marca': forms.TextInput(attrs={'class':'form-control','id':'marca','placeholder':'Introduzca la marca de la Fuente'}),
            'modelo': forms.TextInput(attrs={'class':'form-control','id':'modelo','placeholder':'Introduzca el modelo de la Fuente'}),
            'serie': forms.TextInput(attrs={'class':'form-control','id':'serie','placeholder':'Introduzca el número de serie de la Fuente'}),
        }


class VideoForm(forms.ModelForm):
    
    class Meta:
        model = Video
        fields = {
			'marca',
            'modelo',
            'serie',
		}
        widgets = {
            'marca': forms.TextInput(attrs={'class':'form-control','id':'marca','placeholder':'Introduzca la marca de la Tarjeta de Video'}),
            'modelo': forms.TextInput(attrs={'class':'form-control','id':'modelo','placeholder':'Introduzca el modelo de la Tarjeta de Video'}),
            'serie': forms.TextInput(attrs={'class':'form-control','id':'serie','placeholder':'Introduzca el número de serie de la Tarjeta de Video'}),
        }
        

class MemoriaForm(forms.ModelForm):
    
    class Meta:
        model = Memoria
        fields = {
			'serie',
            'marca',
            'capacidad',
            'tipo',
		}
        widgets = {
            'serie': forms.TextInput(attrs={'class':'form-control','id':'serie','placeholder':'Introduzca el número de serie de la Memoria RAM'}),
            'marca': forms.TextInput(attrs={'class':'form-control','id':'marca','placeholder':'Introduzca la marca de la Memoria RAM'}),
            'capacidad': forms.NumberInput(attrs={'class':'form-control','id':'capacidad_ram','placeholder':'Introduzca la capacidad(Mb) de la Memoria RAM'}),
            'tipo': forms.Select(attrs={'class':'form-control','id':'tipo','placeholder':'Introduzca el tipo de Memoria RAM'}),
        }
        
        
class ComponentesForm(forms.ModelForm):
    
    class Meta:
        model = Componentes
        fields = {
			'mac',
            'motherboard',
            'cpu',
            'ram_1',
            'ram_2',
            'ram_3',
            'ram_4',
            'disco',
            'optica',
            'fuente',
            'video',
		}
        widgets = {
            'mac': forms.Select(attrs={'class':'form-control','id':'mac','placeholder':'Introduzca el código del MAC'}),
            'motherboard': forms.Select(attrs={'class':'form-control','id':'motherboard','placeholder':'Seleccione la Motherboard'}),
            'cpu': forms.Select(attrs={'class':'form-control','id':'cpu','placeholder':'Seleccione la CPU'}),
            'ram_1': forms.Select(attrs={'class':'form-control','id':'ram_1','placeholder':'Seleccione la Memoria RAM 1'}),
            'ram_2': forms.Select(attrs={'class':'form-control','id':'ram_2','placeholder':'Seleccione la Memoria RAM 2'}),
            'ram_3': forms.Select(attrs={'class':'form-control','id':'ram_3','placeholder':'Seleccione la Memoria RAM 3'}),
            'ram_4': forms.Select(attrs={'class':'form-control','id':'ram_4','placeholder':'Seleccione la Memoria RAM 4'}),
            'disco': forms.Select(attrs={'class':'form-control','id':'disco','placeholder':'Seleccione el Disco'}),
            'optica': forms.Select(attrs={'class':'form-control','id':'optica','placeholder':'Seleccione la Unidad Óptica'}),
            'fuente': forms.Select(attrs={'class':'form-control','id':'fuente','placeholder':'Seleccione la Fuente'}),
            'video': forms.Select(attrs={'class':'form-control','id':'video','placeholder':'Seleccione la Tarjeta de Video'}),
        }
        

class IncidenciasForm(forms.ModelForm):
    
    class Meta:
        model = Incidencias
        fields = {
			'inventario',
            'tipo',
            'descripcion',
            'nombre',
		}
        widgets = {
            'inventario': forms.Select(attrs={'class':'form-control','id':'inventario'}),
            'tipo': forms.Select(attrs={'class':'form-control','id':'tipo'}),
            'descripcion': forms.Textarea(attrs={'class':'form-control','id':'descripcion','placeholder':'Introduzca una breve descripción del recurso'}),
            'nombre': forms.TextInput(attrs={'class':'form-control','id':'inventario','placeholder':'Introduzca su nómbre'}),
        }
        

class OrdenServicioForm(forms.ModelForm):
    
    class Meta:
        model = OrdenServicio
        fields = {
            'inventario',
            'tipo_orden',
            'descripcion',
        }
        widgets = {
            'inventario': forms.Select(attrs={'class':'form-control','id':'inventario'}),
            'tipo_orden': forms.Select(attrs={'class':'form-control','id':'tipo_orden'}),
            'descripcion': forms.Textarea(attrs={'class':'form-control','id':'descripcion','placeholder':'Introduzca una breve descripción de su problema'}),
        }

class OrdenServicioEstadoForm(forms.ModelForm):
    
    class Meta:
        model = OrdenServicio
        fields = {
            'estado',
        }
        widgets = {
            'estado': forms.Select(attrs={'class':'form-control col-sm-8','id':'estado'}),
        }


class MantenimientoForm(forms.ModelForm):
    
    class Meta:
        model = Mantenimiento
        fields = {
            'inventario',
            'orden',
            'responsable',
            'sello_quitado',
            'sello_puesto',
            'participantes',
            'datos_pieza',
            'tipo_mantenimiento',
            'descripcion'
        }
        widgets = {
            'inventario': forms.Select(attrs={'class':'form-control','id':'inventario'}),
            'orden': forms.Select(attrs={'class':'form-control','id':'orden'}),
            'responsable': forms.TextInput(attrs={'class':'form-control','id':'responsable','placeholder':'Introduzca el responsable'}),
            'sello_quitado': forms.TextInput(attrs={'class':'form-control','id':'sello_quitado','placeholder':'Introduzca el código del sello quitado'}),
            'sello_puesto': forms.TextInput(attrs={'class':'form-control','id':'sello_puesto','placeholder':'Introduzca el código del sello puesto'}),
            'participantes': forms.Textarea(attrs={'class':'form-control','id':'participantes','placeholder':'Introduzca los participantes del mantenimiento'}),
            'datos_pieza': forms.Textarea(attrs={'class':'form-control','id':'datos_pieza','placeholder':'Introduzca los datos de la pieza reemplazada'}),
            'tipo_mantenimiento': forms.Select(attrs={'class':'form-control','id':'tipo_mantenimiento'}),
            'descripcion': forms.Textarea(attrs={'class':'form-control','id':'descripcion','placeholder':'Introduzca una descripción del mantenimiento realizado'}),
        }


class RecursosForm(forms.ModelForm):
    
    class Meta:
        model = Recursos
        fields = {
			'inventario',
            'tipo',
            'marca',
            'modelo',
            'descripcion',
            'responsable',
            'estado',
            'fecha_entrada',
            'fecha_alta',
            'valor',
            'centro_costo'
		}
        widgets = {
            'inventario': forms.TextInput(attrs={'class':'form-control','id':'inventario','placeholder':'Introduzca el código de inventario'}),
            'tipo': forms.Select(attrs={'class':'form-control','id':'tipo'}),
            'marca': forms.TextInput(attrs={'class':'form-control','id':'marca','placeholder':'Introduzca la marca del recurso'}),
            'modelo': forms.TextInput(attrs={'class':'form-control','id':'modelo','placeholder':'Introduzca el modelo del recurso'}),
            'responsable': forms.Select(attrs={'class':'form-control','id':'responsable'}),
            'estado': forms.Select(attrs={'class':'form-control','id':'estado'}),
            'descripcion': forms.Textarea(attrs={'class':'form-control','id':'descripcion','placeholder':'Introduzca una breve descripción del recurso'}),
            'fecha_entrada': forms.DateInput(attrs={'class':'form-control','id':'fecha_entrada', 'type':'date'}),
            'fecha_alta': forms.DateInput(attrs={'class':'form-control','id':'fecha_alta', 'type':'date'}),
            'valor': forms.NumberInput(attrs={'class':'form-control','id':'valor','placeholder':'Introduzca el valor del recurso'}),
            'centro_costo': forms.Select(attrs={'class':'form-control','id':'centro_costo'}),
        }
        

class EstadoTecnicoForm(forms.ModelForm):
    
    class Meta:
        model = Recursos
        fields = {
			'estado',
		}
        widgets = {
            'estado': forms.Select(attrs={'class':'form-control','id':'estado'}),
        }
        

class CentroCostoForm(forms.ModelForm):
    
    class Meta:
        model = Recursos
        fields = {
            'centro_costo',
        }
        widgets = {
            'centro_costo': forms.Select(attrs={'class':'form-control','id':'centro_costo'}),
        }


class ResponsableForm(forms.ModelForm):
    
    class Meta:
        model = Recursos
        fields = {
			'responsable',
		}
        widgets = {
            'responsable': forms.Select(attrs={'class':'form-control','id':'responsable'}),
        }
        
        
class AprobacionForm(forms.ModelForm):
    
    class Meta:
        model = Recursos
        fields = {
			'aprobacion',
		}
        widgets = {
            'aprobacion': forms.RadioSelect(attrs={'class':'text-dark', 'id':'aprobacion'}),
        }
        

class SuministradorForm(forms.ModelForm):
    
    class Meta:
        model = Recursos
        fields = {
            'suministrador',
            'tipo_suministrador', 
        }
        widgets = {
            'suministrador': forms.TextInput(attrs={'class':'form-control','id':'suministrador','placeholder':'Introduzca el Nombre de la Entidad que suministra el Recurso'}),
            'tipo_suministrador': forms.Select(attrs={'class':'form-control','id':'tipo_suministrador'}),
        }
        