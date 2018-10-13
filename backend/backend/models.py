from django.db import models

class Geez(models.Model):

    # Fields
    # name of new location
    name = models.TextField()
    street = models.TextField()
    city = models.TextField()
    state = models.TextField()
