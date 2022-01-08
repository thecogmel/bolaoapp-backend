from django.contrib import admin
from .models import Post

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    search_fields = ["content"]
    list_display = ("id", "content", "description", "created_at", "user")


admin.site.register(Post, PostAdmin)
