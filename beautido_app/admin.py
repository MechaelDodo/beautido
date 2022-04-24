from django.contrib import admin
from .models import *

# Register your models here.


class GirlAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'photo', 'time_create', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published', )
    list_filter = ('time_create', 'is_published')
    prepopulated_fields = {'slug': ('title',)}


class CategoryAdmin(admin.ModelAdmin):
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Girl, GirlAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Score)
