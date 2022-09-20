from django.db import models


class Master(models.Model):
    user = models.ForeignKey('accounts.User', on_delete=models.SET_NULL, null=True, blank=True, default=None)


class Klass(models.Model):
    master = models.ForeignKey('contentshub.Master', on_delete=models.SET_NULL, null=True, blank=True, default=None)
    title = models.CharField(max_length=50)
