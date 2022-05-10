from django.urls import path
from django.views.decorators.cache import cache_page

from .views import *


urlpatterns = [
    # path('', index, name='home'),
    path('', cache_page(60)(GirlsHome.as_view()), name='home'),
    #path('second/<int:secid>/', index_second),
    path('about/', about, name='about'),
    path('new_girl/', AddGirl.as_view(), name='add_girl'),


    path('photos/', ShowPhotos.as_view(), name='show_photos'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', LoginUser.logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('girl/<slug:girl_slug>/', ShowGirl.as_view(), name='show_girl'),
    path('category/<slug:category_slug>/', ShowCategory.as_view(), name='show_the_category'),
]

