from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from django.contrib.admin.models import LogEntry
from .models import (
	CentroCosto,
 	# NEW MODELS #
	CentrosCostos,
	Departamento,
	Area,
	Sede,
	# END NEW MODELS #
	TipoRecurso,
	Perfil,
    Motherboard,
    CPU,
    Memoria,
    Disco,
    Optica,
    Fuente,
    Video,
    Componentes,
    Incidencias,
    OrdenServicio,
    Mantenimiento,
    Recursos,
    TipoOrden,
    TipoIncidencia,
	)

# Register your models here.
admin.site.register(LogEntry)

# NEW MODELS #
admin.site.register(CentrosCostos)
admin.site.register(Departamento)
admin.site.register(Area)
admin.site.register(Sede)
# END NEW MODELS #

@admin.register(CentroCosto)
class CentroCostoAdmin(ImportExportModelAdmin):
	list_display = (
		"codigo",
		"cede",
		"facultad",
		"departamento",
		"responsable",
		)

@admin.register(TipoRecurso)
class TipoRecursoAdmin(ImportExportModelAdmin):
	list_display = (
		"nombre",
		"descripcion",
		)

@admin.register(TipoOrden)
class TipoOrdenAdmin(ImportExportModelAdmin):
	list_display = (
		"nombre",
		"descripcion",
		)

@admin.register(TipoIncidencia)
class TipoIncidenciaAdmin(ImportExportModelAdmin):
	list_display = (
		"nombre",
		"descripcion",
		)

@admin.register(Perfil)
class PerfilAdmin(ImportExportModelAdmin):
	list_display = (
		"id",
		"username",
		"cargo",
		"telefono",
		"celular",
		"whatsapp",
		"rol",
		)

@admin.register(Motherboard)
class MotherboardAdmin(ImportExportModelAdmin):
	list_display = (
		"marca",
		"modelo",
		"serie",
		)

@admin.register(CPU)
class CPUAdmin(ImportExportModelAdmin):
	list_display = (
		"marca",
		"nombre",
		"serie",
		)

@admin.register(Memoria)
class MemoriaAdmin(ImportExportModelAdmin):
	list_display = (
		"serie",
		"marca",
		"capacidad",
		"tipo",
		)

@admin.register(Disco)
class DiscoAdmin(ImportExportModelAdmin):
	list_display = (
		"marca",
		"modelo",
		"serie",
		)

@admin.register(Optica)
class OpticaAdmin(ImportExportModelAdmin):
	list_display = (
		"marca",
		"modelo",
		"serie",
		)

@admin.register(Fuente)
class FuenteAdmin(ImportExportModelAdmin):
	list_display = (
		"marca",
		"modelo",
		"serie",
		)

@admin.register(Video)
class VideoAdmin(ImportExportModelAdmin):
	list_display = (
		"marca",
		"modelo",
		"serie",
		)

@admin.register(Componentes)
class ComponentesAdmin(ImportExportModelAdmin):
	list_display = (
		"mac",
		"motherboard",
		"cpu",
		"ram_1",
		"ram_2",
        "ram_3",
        "ram_4",
        "disco",
        "optica",
        "fuente",
        "video",
		)

@admin.register(Incidencias)
class IncidenciasAdmin(ImportExportModelAdmin):
	list_display = (
        "fecha",
	    "tipo",
        "inventario",
        "nombre",
        "descripcion",
        )

@admin.register(OrdenServicio)
class Orden_ServicioAdmin(ImportExportModelAdmin):
	list_display = (
		"inventario",
		"orden",
		"estado",
		"tipo_orden",
		"descripcion",
		)

@admin.register(Mantenimiento)
class MantenimientoAdmin(ImportExportModelAdmin):
	list_display = (
		"inventario",
		"orden",
		"fecha",
		"responsable",
		"sello_quitado",
		"sello_puesto",
		"participantes",
		"datos_pieza",
		"tipo_mantenimiento",
		"descripcion",
		)

@admin.register(Recursos)
class RecursosAdmin(ImportExportModelAdmin):
	list_display = (
		"inventario",
		"tipo",
		"descripcion",
		"marca",
		"modelo",
		"fecha_entrada",
		"fecha_alta",
		"valor",
		"responsable",
		"estado",
		"centro_costo",
		)