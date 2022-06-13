from django.db import models


class Compensation(models.Model):
    name = models.CharField(max_length=100, null=False)
    status = models.CharField(max_length=2000, null=False)
    background = models.CharField(max_length=80, null=True)

    def set_status(self, status):
        self.status = status
        return True
