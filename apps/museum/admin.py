from django.contrib import admin

from apps.museum.models import Category, SubCategory


class CategoryAdmin(admin.ModelAdmin):
    search_fields = ('name', 'slug')
    list_display = ['name', 'slug']


class SubCategoryAdmin(admin.ModelAdmin):
    search_fields = ('name', 'slug')
    list_filter = ('category',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
