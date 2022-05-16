from django.db import models
from django.conf import settings


class BaseModel(models.Model):
    # se hace de sta forma si el modelo por defecto de su uario personalizado
    user_create = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_create', blank=True, null=True)
    user_update = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_update', blank=True, null=True)
    data_create = models.DateTimeField(
        auto_now_add=True, blank=True, null=True)
    date_update = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        abstract = True
