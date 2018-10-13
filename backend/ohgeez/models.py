from django.db import models
from django.core.validators import RegexValidator
from django.utils.translation import ugettext_lazy as _
from datetime import datetime


class Category(models.Model):
    # Fields
    name = models.CharField(_("Category Name"), max_length=30)

    def __str__(self):
        return "%s" % (self.name)

class Item(models.Model):

    # Fields
    # name of new location
    name = models.CharField(_("Name"), max_length=128)

    # Address fields
    address = models.CharField(_("Address"), max_length=128)
    city = models.CharField(_("City"), max_length=30)
    state = models.CharField(_("State"), max_length=2)
    zip_code = models.CharField(_("Zip Code"), max_length=5)

    #Location Fields
    longitude = models.FloatField(editable=False, default=0.0)
    latitude = models.FloatField(editable=False, default=0.0)

    #Phone fields
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)

    # Description
    description = models.TextField()

    # Category
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    # bookkeeping
    created_at = models.DateTimeField(editable=False, auto_now_add=True)
    updated_at = models.DateTimeField(editable=False, auto_now=True)

    # def __addGps():
    #     geolocator = Nominatim(user_agent="ohgeez")
    #     location = geolocator.geocode("%s %s, %s %s" % (self.address, self.city, self.state, self.zip_code))
    #     self.longitude = location.longitude
    #     self.latitude = location.latitude
    #
    # def save(self):
    #     if not self.id:
    #         self.__addGps()
    #     super(Item, self).save()

    def __str__(self):
        return "%s" % (self.name)
