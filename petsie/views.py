from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render, redirect
from petsie.forms import PetSitterOwner_Form
from petsie.models import User



# Create your views here.


def home(request):
    return render(request, 'home_page.html')

def register(request):
    if request.method == 'POST':
        form = PetSitterOwner_Form(request.POST)

        if form.is_valid():
            form.save()

            messages.info(request, "Thanks for registering. You are now logged in.")
            new_user = authenticate(username=request.POST['username'],
                                    password=request.POST['password1'])
            login(request, new_user)
            return redirect("redirect_type")
            #
            # return HttpResponseRedirect(reverse("boot"))

    else:
        form = PetSitterOwner_Form()

    return render(request, "registration/register.html", {
        'form': form,
    })


@login_required
def profile(request):
    return render(request, 'profile.html', {})


def redirect_type(request):
    if(request.user.usertype=='Pet Sitter'):
        return redirect('pet_sitters')
    else:
        return redirect('pet_owners')


def pet_sitters(request):
    return render(request, 'pet_sitters.html')

def pet_owners(request):
    users = User.objects.filter(usertype='Pet Sitter')
    return render(request, 'pet_owners.html', {'users': users})



def aboutus(request):
    return render(request, 'aboutus.html')