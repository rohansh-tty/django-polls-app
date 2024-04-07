from django.contrib import admin

# Register your models here.
# data base models 
# db - columns, data type of each column
from .models import Question, Choice

admin.site.register(Question)
admin.site.register(Choice)


