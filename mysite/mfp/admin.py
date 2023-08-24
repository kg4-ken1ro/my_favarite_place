from django.contrib import admin

# Register your models here.
from .models import Restaurant, C_store, Restroom

admin.site.register(Restaurant)
admin.site.register(C_store)
admin.site.register(Restroom)


# from django.contrib.auth.models import Group
# from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# from .models import User

# class UserAdmin(BaseUserAdmin):
#     list_display = (
#         "email",
#         "active",
#         "staff",
#         "admin",
#     )
#     list_filter = (
#         "admin",
#         "active",
#     )
#     ordering = ("email",)
#     filter_horizontal = ()
#     ordering = ("email",)
#     search_fields = ('email',)

#     fieldsets = (
#         (None, {'fields': ('email', 'password')}),
#         ('Permissions', {'fields': ('staff','admin',)}),
#     )

#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('email', 'password1', 'password2')}
#         ),
#     )

# admin.site.register(User,UserAdmin)
# admin.site.unregister(Group)