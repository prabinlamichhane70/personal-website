from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Register your models here.
class UserModelAdmin(BaseUserAdmin):
  list_display = ('id', 'email', 'name' , 'is_editor','is_admin','is_staff','is_superuser')
  list_filter = ('is_admin',)
  fieldsets = (
      ('User Credentials', {'fields': ('email', 'password')}),
      ('Personal info', {'fields': ('name', )}),
      ('Permissions', {'fields': ('is_admin','is_editor','groups')}),
  )
  add_fieldsets = (
      (None, {
          'classes': ('wide',),
          'fields': ('email', 'name', 'password1', 'password2'),
      }),
  )
  search_fields = ('email',)
  ordering = ('email', 'id')
  # filter_horizontal = ('groups', 'user_permissions')


admin.site.register(User, UserModelAdmin)
