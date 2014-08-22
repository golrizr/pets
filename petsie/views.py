from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render, redirect
from petsie.forms import PetSitterOwner_Form, PetProfile
from petsie.models import *

# Create your views here.

def home(request):
    return render(request, 'home_page.html')


def register(request):
    if request.method == 'POST':
        form = PetSitterOwner_Form(request.POST, request.FILES)

        if form.is_valid():
            form.save()

            # messages.info(request, "Thanks for registering. You are now logged in.")
            new_user = authenticate(username=request.POST['username'],
                                    password=request.POST['password1'])
            login(request, new_user)
            # return redirect("redirect_type")
            return redirect("profile")

    else:
        form = PetSitterOwner_Form()

    return render(request, "registration/register.html", {
        'form': form,
    })



@login_required
def profile(request):
    pet = Pet.objects.filter(owner=request.user)
    return render(request, 'profile.html', {'pet': pet, 'owner': "Pet Owner"},)


# @login_required
# def profile(request):
#     pet = Pet.objects.filter(owner=request.user)
#     return render(request, 'profile.html', {'pet': pet, 'owner': "Pet Owner"},)


def redirect_type(request):
    # Shouldn't need to hardcode the usertype string here, want to use a variable you've defined on your model
    if(request.user.usertype=='Pet Sitter'):
        return redirect('pet_sitters')
    else:
        return redirect('pet_owners')


@login_required
def pet_sitters(request):
    return render(request, 'pet_sitters.html')

@login_required
def pet_owners(request):
    # Shouldn't need to hardcode the usertype string here, want to use a variable you've defined on your model
    users = User.objects.filter(usertype='Pet Sitter')
    return render(request, 'pet_owners.html', {'users': users})

def aboutus(request):
    return render(request, 'aboutus.html')



@login_required
def edit_profile(request, user_id):
    user = User.objects.get(id=user_id)

    if request.method == "POST":
        form = PetSitterOwner_Form(request.POST, request.FILES, instance=user)
        if form.is_valid():
            if form.save():
                return redirect("/profile/")

    else:

        form = PetSitterOwner_Form(instance=user)
    data = {"profile": profile, "form": form}
    return render(request, "edit_profile.html", data)

@login_required
def upload_pet_profile(request):
    if request.method == "POST":
        form = PetProfile(request.POST, request.FILES)
        if form.is_valid():
            owner = request.user
            pet_image = form.cleaned_data['pet_image']
            name = form.cleaned_data['name']
            age = form.cleaned_data['age']
            description = form.cleaned_data['description']
            # Don't need to do this, your model form should take care of it
            Pet.objects.create(owner=owner, pet_image=pet_image, name=name, age=age, description=description)
            return redirect("/profile/")

    else:
        form = PetProfile()
    data = {"profile": profile, "form": form, "owner": 'Pet Owner'}
    return render(request, 'upload_pet_profile.html', data)

@login_required
def edit_pet_profile(request, user_id):
    pet = Pet.objects.filter(owner=user_id)[0]

    if request.method == "POST":
        form = PetProfile(request.POST, request.FILES, instance=pet)
        if form.is_valid():
            if form.save():
                return redirect("/profile/")

    else:

        form = PetProfile(instance=pet)
    data = {"form": form}
    return render(request, "edit_pet_profile.html", data)

@login_required
def view_sitter_profile(request, user_id):
    pet_owner_user = User.objects.get(id=user_id)
    pet = Pet.objects.filter(owner=pet_owner_user)
    # return render(request, 'profile.html', {'user': user, 'pet': pet, 'owner': "Pet Owner"},)

    return render(request, 'view_sitter_profile.html', {'pet_owner_user': pet_owner_user, 'pet': pet, 'owner': "Pet Owner"},)


    # return render(request, 'profile.html', {'random_user': user, 'pet': pet, 'owner': "Pet Owner"},)

def contact_petsitter(request):
    return render(request, 'contact_petsitter.html')
