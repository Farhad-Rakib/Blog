from django.contrib import admin
from .models import Category, Post
# Register your models here.

class PostModelAdmin(admin.ModelAdmin):
    list_filter = ("title","published","created")
    list_display = ("title","author","status","created")
    search_fields=("title","author")
    

class CategoryModelAdmin(admin.ModelAdmin):
    list_filter = ("name","created")
    list_display = ("name","slug","created")
    search_fields=("name","slug")



admin.site.register(Post,PostModelAdmin)
admin.site.register(Category,CategoryModelAdmin)



### admin page header and title changed
admin.site.site_title = 'Tech Mentor Admin'
admin.site.site_header = 'Tech Mentor Admin'
