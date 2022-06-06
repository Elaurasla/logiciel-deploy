from django.contrib import admin

from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Shopper

from django.contrib.auth.admin import GroupAdmin as DjangoGroupAdmin
from django.contrib.auth.models import Group as DjangoGroup
from .models import Shopper, Group


class ShopperCreationForm(forms.ModelForm):
    class Meta:
        model = Shopper
        fields= '__all__'

class ShopperForm(forms.ModelForm):
    class Meta:
        model = Shopper
        fields= '__all__'

class ShopperAdmin(UserAdmin):
    class Meta:
        model = Shopper
        form = ShopperForm
        add_form = ShopperCreationForm

        list_display = ('id', 'first_name', 'last_name', 'email', 'mobile_number',)
        fieldsets = (
            (None, {'fields': ('username', 'password',)}),
            ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'date_joined', 'last_login', 'is_online',)}),
            ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions',)}),
            ('Coco', {'fields': ('my_time_field', 'mobile_number',)}),
        )
        add_fieldsets = (
         (None, {
                'classes': ('wide',),
                'fields': ('username', 'mobile_number', 'email', 'first_name', 'last_name',)}
            ),
        )
        search_fields = ('id', 'mobile_number', 'email', 'first_name', 'last_name',)
        ordering = ('last_name', 'first_name',)

        class Meta:
            model = Shopper

    
admin.site.register(Shopper)

admin.site.unregister(DjangoGroup)
admin.site.register(Group, DjangoGroupAdmin)