# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.admin.actions import delete_selected
admin.site.add_action(delete_selected)

from main.models import *

class PersonAdmin(admin.ModelAdmin):
    pass

class ActivityAdmin(admin.ModelAdmin):
    pass

admin.site.register(Person, PersonAdmin)
admin.site.register(Activity, ActivityAdmin)