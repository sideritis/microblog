from django.views.generic import ListView
from django.http import Http404

from article.views import ArticleMixin


class TagsListView(ArticleMixin, ListView):
    template_name = 'articles/article_list.html'
    context_object_name = 'articles'
    paginate_by = 7

    def get_queryset(self):
        slug = self.kwargs.get('slug')

        # in case of None return 404
        if not slug:
            raise Http404

        queryset = super().get_queryset()
        queryset = queryset.filter(tags__slug__exact=slug)

        return queryset
