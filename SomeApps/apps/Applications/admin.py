from django.contrib import admin

from .models import Application


class ApplicationAdmin(admin.ModelAdmin):
    model = Application
    list_display = ('id', 'title', 'api_key')


admin.site.register(Application, ApplicationAdmin)
