from django.contrib import admin
from .models import Project
# Register your models here.

#admin.site.register(Project)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'desc')
    list_editable = ('title',)
    list_filter = ('title', 'created', 'updated')
    search_fields = ('title',)
