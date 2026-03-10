from django.contrib import admin
from .models import Post, PostImages, Comment, Projects, ProjectImages

# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}
    
@admin.register(PostImages)
class PostImagesAdmin(admin.ModelAdmin):
    list_display = ('post', 'image')
    search_fields = ('post__title',)
    
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'content', 'created_at')
    search_fields = ('post__title', 'content')
    

@admin.register(Projects)
class ProjectsAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'created_at')
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(ProjectImages)
class ProjectImagesAdmin(admin.ModelAdmin):
    list_display = ('project', 'image')
    search_fields = ('project__title',)    
