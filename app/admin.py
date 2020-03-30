from django.contrib import admin
from . models import Contact
from django.contrib.auth.models import Group
from import_export.admin import ImportExportModelAdmin

# Register your models here.
#class ContactAdmin(admin.ModelAdmin):
class ContactAdmin(ImportExportModelAdmin):
    list_display=('id','firstname','lastname','gender','phone','email','info','datecreated')
    list_filter =('gender', 'datecreated')
    list_per_page =15
    list_display_links =['id', 'firstname','lastname']
    list_editable =('gender', 'phone')
    search_fields = ['firstname','lastname','gender','phone','email','info']

admin.site.register(Contact,ContactAdmin)
admin.site.unregister(Group)