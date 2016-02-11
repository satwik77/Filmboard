from django.contrib import admin
from registration.models import *

# Register your models here.


class ArtistAdmin(admin.ModelAdmin):
    list_display = ('name', 'gender')
    list_filter = ['location']
    search_fields = ['name']

class AlliedAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    list_filter = ['location']
    search_fields = ['name']

class ProductionAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    list_filter = ['location']
    search_fields = ['name']

class ExpAdmin(admin.ModelAdmin):
    list_display = ('project_name', 'project_type')
    search_fields = ['project_name']

class RecAdmin(admin.ModelAdmin):
    list_display = ('project_name', 'project_type')
    search_fields = ['project_name']    

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('project_name', 'project_type')
    search_fields = ['project_name']

class notifyadmin(admin.ModelAdmin):
    list_display = ('user', 'sent')


admin.site.register(Artist, ArtistAdmin)
admin.site.register(Allied, AlliedAdmin)
admin.site.register(Production, ProductionAdmin)
admin.site.register(PastExperiences, ExpAdmin)
admin.site.register(Recommendations, RecAdmin)
admin.site.register(Projects, ProjectAdmin)
admin.site.register(ProjectRequirements)
admin.site.register(Notifications, notifyadmin)
