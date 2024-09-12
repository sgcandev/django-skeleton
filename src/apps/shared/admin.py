from django.contrib import admin

from src.apps.shared.models import Cargo, DocumentState


@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    pass


@admin.register(DocumentState)
class DocumentStateAdmin(admin.ModelAdmin):
    pass
