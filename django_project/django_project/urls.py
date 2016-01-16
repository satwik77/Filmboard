from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
# from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
admin.autodiscover()

from registration import views 

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/', views.user_login, name='login'),
    url(r'^logout/', views.user_logout, name='logout'),    
    url(r'^register/', views.artist_registration, name='artistregistration'),
    url(r'^dashboard/', views.dashboard, name='dashboard'),
    url(r'^updateprofile/', views.update_profile, name='updateprofile'),
    url(r'^addexp/', views.add_exp, name='addexperience'),
    url(r'^viewexp/', views.view_experiences, name='viewexperience'),
    url(r'^seek_rec/', views.seek_rec, name='seekrecommendation'),
    url(r'^view_rec/', views.view_rec, name='viewrecommendation'),
    url(r'^home/', views.home, name='home'),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
