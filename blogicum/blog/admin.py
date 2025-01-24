from django.contrib import admin

from .models import Category, Location, Post


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'slug',
        'is_published',
        'created_at'
    )
    search_fields = ['title', 'description']
    list_filter = ['is_published', 'created_at']
    list_editable = ('is_published',)


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'is_published',
        'created_at'
    )
    search_fields = ['name']
    list_filter = ['is_published', 'created_at']
    list_editable = ('is_published',)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'is_published',
        'author',
        'category',
        'location',
        'pub_date',
        'created_at'
    )
    search_fields = ['title', 'text', 'author__username']
    list_filter = ['is_published', 'pub_date', 'category', 'location']
    date_hierarchy = 'pub_date'
    list_editable = ('is_published',)
