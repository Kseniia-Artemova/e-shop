from django.contrib import admin
from catalog.models import Category, Product, Contact
from django.utils.html import format_html

# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'price',
        'category',
        'toggle_description_button',
    )
    list_filter = ('category', )
    search_fields = ('name', 'description')
    fields = ['name', 'description', 'image', 'price', 'category']

    def toggle_description_button(self, obj):
        return format_html(
            '<div class="description-wrapper">'
            '    <button type="button" class="toggle-description">Развернуть</button>'
            '    <div class="description-content hidden-description">{}</div>'
            '</div>',
            obj.description
        )
    toggle_description_button.short_description = 'Описание'

    class Media:
        css = {
            'all': ('css/admin_description_button.css',)
        }
        js = (
            'js/admin_description_button.js',
        )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    search_fields = ('name', )
    fields = ['name', 'image']


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'inn', 'address')
    search_fields = ('inn', )