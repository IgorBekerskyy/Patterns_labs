from django.db import models


class Caretaker(models.Model):
    name = models.CharField(max_length=20, null=False)



