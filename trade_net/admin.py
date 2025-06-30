from django.contrib import admin

from .models import Product, NetUnit


@admin.action(description="Очистить задолженость")
def clear_dept(modeladmin, request, queryset):
    queryset.update(dept=0.0)


class ProdictInLine(admin.TabularInline):
    model = Product
    extra = 0


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "model", "release_date", "manufacture"]
    list_filter = ["name", "model", "release_date", "manufacture"]
    search_help_text = "name"


@admin.register(NetUnit)
class NetUnitAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "email",
        "country",
        "city",
        "address",
        "supplier",
        "dept",
        "created_at",
    ]
    list_filter = ["unit_type", "name", "country", "city"]
    search_help_text = ["name", "country", "city"]
    inlines = [ProdictInLine]
    actions = [clear_dept]
