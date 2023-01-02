from django.contrib import admin

from .models import Tag, Entry, Comment


admin.site.register([Entry, Comment, Tag])
