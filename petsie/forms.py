from django.contrib.auth.forms import UserCreationForm
from django import forms
from petsie.models import User


class PetSitterOwner_Form(UserCreationForm):

    phone_number = forms.CharField()
    address = forms.CharField()
    city = forms.CharField()
    state_abbr = forms.CharField()
    zipcode = forms.CharField()
    # Desired_service_type = forms.CharField()

    CHOICES = (('Pet Sitter', 'Pet Sitter',), ('Pet Owner', 'Pet Owner',))
    usertype = forms.ChoiceField(label= 'Are you a:', widget=forms.RadioSelect, choices=CHOICES)

    # usertype = forms.ChoiceField(widget = forms.Select(),
    #         choices = ['pet sitter', 'pet owner'], required=True,)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email','phone_number','address', 'city', 'state_abbr', 'zipcode','usertype']


