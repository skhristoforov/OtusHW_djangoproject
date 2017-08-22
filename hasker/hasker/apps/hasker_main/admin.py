from django.contrib import admin
from hasker.apps.hasker_main.models import *

# Register your models here.

admin.site.register(HaskerUser)
admin.site.register(HaskerQuestion)
admin.site.register(HaskerAnswer)
admin.site.register(HaskerTag)
