from django.contrib import admin
from .models import create_rules,ques_create,create_topic
# Register your models here.
admin.site.register(create_rules)
admin.site.register(ques_create)
admin.site.register(create_topic)

