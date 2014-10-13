from django.contrib import admin

# Register your models here.
import models
admin.site.register(models.Blog)
admin.site.register(models.Category)
admin.site.register(models.Tag)
admin.site.register(models.ClientInfo)
