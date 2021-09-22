import view as view
from django.urls import path
from django.views.decorators.cache import cache_page

from .views import *

urlpatterns = [
    path('', cache_page(60*30)(AboutBelarusHome.as_view()), name='home'),
    path('about/', AboutSite.as_view(), name='about'),
    path('contact/', ContactFormView.as_view(), name='contact'),
    path('partners/', PartnersProject.as_view(), name='partners'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('category/<slug:cat_slug>/', cache_page(60*30)(AboutBelarusCategory.as_view()), name='category'),
]
