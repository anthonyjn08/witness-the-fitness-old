from django.contrib import admin
from .models import Classes


class ClassesAdmin(admin.ModelAdmin):
    list_display = (
        'sport',
        'trainer_id',
    )

admin.site.register(Classes, ClassesAdmin)

