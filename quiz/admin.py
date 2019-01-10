from django.contrib import admin

# Register your models here.
from .models import Question, Category, Answers, Quiz, Option

admin.site.register(Question)
admin.site.register(Category)
admin.site.register(Answers)
admin.site.register(Quiz)
admin.site.register(Option)
