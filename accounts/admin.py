from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Student)
admin.site.register(Trainer)
admin.site.register(Tag)
admin.site.register(Topic)
admin.site.register(Fee)
admin.site.register(bookdemo)
admin.site.register(contact)
admin.site.register(image)