from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import (
    adminSite,
    UserDelete, 
    userCreate,
    userDetail,
    Logout, 
    PasswordChange, 
    PasswordChangeDone,
    userDetailPublico,
    perfilUpdate,
    PasswordResetView, 
    PasswordResetDone, 
    PasswordResetConfirm, 
    PasswordResetComplete,
    userUpdate,
    )
from .views import (
   tipoRecursoList,
   TipoRecursoDelete,
   tipoRecursoCreate,
   tipoRecursoDetail,
   tipoRecursoUpdate,
)
from .views import (
    centroCostoList,
    centroCostoCreate,
    centroCostoDetail,
    CentroCostoDelete,
    centroCostoUpdate,
    )
from .views import (
    AdminLogs,
    ficha_tecnica,
    login_view,
)
from .views import (
    AlmacenComponentes,
    )
from .views import (
    MotherboardDelete,
    CPUDelete,
    DiscoDelete,
    OpticaDelete,
    FuenteDelete,
    VideoDelete,
    RAMDelete,
)
from .views import (
    motherboardCreate,
    cpuCreate,
    discoCreate,
    opticaCreate,
    fuenteCreate,
    videoCreate,
    ramCreate,
)
from .views import (
    motherboardUpdate,
    cpuUpdate,
    discoUpdate,
    opticaUpdate,
    fuenteUpdate,
    videoUpdate,
    ramUpdate,
)
from .views import (
    componentesList,
    componentesCreate,
    componentesDetail,
    componentesUpdate,
    ComponentesDelete,
)
from .views import (
    incidenciasCreate,
    IncidenciasDelete,
    incidenciasDetail,
    incidenciasList,
    incidenciasUpdate,
    )
from .views import (
    tipoIncidenciaList,
    tipoIncidenciaCreate,
    tipoIncidenciaUpdate,
    tipoIncidenciaDetail,
    TipoIncidenciaDelete,
    )
from .views import (
    tipoOrdenList,
    tipoOrdenCreate,
    tipoOrdenUpdate,
    tipoOrdenDetail,
    TipoOrdenDelete,
    )
from .views import (
	Estadisticas,
	)
from .views import (
   mantenimientoCreate,
   mantenimientoList,
   mantenimientoUpdate, 
   mantenimientoDetail,
   )
from .views import (
   ordenServicioCreate, 
   ordenServicioList, 
   ordenServicioUpdate,
   ordenServicioDetail,
   OrdenServicioDelete,
   estadoOrdenServicioUpdate
   )
from .views import dictamenTecnicoList
from .views import (
   recursosList,
   recursoCreate,
   recursoUpdate,
   recursoDetail, 
   RecursoDelete, 
   )
from .views import (
   responsableList, 
   ResponsableUpdate,
   )
from .views import (
   estadoTecnicoList, 
   EstadoTecnicoUpdate,
   )
from .views import (
   ExpedientesRevisados,
   ExpedientePendientes,
   AprobacionUpdate,
)
from .views import (
   suministradorList,
   SuministradorDelete,
   SuministradorUpdate,
)
# NEW MODELS URL
from .views import (
    sedeList,
    SedeDelete,
    sedeUpdate,
    sedeCreate,
    )
from .views import (
    areaList,
    AreaDelete,
    areaUpdate,
    areaCreate,
    )
from .views import (
    departamentoList,
    DepartamentoDelete,
    departamentoUpdate,
    departamentoCreate,
    departamentoDetail,
    )
from .views import (
    centrosCostosList,
    centrosCostosCreate,
    centrosCostosDetail,
    CentrosCostosDelete,
    centrosCostosUpdate,
    )
# END NEW MODELS URL

urlpatterns = [
    # LOGIN LOGOUT #
    path('login/', login_view, name="login"),
    path('logout/', login_required(Logout.as_view()), name="logout"),
    # PASSWORD CHANGE #
    path('password_change/', login_required(PasswordChange.as_view()), name="PasswordChange"),
    path('password_change/done/', login_required(PasswordChangeDone.as_view()), name="password_change_done"),
    # PASSWORD RESET #
    path('password_reset/', PasswordResetView.as_view(), name="PasswordReset"),
    path('password_reset/done/', PasswordResetDone.as_view(), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', PasswordResetConfirm.as_view(), name="password_reset_confirm"),
    path('reset/done', PasswordResetComplete.as_view(), name="password_reset_complete"),
    # USER #
    path('adminSite/', login_required(adminSite), name="AdminSite"),
    path('UserDelete/<int:pk>/', login_required(UserDelete.as_view()), name="UserDelete"),
    path('UserCreate/', login_required(userCreate), name="UserCreate"),
    path('UserDetail/<int:pk>/', login_required(userDetail), name="UserDetail"),
    path('UserDetailPublico/<int:pk>/', login_required(userDetailPublico), name="UserDetailPublico"),
    path('PerfilUpdate/<int:pk>/', login_required(perfilUpdate), name="PerfilUpdate"),
    path('userUpdate/<int:pk>/', login_required(userUpdate), name="userUpdate"),
    # URL Tipo de Recursos #
    path('TipoRecursoList/', login_required(tipoRecursoList), name="TipoRecursoList"),
    path('TipoRecursoCreate/', login_required(tipoRecursoCreate), name="TipoRecursoCreate"),
    path('TipoRecursoDetail/<int:pk>/', login_required(tipoRecursoDetail), name="TipoRecursoDetail"),
    path('TipoRecursoUpdate/<int:pk>/', login_required(tipoRecursoUpdate), name="TipoRecursoUpdate"),
    path('TipoRecursoDelete/<int:pk>/', login_required(TipoRecursoDelete.as_view()), name="TipoRecursoDelete"),
    # URL Tipo de Incidencia #
    path('TipoIncidenciaList/', login_required(tipoIncidenciaList), name="TipoIncidenciaList"),
    path('TipoIncidenciaCreate/', login_required(tipoIncidenciaCreate), name="TipoIncidenciaCreate"),
    path('TipoIncidenciaDetail/<int:pk>/', login_required(tipoIncidenciaDetail), name="TipoIncidenciaDetail"),
    path('TipoIncidenciaUpdate/<int:pk>/', login_required(tipoIncidenciaUpdate), name="TipoIncidenciaUpdate"),
    path('TipoIncidenciaDelete/<int:pk>/', login_required(TipoIncidenciaDelete.as_view()), name="TipoIncidenciaDelete"),
    # URL Tipo de Orden #
    path('TipoOrdenList/', login_required(tipoOrdenList), name="TipoOrdenList"),
    path('TipoOrdenCreate/', login_required(tipoOrdenCreate), name="TipoOrdenCreate"),
    path('TipoOrdenDetail/<int:pk>/', login_required(tipoOrdenDetail), name="TipoOrdenDetail"),
    path('TipoOrdenUpdate/<int:pk>/', login_required(tipoOrdenUpdate), name="TipoOrdenUpdate"),
    path('TipoOrdenDelete/<int:pk>/', login_required(TipoOrdenDelete.as_view()), name="TipoOrdenDelete"),
    # URL Centros de Costos #
    path('CentroCostoList/', login_required(centroCostoList), name="CentroCostoList"),
    path('CentroCostoCreate/', login_required(centroCostoCreate), name="CentroCostoCreate"),
    path('CentroCostoDetail/<int:pk>/', login_required(centroCostoDetail), name="CentroCostoDetail"),
    path('CentroCostoUpdate/<int:pk>/', login_required(centroCostoUpdate), name="CentroCostoUpdate"),
    path('CentroCostoDelete/<int:pk>/', login_required(CentroCostoDelete.as_view()), name="CentroCostoDelete"),
    # URL Historial #
    path('AdminLog/', login_required(AdminLogs), name="AdminLogs"),
    path('FichaTecnica/<int:pk>', login_required(ficha_tecnica), name="FichaTecnica"),
    # URL Almacen #
    path('AlmacenList/', login_required(AlmacenComponentes), name="AlmacenList"),
    # URL DELETE #
    path('MotherboardDelete/<int:pk>/', login_required(MotherboardDelete.as_view()), name="MotherboardDelete"),
    path('CPUDelete/<int:pk>/', login_required(CPUDelete.as_view()), name="CPUDelete"),
    path('DiscoDelete/<int:pk>/', login_required(DiscoDelete.as_view()), name="DiscoDelete"),
    path('OpticaDelete/<int:pk>/', login_required(OpticaDelete.as_view()), name="OpticaDelete"),
    path('FuenteDelete/<int:pk>/', login_required(FuenteDelete.as_view()), name="FuenteDelete"),
    path('VideoDelete/<int:pk>/', login_required(VideoDelete.as_view()), name="VideoDelete"),
    path('RAMDelete/<int:pk>/', login_required(RAMDelete.as_view()), name="RAMDelete"),
    # URL CREATE #
    path('MotherboardCreate/', login_required(motherboardCreate), name="MotherboardCreate"),
    path('CPUCreate/', login_required(cpuCreate), name="CPUCreate"),
    path('DiscoCreate/', login_required(discoCreate), name="DiscoCreate"),
    path('OpticaCreate/', login_required(opticaCreate), name="OpticaCreate"),
    path('FuenteCreate/', login_required(fuenteCreate), name="FuenteCreate"),
    path('VideoCreate/', login_required(videoCreate), name="VideoCreate"),
    path('RAMCreate/', login_required(ramCreate), name="RAMCreate"),
    # URL UPDARE
    path('MotherboardUpdate/<int:pk>/', login_required(motherboardUpdate), name="MotherboardUpdate"),
    path('CPUUpdate/<int:pk>/', login_required(cpuUpdate), name="CPUUpdate"),
    path('DiscoUpdate/<int:pk>/', login_required(discoUpdate), name="DiscoUpdate"),
    path('OpticaUpdate/<int:pk>/', login_required(opticaUpdate), name="OpticaUpdate"),
    path('FuenteUpdate/<int:pk>/', login_required(fuenteUpdate), name="FuenteUpdate"),
    path('VideoUpdate/<int:pk>/', login_required(videoUpdate), name="VideoUpdate"),
    path('RAMUpdate/<int:pk>/', login_required(ramUpdate), name="RAMUpdate"),
    # URL Expedientes #
    path('ComponentesList/', login_required(componentesList), name="ComponentesList"),
    path('ComponentesCreate/', login_required(componentesCreate), name="ComponentesCreate"),
    path('ComponentesDetail/<int:pk>', login_required(componentesDetail), name="ComponentesDetail"),
    path('ComponentesUpdate/<int:pk>', login_required(componentesUpdate), name="ComponentesUpdate"),
    path('ComponentesDelete/<int:pk>', login_required(ComponentesDelete.as_view()), name="ComponentesDelete"),
    # URL Incidencias #
    path('IncidenciasList/', login_required(incidenciasList), name="IncidenciasList"),
    path('IncidenciasCreate/', login_required(incidenciasCreate), name="IncidenciasCreate"),
    path('IncidenciasDetail/<int:pk>/', login_required(incidenciasDetail), name="IncidenciasDetail"),
    path('IncidenciasUpdate/<int:pk>/', login_required(incidenciasUpdate), name="IncidenciasUpdate"),
    path('IncidenciasDelete/<int:pk>/', login_required(IncidenciasDelete.as_view()), name="IncidenciasDelete"),
    # URL Estadisticas #
	path('', login_required(Estadisticas), name="Estadisticas"),
    # URL Orden de Servicio #
    path('OrdenServicioCreate/', login_required(ordenServicioCreate), name="OrdenServicioCreate"),
    path('OrdenServicioList/', login_required(ordenServicioList), name="OrdenServicioList"),
    path('OrdenServicioDetail/<int:pk>/', login_required(ordenServicioDetail), name="OrdenServicioDetail"),
    path('OrdenServicioUpdate/<int:pk>/', login_required(ordenServicioUpdate), name="OrdenServicioUpdate"),
    path('OrdenServicioDelete/<int:pk>/', login_required(OrdenServicioDelete.as_view()), name="OrdenServicioDelete"),
    path('OrdenServicioEstado/<int:pk>/', login_required(estadoOrdenServicioUpdate), name="OrdenServicioEstadoUpdate"),
    # URL Mantenimiento #
    path('MantenimientoCreate/', login_required(mantenimientoCreate), name="MantenimientoCreate"),
    path('MantenimientoList/', login_required(mantenimientoList), name="MantenimientoList"),
    path('MantenimientoDetail/<int:pk>/', login_required(mantenimientoDetail), name="MantenimientoDetail"),
    path('MantenimientoUpdate/<int:pk>/', login_required(mantenimientoUpdate), name="MantenimientoUpdate"),
    # URL Dictamen #
    path('DictamenTecnicoList/', login_required(dictamenTecnicoList), name="DictamenTecnicoList"),
    # URL Recursos #
    path('RecursoList/', login_required(recursosList), name="RecursoList"),
    path('RecursoCreate/', login_required(recursoCreate), name="RecursoCreate"),
    path('RecursoDetail/<int:pk>/', login_required(recursoDetail), name="RecursoDetail"),
    path('RecursoUpdate/<int:id>/', login_required(recursoUpdate), name="RecursoUpdate"),
    path('RecursoDelete/<int:pk>/', login_required(RecursoDelete.as_view()), name="RecursoDelete"),
    # URL Responsable #
    path('ResponsableList/', login_required(responsableList), name="ResponsableList"),
    path('ResponsableUpdate/<int:pk>/', login_required(ResponsableUpdate.as_view()), name="ResponsableUpdate"),
    # URL Aprobacion #
    path('ExpedientesRevisados/', login_required(ExpedientesRevisados), name="ExpedientesRevisados"),
    path('ExpedientePendientes/', login_required(ExpedientePendientes), name="ExpedientePendientes"),
    path('AprobacionUpdate/<int:pk>/', login_required(AprobacionUpdate.as_view()), name="AprobacionUpdate"),
    # URL Estado #
    path('EstadoTecnicoList/', login_required(estadoTecnicoList), name="EstadoTecnicoList"),
    path('EstadoTecnicoUpdate/<int:pk>/', login_required(EstadoTecnicoUpdate.as_view()), name="EstadoTecnicoUpdate"),
    # URL Suministrador #
    path('SuministradorList/', login_required(suministradorList), name="SuministradorList"),
    path('SuministradorUpdate/<int:pk>/', login_required(SuministradorUpdate.as_view()), name="SuministradorUpdate"),
    path('SuministradorDelete/<int:pk>/', login_required(SuministradorDelete.as_view()), name="SuministradorDelete"),
    # URL NEW MODELS #
    # URL Sede #
    path('SedeList/', login_required(sedeList), name="SedeList"),
    path('SedeCreate/', login_required(sedeCreate), name="SedeCreate"),
    path('SedeUpdate/<int:pk>/', login_required(sedeUpdate), name="SedeUpdate"),
    path('SedeDelete/<int:pk>/', login_required(SedeDelete.as_view()), name="SedeDelete"),
    # URL Areas #
    path('AreaList/', login_required(areaList), name="AreaList"),
    path('AreaCreate/', login_required(areaCreate), name="AreaCreate"),
    path('AreaUpdate/<int:pk>/', login_required(areaUpdate), name="AreaUpdate"),
    path('AreaDelete/<int:pk>/', login_required(AreaDelete.as_view()), name="AreaDelete"),
    # URL Departamento #
    path('DepartamentoList/', login_required(departamentoList), name="DepartamentoList"),
    path('DepartamentoCreate/', login_required(departamentoCreate), name="DepartamentoCreate"),
    path('DepartamentoDetail/<int:pk>/', login_required(departamentoDetail), name="DepartamentoDetail"),
    path('DepartamentoUpdate/<int:pk>/', login_required(departamentoUpdate), name="DepartamentoUpdate"),
    path('DepartamentoDelete/<int:pk>/', login_required(DepartamentoDelete.as_view()), name="DepartamentoDelete"),
    # URL Centros de Costo #
    path('CentrosCostosList/', login_required(centrosCostosList), name="CentrosCostosList"),
    path('CentrosCostosCreate/', login_required(centrosCostosCreate), name="CentrosCostosCreate"),
    path('CentrosCostosDetail/<int:pk>/', login_required(centrosCostosDetail), name="CentrosCostosDetail"),
    path('CentrosCostosUpdate/<int:pk>/', login_required(centrosCostosUpdate), name="CentrosCostosUpdate"),
    path('CentrosCostosDelete/<int:pk>/', login_required(CentrosCostosDelete.as_view()), name="CentrosCostosDelete"),
]