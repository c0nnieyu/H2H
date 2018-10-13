from django.db import models
from django.contrib.localflavor.us.models import USStateField
from django.core.validators import RegexValidator

from geopy.geocoders import Nominatim

class Geez(models.Model):

    # Fields
    # name of new location
    name = models.TextField()

    # Address fields
    address = models.CharField(_("Address"), max_length=128))
    city = models.CharField(_("Address 2"), max_length=128, blank=True)
    state = models.USStateField()
    zip_code = models.CharField(_("Zip Code"), max_length=5)

    #Location Fields
    longitude = models.FloatField(editable=False)
    latitude = models.FloatField(editable=False)

    #Phone fields
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)

    # Description
    description = models.TextField()

    # Category
    category = models.ForeignKey(Category)

    # bookkeeping
    created = models.DateField(editable=False)
    updated = models.DateTimeField(editable=False)

    def addGps(self):
        geolocator = Nominatim(user_agent="ohgeez")
        location = geolocator.geocode("%s %s, %s %s" % (self.address, self.city, self.state, self.zip_code))
        self.longitude = location.longitude
        self.latitude = location.latitude

    def save(self):
        if not self.id:
            self.created = datetime.date.today()
            addGps(self)
        self.updated = datetime.datetime.today()
        super(Geez, self).save()

    def __str__(self):
        return "%s" % (self.name)


class Category(models.Model):
    # Fields
    name = models.CharField(_("Category Name"), max_length=30)

    def __str__(self):
        return "%s" % (self.name)
