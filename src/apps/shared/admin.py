from django.contrib import admin

from src.apps.shared.models import Cargo, DocumentState, Documentsort


@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    pass


@admin.register(DocumentState)
class DocumentStateAdmin(admin.ModelAdmin):
    pass


@admin.register(Documentsort)
class DocumentSortAdmin(admin.ModelAdmin):
    pass
