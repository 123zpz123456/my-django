from django.contrib import admin

from .models import Comment

#from typeidea.custom_site import custom_site
from typeidea.base_admin import BaseOwnerAdmin


import xadmin


@xadmin.sites.register(Comment)
class CommentAdmin(BaseOwnerAdmin):
    list_display = ('target', 'nickname', 'content', 'website', 'create_time')

