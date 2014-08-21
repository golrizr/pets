from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static

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

    url(r'^edit_profile/(?P<user_id>\w+)/edit/$', 'petsie.views.edit_profile', name='edit_profile'),
    url(r'^upload_pet_profile/$', 'petsie.views.upload_pet_profile', name='upload_pet_profile'),
    url(r'^edit_pet_profile/(?P<user_id>\w+)/edit/$', 'petsie.views.edit_pet_profile', name='edit_pet_profile'),


    url(r'^view_sitter_profile/(?P<user_id>\w+)/$', 'petsie.views.view_sitter_profile', name='view_sitter_profile'),
    url(r'^contact_petsitter/$', 'petsie.views.contact_petsitter', name='contact_petsitter'),



)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)