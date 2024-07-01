from django.db import models
from simple_history.models import HistoricalRecords
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import pre_save
from django.dispatch import receiver
from .choices import (
	Rol,
	Sede,
    Tipo_RAM,
    Tipo_Mantenimiento, 
    Estado_Orden,
    Estado,
    Aprobacion,
    Aprobacion_Baja,
    Suministrador,
    Responsable,
    PC,
	)

# Create your models here.
class CentroCosto(models.Model):
	codigo = models.CharField(max_length=6, blank = False, unique = True)
	cede = models.CharField(max_length=17, blank = False, choices = Sede)
	facultad = models.CharField(max_length=50, blank = False) 
	departamento = models.CharField(max_length=50, blank = False)
	responsable = models.CharField(max_length=50, blank = False, null = False)
	historial = HistoricalRecords()
	
	def __str__(self):
		return self.cede + ' - ' + self.facultad + '-' + self.departamento

class TipoRecurso(models.Model):
    nombre = models.CharField(max_length=50, blank = False, null = False, unique = True)
    descripcion = models.TextField(max_length=300, blank = False, null = False)
    historial = HistoricalRecords()

    def __str__(self):
        return self.nombre

class TipoOrden(models.Model):
    nombre = models.CharField(max_length=50, blank = False, null = False, unique = True)
    descripcion = models.TextField(max_length=300, blank = False, null = False)
    historial = HistoricalRecords()

    def __str__(self):
        return self.nombre

class TipoIncidencia(models.Model):
    nombre = models.CharField(max_length=50, blank = False, null = False, unique = True)
    descripcion = models.TextField(max_length=300, blank = False, null = False)
    historial = HistoricalRecords()

    def __str__(self):
        return self.nombre

class Perfil(AbstractUser):
	ci = models.CharField(max_length=11, blank = True, null = True, unique = True)
	cargo = models.CharField(max_length=50, blank = True, null = True)
	telefono = models.CharField(max_length=8, blank = True, null = True)
	celular = models.CharField(max_length=8, blank = True, null = True)
	whatsapp = models.CharField(max_length=8, blank = True, null = True)
	rol = models.CharField(max_length = 15, blank = False, null = True, choices = Rol, default="Usuario")
	historial = HistoricalRecords()
	
	def __str__(self):
		return self.username

# NEW MODELS #
class Sede(models.Model):
    nombre = models.CharField(max_length=150, blank=False, unique = True, choices=Sede)
    responsable_soporte = models.OneToOneField(Perfil, on_delete=models.CASCADE, limit_choices_to={'rol':'Soporte Tecnico'})
    historial = HistoricalRecords()

    def __str__(self):
        return self.nombre
		
class Area(models.Model):
    nombre = models.CharField(max_length=150, blank=False, unique = True)
    jefe_area = models.OneToOneField(Perfil, on_delete=models.CASCADE, limit_choices_to={'rol':'Jefe de Area'}, related_name='jarea_a')
    supervisor_area = models.OneToOneField(Perfil, on_delete=models.CASCADE, limit_choices_to={'rol':'Supervisor'}, related_name='supervisor_a')
    responsable_area = models.OneToOneField(Perfil, on_delete=models.CASCADE, limit_choices_to={'rol':'Responsable'}, related_name='responsable_a')
    historial = HistoricalRecords()

    def __str__(self):
        return self.nombre

class Departamento(models.Model):
    nombre = models.CharField(max_length=150, blank=False, unique = True)
    sede = models.ForeignKey(Sede, on_delete=models.CASCADE)
    area = models.OneToOneField(Area, on_delete=models.CASCADE)
    jefe = models.OneToOneField(Perfil, on_delete=models.CASCADE, limit_choices_to={'rol':'Jefe de Area'}, related_name='jefe_d')
    supervisor = models.OneToOneField(Perfil, on_delete=models.CASCADE, limit_choices_to={'rol':'Supervisor'}, related_name='supervisor_d')
    responsable = models.OneToOneField(Perfil, on_delete=models.CASCADE, limit_choices_to={'rol':'Responsable'}, related_name='responsable_d')
    historial = HistoricalRecords()

    def __str__(self):
        return self.nombre

class CentrosCostos(models.Model):
    nombre = models.CharField(max_length=150, blank=False, unique = True)
    codigo = models.CharField(max_length=150, blank=False, unique = True)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    jefe = models.OneToOneField(Perfil, on_delete=models.CASCADE, limit_choices_to={'rol':'Jefe de Area'}, related_name='jefe_c')
    supervisor = models.OneToOneField(Perfil, on_delete=models.CASCADE, limit_choices_to={'rol':'Supervisor'}, related_name='supervisor_c')
    responsable = models.OneToOneField(Perfil, on_delete=models.CASCADE, limit_choices_to={'rol':'Responsable'}, related_name='responsable_c')
    historial = HistoricalRecords()
    
    def __str__(self):
        return self.codigo + '-' + self.nombre
# END NEW MODELS

# MOTHERBOARD #
class Motherboard(models.Model):
    marca = models.CharField(max_length = 50, blank = False, null = False)
    modelo = models.CharField(max_length = 50, blank = False, null = False)
    serie = models.CharField(max_length = 50, blank = False, null = False, unique = True)
    
    def __str__(self):
        return self.serie
    
    @receiver(pre_save, sender=serie)
    def check_unique(sender, instance, **kwargs):
        if instance.Componentes.exists():
            raise ValueError('Esta Motherboard ya esta asignada a otro Componente')

# CPU #
class CPU(models.Model):
    marca = models.CharField(max_length = 50, blank = False, null = False)
    nombre = models.CharField(max_length = 50, blank = False, null = False)
    serie = models.CharField(max_length = 50, blank = False, null = False, unique = True)
    
    def __str__(self):
        return self.serie
    
    @receiver(pre_save, sender=serie)
    def check_unique(sender, instance, **kwargs):
        if instance.Componentes.exists():
            raise ValueError('Esta CPU ya esta asignada a otro Componente')

# HDD #
class Disco(models.Model):
    marca = models.CharField(max_length = 50, blank = False, null = False)
    modelo = models.CharField(max_length = 50, blank = False, null = False)
    serie = models.CharField(max_length = 50, blank = False, null = False, unique = True)
    
    def __str__(self):
        return self.serie

    @receiver(pre_save, sender=serie)
    def check_unique(sender, instance, **kwargs):
        if instance.Componentes.exists():
            raise ValueError('Este Disco ya esta asignada a otro Componente')

# Optica #
class Optica(models.Model):
    marca = models.CharField(max_length = 50, blank = False, null = False)
    modelo = models.CharField(max_length = 50, blank = False, null = False)
    serie = models.CharField(max_length = 50, blank = False, null = False, unique = True)
    
    def __str__(self):
        return self.serie
    
    @receiver(pre_save, sender=serie)
    def check_unique(sender, instance, **kwargs):
        if instance.Componentes.exists():
            raise ValueError('Esta Unidad Optica ya esta asignada a otro Componente')

# Fuente #
class Fuente(models.Model):
    marca = models.CharField(max_length = 50, blank = False, null = False)
    modelo = models.CharField(max_length = 50, blank = False, null = False)
    serie = models.CharField(max_length = 50, blank = False, null = False, unique = True)
    
    def __str__(self):
        return self.serie

    @receiver(pre_save, sender=serie)
    def check_unique(sender, instance, **kwargs):
        if instance.Componentes.exists():
            raise ValueError('Esta Fuente ya esta asignada a otro Componente')

# Video #
class Video(models.Model):
    marca = models.CharField(max_length = 50, blank = False, null = False)
    modelo = models.CharField(max_length = 50, blank = False, null = False)
    serie = models.CharField(max_length = 50, blank = False, null = False, unique = True)
    
    def __str__(self):
        return self.serie
    
    @receiver(pre_save, sender=serie)
    def check_unique(sender, instance, **kwargs):
        if instance.Componentes.exists():
            raise ValueError('Esta Tarjeta de Video ya esta asignada a otro Componente')

# Memoria RAM #
class Memoria(models.Model):
    serie = models.CharField(max_length = 50, blank = False, null = False, unique = True)
    marca = models.CharField(max_length = 50, blank = False, null = False)
    capacidad = models.CharField(max_length = 5, blank = False, null = False)
    tipo = models.CharField(max_length = 50, blank = False, null = False, choices = Tipo_RAM, default='Definir')
    
    def __str__(self):
        return self.serie
    
    @receiver(pre_save, sender=serie)
    def check_unique(sender, instance, **kwargs):
        if instance.Componentes.exists():
            raise ValueError('Esta Memoria RAM ya esta asignada a otro Componente')
    
class Recursos(models.Model):
    inventario = models.CharField(max_length=50, blank = False, null = False, unique = True)
    tipo = models.ForeignKey(TipoRecurso, on_delete=models.CASCADE)
    descripcion = models.TextField(max_length=300, blank = False, null = False)
    marca = models.CharField(max_length=50, blank = False, null = False)
    modelo = models.CharField(max_length=50, blank = False, null = False)
    fecha_entrada = models.DateField(blank = False, null = False)
    fecha_alta = models.DateField(blank = False, null = False)
    valor = models.DecimalField(max_digits=7, decimal_places=2, blank = True, null = True)
    responsable = models.ForeignKey(Perfil, on_delete=models.CASCADE)
    estado = models.CharField(max_length=50, blank = False, null = False, choices = Estado, default='Seleccione...')
    aprobacion = models.CharField(max_length=50, blank = False, null = False, choices = Aprobacion, default= 'Pendiente')
    suministrador = models.CharField(max_length=50, blank = False, null = False, default='Por Definir')
    tipo_suministrador = models.CharField(max_length=50, blank = False, null = False, choices = Suministrador, default= 'Seleccione...')
    centro_costo = models.ForeignKey(CentroCosto, on_delete=models.CASCADE)
    historial = HistoricalRecords() 

    def __str__(self):
        return self.inventario

class Recursos_Baja(models.Model):
	inventario = models.ForeignKey(Recursos, on_delete=models.CASCADE)
	aprobacion_baja = models.CharField(max_length=50, blank = False, null = False, choices = Aprobacion_Baja, default= 'Pendiente')
	historial = HistoricalRecords() 

	def __str__(self):
		return self.inventario

# Componentes #
class Componentes(models.Model):
    mac = models.OneToOneField(Recursos, on_delete=models.CASCADE, limit_choices_to=PC)
    motherboard = models.OneToOneField(Motherboard, on_delete=models.CASCADE)
    cpu = models.OneToOneField(CPU, on_delete=models.CASCADE)
    ram_1 = models.OneToOneField(Memoria, on_delete=models.CASCADE, related_name='componentes_1', default='Vacio')
    ram_2 = models.OneToOneField(Memoria, on_delete=models.CASCADE, related_name='componentes_2', default='Vacio')
    ram_3 = models.OneToOneField(Memoria, on_delete=models.CASCADE, related_name='componentes_3', default='Vacio')
    ram_4 = models.OneToOneField(Memoria, on_delete=models.CASCADE, related_name='componentes_4', default='Vacio')
    disco = models.OneToOneField(Disco, on_delete=models.CASCADE)
    optica = models.OneToOneField(Optica, on_delete=models.CASCADE)
    fuente = models.OneToOneField(Fuente, on_delete=models.CASCADE)
    video = models.OneToOneField(Video, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.mac

class Incidencias(models.Model):
    fecha = models.DateField(blank = False, null = False, auto_now = True)
    tipo =  models.ForeignKey(TipoIncidencia, on_delete=models.CASCADE)
    inventario = models.ForeignKey(Recursos, on_delete=models.CASCADE)
    nombre = models.CharField(max_length = 50, null = False, blank = False)
    descripcion = models.TextField(max_length=300, blank = False, null = False)
    historial = HistoricalRecords()
	
    def __str__(self):
    	return f"{self.nombre}"

class OrdenServicio(models.Model):
    inventario = models.ForeignKey(Recursos, on_delete=models.CASCADE)
    orden = models.BigAutoField(primary_key = True)
    estado = models.CharField(max_length=50, blank = False, null = False, choices = Estado_Orden, default='Nueva')
    tipo_orden = models.ForeignKey(TipoOrden, on_delete=models.CASCADE)
    descripcion = models.TextField(max_length=300, blank = False, null = False)
    fecha = models.DateField(auto_now=True)
    historial = HistoricalRecords()

    def __str__(self):
        return "TK-" + f"{self.orden}"

class DictamenTecnico(models.Model):
    pass

class Mantenimiento(models.Model):
    inventario = models.ForeignKey(Recursos, on_delete=models.CASCADE)
    orden = models.ForeignKey(OrdenServicio, on_delete=models.CASCADE)
    fecha = models.DateField(auto_now=True)
    responsable = models.CharField(max_length=100, blank = False, null = False)
    sello_quitado = models.CharField(max_length=10, blank = False, null = False)
    sello_puesto = models.CharField(max_length=10, blank = False, null = False)
    participantes = models.TextField(max_length=500, blank = False, null = False)
    datos_pieza = models.TextField(max_length=500, blank = False, null = False)
    tipo_mantenimiento = models.CharField(max_length=50, blank = False, null = False, choices = Tipo_Mantenimiento, default='Definir')
    descripcion = models.TextField(max_length=300, blank = False, null = False)
    historial = HistoricalRecords()
    
    def __str__(self):
        return f"{self.orden}"
