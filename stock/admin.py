from django.contrib import admin

from .models import Stock, Category, Equipment

admin.site.register(Stock)
admin.site.register(Category)


class EquipmentAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Equipment._meta.fields]
    list_editable = ["number"]
    list_filter = ("name", "category", "stock", )
    sortable_by = ["stock", "created_at", "category"]

    class Meta:
        model = Equipment


admin.site.register(Equipment, EquipmentAdmin)