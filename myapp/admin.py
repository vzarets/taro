from django.contrib import admin

from django.contrib import admin
from .models import Question, Card, Interpretation

admin.site.register(Question)
admin.site.register(Card)
admin.site.register(Interpretation)

