from django.contrib import admin

from cheerup_board.models import Comment, Message, PhotoPost

# Register your models here.

@admin.register(PhotoPost)
class PostAdmin(admin.ModelAdmin):
	list_display = ['id', 'author', 'create_at']
	list_display_links = ['id', 'author']

@admin.register(Comment)
class CommnetAdmin(admin.ModelAdmin):
	list_display = ['id', 'author', 'post','create_at']
	list_display_links = ['id', 'author', 'post']

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
	list_display = ['id', 'author', 'create_at']
	list_display_links = ['id', 'author']