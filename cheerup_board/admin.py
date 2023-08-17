from django.contrib import admin

from cheerup_board.models import Comment, Message, PhotoPost

# Register your models here.
admin.site.register(PhotoPost)
admin.site.register(Comment)
admin.site.register(Message)