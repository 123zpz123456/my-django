from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from .models import Post
from .serializers import PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer    #PostSerializer实现数据列表页
    queryset = Post.objects.filter(status=Post.STATUS_NORMAL)
    #permission_classes = [IsAdminUser]    #写入时的权限校验

