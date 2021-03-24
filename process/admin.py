from django.contrib import admin
from process.models import IndustryModel
from django.contrib.auth.models import Group,User

admin.site.register(IndustryModel)

admin.site.unregister(Group)
admin.site.unregister(User)
