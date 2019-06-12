from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from django.contrib.admin.models import LogEntry

import xadmin
from xadmin.layout import Row, Fieldset, Container
from xadmin.filters import manager
from xadmin.filters import RelatedFieldListFilter

from .models import Post, Tag, Category
from .adminforms import PostAdminForm
#from typeidea.custom_site import custom_site
from typeidea.base_admin import BaseOwnerAdmin


class CategoryOwnerFilter(RelatedFieldListFilter):
    
    @classmethod
    def test(cls, field, request, params, model, admin_view, field_path):
        return field.name == 'category'
    
    def __init__(self, field, request, params, model, model_admin, field_path):
        super().__init__(field, request, params, model, model_admin, field_path)
        #重新获取lookup_choices,根据owner过滤
        self.lookup_choices = Category.objects.filter(owner=request.user).values_list('id', 'name')

manager.register(CategoryOwnerFilter, take_priority=True)


class PostInline(BaseOwnerAdmin):
    form_layout = (
        Container(
            Row("title", "desc")
        )
    )
    extra = 1  #控制额外多几个
    model = Post


@xadmin.sites.register(Category)
class CategoryAdmin(BaseOwnerAdmin):
    inlines = [PostInline,]
    list_display = ('name', 'status', 'is_nav', 'created_time', 'owner', 'post_count')
    fields = ('name', 'status', 'is_nav', 'owner')

    def post_count(self, obj):
        return obj.post_set.count()
    
    post_count.short_description = '文章数量'


@xadmin.sites.register(Tag)
class TagAdmin(BaseOwnerAdmin):
    list_display = ('name', 'status', 'owner', 'created_time')
    fields = ('name', 'status', 'owner')
  

@xadmin.sites.register(Post)
class PostAdmin(BaseOwnerAdmin):
    form = PostAdminForm
    list_display = ('title', 'category', 'status', 'created_time', 'owner', 'operator')
    list_display_link = []

    list_filter = ['category'] #注意这里定义的不是filter类，而是字段名
    search_fields = ['title', 'category__name']
    
    actions_on_top = True
    actions_on_bottom = True
    save_on_top = True

    #fields = (('category', 'title'), 'desc', 'status', 'content', 'tag')
    filter_horizontal = ('tag',)
    form_layout = (
        Fieldset(
            '基础信息',
            Row("title", "category"),
            'status',
            'tag',
        ),
        Fieldset(
            '内容信息',
            'desc',
            'content',
        )
    )

    def operator(self, obj):
        return format_html(
            '<a href="{}">编辑</a>',
            self.model_admin_url('change', obj.id)
        )
    operator.short_description = '操作'

    @property
    def media(self):
        # xadmin 基于bootstrap,引入会导致页面样式冲突，这里只做演示
        media = super().media
        media.add_js(['https://cdn.bootcss.com/bootstrap/4.0.0-beta.2/js/bootstrap.bundle.js'])
        media.add_css({'all':("https://cdn.bootcss.com/bootstrap/4.0.0-beta.2/css/bootstrap.min.css",)},)
        return media


@xadmin.sites.register(LogEntry)
class LogEntryAdmin(BaseOwnerAdmin):
    list_display = ('object_repr', 'object_id', 'action_flag', 'user', 'change_message')

    
    