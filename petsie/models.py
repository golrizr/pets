from django.contrib.auth.models import AbstractUser
from django.db import models



class User(AbstractUser):
    # image = models.ImageField(blank=True, null=True)
    phone_number = models.CharField(max_length=12, help_text="Format should be: 650-111-2222", null=True)
    address = models.TextField(null=True)
    city = models.TextField(null=True)
    state_abbr = models.CharField(max_length=24, null=True)
    zipcode = models.TextField(null=True)
    # You should look into Django's built-in ChoiceField, which would be a better option for usertype than a TextField
    usertype = models.TextField(null=True)

    def __unicode__(self):
        return self.first_name


