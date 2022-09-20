from django.db import models


class Question(models.Model):
    user = models.ForeignKey('accounts.User', on_delete=models.SET_NULL, null=True, blank=True, default=None)
    klass = models.ForeignKey('contentshub.Klass', on_delete=models.SET_NULL, null=True, blank=True, default=None)
    contents = models.TextField()


class Answer(models.Model):
    question = models.ForeignKey('community.Question', on_delete=models.SET_NULL, null=True, blank=True, default=None)
    contents = models.TextField()
