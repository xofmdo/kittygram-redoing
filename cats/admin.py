from django.contrib import admin
from .models import Cat, Owner


@admin.register(Cat)
class CatAdmin(admin.ModelAdmin):
    """Страница котов в админке"""

    list_display = (
        'name',
        'color',
        'birth_year'
    )
    search_fields = ('name',)
    empty_value_display = '-пусто-'


@admin.register(Owner)
class CommentAdmin(admin.ModelAdmin):
    """Страница хозяев в админке"""

    list_display = (
        'last_name',
        'last_name'
    )

    search_fields = (
        'last_name',
        'last_name'
    )
    empty_value_display = '-пусто-'
