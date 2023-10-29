from django.contrib import admin

from .models import Birthday, Tag


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = (
        'tag',
    )


@admin.register(Birthday)
class BirthdayAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'birthday',
        'image',
        'author',
    )


class BirthdayInline(admin.TabularInline):
    model = Birthday
    extra = 1
