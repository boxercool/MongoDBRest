from django.contrib import admin

# Register your models here.
from .models import Posts, PostsRates

admin.site.register(Posts)
admin.site.register(PostsRates)
