from django.db import models
from django.contrib.localflavor.us.models import USStateField
from django.core.validators import RegexValidator

class Geez(models.Model):

    # Fields
    # name of new location
    name = models.TextField()

    # Address fields
    address = models.CharField(_("Address"), max_length=128))
    city = models.CharField(_("Address 2"), max_length=128, blank=True)
    state = models.USStateField()
    zip_code = models.CharField(_("Zip Code"), max_length=5)

    #Phone fields
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)

    # Description
    description = models.TextField()

    # Category
    category = models.ForeignKey(Category)

    def __str__(self):
        return "%s" % (self.name)

class Category(models.Model):
    # Fields
    name = models.CharField(_("Category Name"), max_length=30)

    def __str__(self):
        return "%s" % (self.name)
