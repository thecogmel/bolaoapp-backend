from django.contrib import admin
from .models import Post, Reaction

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    search_fields = ["content"]
    list_display = ("id", "content", "description", "created_at", "user")


class ReactionAdmin(admin.ModelAdmin):
    search_fields = ["like"]
    list_display = ("id", "like", "created_at", "post", "user")


admin.site.register(Post, PostAdmin)
admin.site.register(Reaction, ReactionAdmin)
