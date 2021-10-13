from django.contrib import admin
from .models import User

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    search_fields = ["email"]
    list_display = (
        "id",
        "email",
        "name",
        "nickname",
        "is_active",
        "is_superuser",
        "created_at",
    )


admin.site.register(User, UserAdmin)
