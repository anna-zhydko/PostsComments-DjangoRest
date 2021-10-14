from django.contrib import admin
from .models import NewsPost, Comment, Upvote


admin.site.register(NewsPost)
admin.site.register(Comment)
admin.site.register(Upvote)
