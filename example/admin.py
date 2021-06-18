from django.contrib import admin

from example.models import Example


class ExampleAdmin(admin.ModelAdmin):
    list_display = ['id', 'date', 'datetime']
    list_display_links = ['date', 'datetime']
    list_per_page = 25


admin.site.register(Example, ExampleAdmin)
