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

    url(r'^logintest/', views.user_login_test, name='login_test'),
    
    url(r'^logout/', views.user_logout, name='logout'),    
    url(r'^register/', views.initial_registration, name='artistregistration'),
    url(r'^register_profile/', views.register_profile, name='artistregistration'),


    url(r'^dashboard/', views.dashboard, name='dashboard'),
    # url(r'^dashboard_allied/', views.dashboard_allied, name='dashboard_allied'),
    url(r'^updateprofile/', views.update_profile, name='updateprofile'),
    url(r'^addexp/', views.add_exp, name='addexperience'),
    url(r'^viewexp/', views.view_experiences, name='viewexperience'),
    url(r'^editexp/(?P<expid>[0-9]+)/', views.change_exp, name='editexperience'),    
    url(r'^seek_rec/', views.seek_rec, name='seekrecommendation'),
    url(r'^view_rec/', views.view_rec, name='viewrecommendation'),
    url(r'^home/', views.home, name='home'),
    url(r'^projects/', views.show_projects, name='projectlistings'),
    url(r'^projects-details/(?P<project_id>[0-9]+)/', views.show_project_details, name='projectdetails'),
    url(r'^apply/(?P<requirement_id>[0-9]+)/', views.apply_for_project, name='apply_for_project'),
    
    url(r'^addproject/', views.add_project, name='addproject'),
    url(r'^addrequirements/(?P<project_id>[0-9]+)/', views.add_req, name='addrequirements'),
    # url(r'^saverequirements/(?P<project_id>[0-9]+)/', views.save_req, name='saverequirements'),

    url(r'^artist_search/(?P<art_id>[0-9]+)/', views.show_profile, name='show profile'),
    url(r'^artist_search/', views.artist_search, name='artist_search'),
    
    url(r'^my-projects/', views.my_projects, name='myprojectlistings'),
    url(r'^my-projects-details/(?P<project_id>[0-9]+)/', views.my_project_details, name='myprojectdetails'),
    url(r'^my-projects-requirements/(?P<requirement_id>[0-9]+)/', views.my_project_requirements, name='myprojectdetails'),


    url(r'^prod_profile/(?P<prod_id>[0-9]+)/', views.show_profile_prod, name='show profile prod'),
   
    url(r'^guest_talent/',views.guest_artist_dashboard, name='guest artist'),
    url(r'^guest_service/',views.guest_allied_dashboard, name='guest allied'),
    url(r'^guest_producer/',views.guest_producer_dashboard, name='guest producer'),

    # url(r'^guest/allied/',views.guest_allied_dashboard, name='guest allied'),
    # url(r'^guest/production/',views.guest_production_dashboard, name='guest production'),
    url(r'^applyGoogle/', views.get_google_json, name='googlejson'),
    url(r'^googlereg/', views.google_user_select_type, name='google_user_select_type'),

    url(r'^mailtest/', views.mail_test, name='login'),
    # url(r'^fblogin/', views.fb_login, name='fblogin'),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
