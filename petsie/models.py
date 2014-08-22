from django.contrib.auth.models import AbstractUser
from django.db import models



class User(AbstractUser):
    image = models.ImageField(blank=True, null=True, upload_to="profile_images")
    phone_number = models.CharField(max_length=12, help_text="Format should be: 650-111-2222", null=True)
    address = models.TextField(null=True)
    city = models.TextField(null=True)
    # this should be max length of 2?
    state_abbr = models.CharField(max_length=24, null=True)
    zipcode = models.TextField(null=True)
    usertype = models.TextField(null=True)

    def __unicode__(self):
        return u"{}".format(self.first_name)


class Pet(models.Model):
    pet_image = models.ImageField(blank=True, null=True, upload_to="pet_images")
    # should use a related_name here, "pets" possibly
    owner = models.ForeignKey(User)
    name = models.CharField(max_length=30)
    age = models.PositiveIntegerField()
    # don't need to pass a max_length to TextField
    description = models.TextField(max_length=10000)

    def __unicode__(self):
        return u"{}".format(self.name)
