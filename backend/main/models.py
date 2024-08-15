from django.db import models


class SliderImage(models.Model):
    images = models.ImageField(upload_to="images/")
