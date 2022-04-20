from django.urls import path
from .views import *

urlpatterns = [
    # path('', index, name='home'),
    path('', GirlsHome.as_view(), name='home'),
    #path('second/<int:secid>/', index_second),
    path('about/', about, name='about'),
    path('new_girl/', AddGirl.as_view(), name='add_girl'),
    path('photos/', show_photos, name='show_photos'),
    path('login/', login, name='login'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('girl/<slug:girl_slug>/', ShowGirl.as_view(), name='show_girl'),
    path('category/<slug:category_slug>/', ShowCategory.as_view(), name='show_the_category'),
]

