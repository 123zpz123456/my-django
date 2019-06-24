from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from .models import Post, Category
from .serializers import (
    PostSerializer, PostDetailSerializer,
    CategorySerializer,    
) 


class PostViewSet(viewsets.ReadOnlyModelViewSet):
    '''提供文章接口'''
    serializer_class = PostSerializer    #PostSerializer实现数据列表页
    queryset = Post.objects.filter(status=Post.STATUS_NORMAL)
    #permission_classes = [IsAdminUser]    #写入时的权限校验

    def retrieve(self, request, *arg, **kwargs):
        self.serializer_class = PostDetailSerializer
        return super().retrieve(request, *arg, **kwargs)
    
    def filter_queryset(self, queryset):
        category_id = self.request.query_params.get('category')
        if category_id:
            queryset = queryset.filter(category_id=category_id)
        return queryset


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.filter(status=Category.STATUS_NORMAL)