from django.db import models

# Create your models here.
class PictureUpload(models.Model):
  img = models.ImageField(upload_to = "p")