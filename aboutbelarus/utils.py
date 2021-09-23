from django.db.models import Count

from .models import *

menu = [{'title': 'Главная страница', 'url_name': 'home'},
        {'title': 'О проекте', 'url_name': 'about'},
        {'title': 'Контакты', 'url_name': 'contact'},
        {'title': 'Наши партнеры', 'url_name': 'partners'},
        ]


class DataMixin:
    paginate_by = 10

    def get_user_context(self, **kwargs):
        context = kwargs
        cats = Category.objects.annotate(Count('aboutbelarus'))
        context['menu'] = menu
        context['cats'] = cats
        if 'cat_selected' not in context:
            context['cat_selected'] = 0
        return context
