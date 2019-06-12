from dal import autocomplete

from blog.models import Category, Tag


class CategoryAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated(): #判断用户是否登入
            return Category.objects.none()    #如果是未登入用户，则返回空的queryset
        
        qs = Category.objects.filter(owner=self.request.user) #获取该用户的所有分类

        if self.q:    #q是url上传过来的值
           qs = qs.filter(name__istartswith=self.q) #用name_istartswith进行查询
        return qs #返回queryset

class TagAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated():
            return Tag.objects.none()
        
        qs = Tag.objects.filter(owner=self.request.user)

        if self.q:
            qs = qs.filter(name__istartswith=self.q)
        return qs