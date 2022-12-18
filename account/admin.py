from django.contrib import admin
from .models import User
from django.contrib.auth.password_validation import validate_password

# Register your models here.


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    fields = (
        'username', 'id', 'is_staff', 'is_superuser', 'is_active', 'password', 'first_name', 'last_name', 'email')
    list_display = ('username', 'is_staff', 'is_superuser')
    readonly_fields = ('id',)
    search_fields = ('username',)

    def save_model(self, request, obj, form, change):

        if obj.pk:
            orig_obj = User.objects.get(pk=obj.pk)
            if obj.password != orig_obj.password:
                obj.set_password(obj.password)
        else:
            obj.set_password(obj.password)
        obj.save()