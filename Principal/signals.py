from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Recursos

@receiver(post_save, sender=Recursos)
def recurso_edit(sender, instance, updated = True, **kwargs):
	if updated:
		instance.aprobacion = "Pendiente"
		instance.save()
