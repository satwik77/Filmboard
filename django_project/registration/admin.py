from django.contrib import admin
from registration.models import *

# Register your models here.


class ArtistAdmin(admin.ModelAdmin):
    list_display = ('name', 'gender')
    list_filter = ['location']
    search_fields = ['name']

class ExpAdmin(admin.ModelAdmin):
    list_display = ('project_name', 'project_type')
    search_fields = ['project_name']

class RecAdmin(admin.ModelAdmin):
    list_display = ('project_name', 'project_type')
    search_fields = ['project_name']    


admin.site.register(Artist, ArtistAdmin)
admin.site.register(PastExperiences, ExpAdmin)
admin.site.register(Recommendations, RecAdmin)
