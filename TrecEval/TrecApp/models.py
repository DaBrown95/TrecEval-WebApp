from django.db import models


class Run(models.Model):
    runfile = models.FileField(upload_to = "runFiles")

