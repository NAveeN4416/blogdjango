from django.contrib import admin

from . models import blogdata, User_profile, Likes_dislikes, author_favorites
# Register your models here.

admin.site.register(blogdata)
admin.site.register(User_profile)
admin.site.register(Likes_dislikes)
admin.site.register(author_favorites)