from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Profile)
admin.site.register(TodoGroup)
admin.site.register(TodoList)
admin.site.register(TodoLikes)