from django.contrib import admin

from .models import Todo, ChoiceModels
# Register your models here.

MODELS = [
    Todo,
    ChoiceModels,
]

admin.site.register(MODELS)