from django.contrib import admin

# Register your models here.
from quiz.models import Contact, Question

admin.site.register(Contact)
admin.site.register(Question)