from django.contrib import admin
from apps.user.models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'full_name', 'date_joined')

    def full_name(self, user):
        return user.get_full_name()


admin.site.register(User, UserAdmin)

