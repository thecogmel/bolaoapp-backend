from django.contrib import admin
from .models import User

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    search_fields = ["nickname"]
    list_display = (
        "id",
        "name",
        "nickname",
        "is_active",
        "is_superuser",
        "created_at",
    )


admin.site.register(User, UserAdmin)
