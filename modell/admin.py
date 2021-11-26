from django.contrib import admin
from .models import User,Posts,Bio,Comment,Likes#,#Reply
# Register your models here.
admin.site.register(User)
admin.site.register(Posts)
admin.site.register(Bio)
admin.site.register(Comment)
#admin.site.register(Reply)
admin.site.register(Likes)
