from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=30, null=False)
    workplace = models.CharField(max_length=90, null=True)
