from django.contrib import admin

from example.models import Example


class ExampleAdmin(admin.ModelAdmin):
    list_display = ['id', 'date', ]
    list_display_links = ['date', ]
    list_per_page = 25


admin.site.register(Example, ExampleAdmin)
