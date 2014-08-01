from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pets.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'petsie.views.home', name='home'),
    url(r'^register/$', 'petsie.views.register', name='register'),
    url(r'^profile/$', 'petsie.views.profile', name='profile'),
    url(r'^redirect_type/$', 'petsie.views.redirect_type', name='redirect_type'),



    #Login form
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),
    url(r'^aboutus/$', 'petsie.views.aboutus', name='aboutus'),

    #profile types
    url(r'^pet_sitters', 'petsie.views.pet_sitters', name='pet_sitters'),
    url(r'^pet_owners', 'petsie.views.pet_owners', name='pet_owners'),




)
