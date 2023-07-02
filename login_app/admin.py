from django.contrib import admin
from .models import Document
from .models import Member
# Register your models here.
admin.site.register(Document)
admin.site.register(Member)