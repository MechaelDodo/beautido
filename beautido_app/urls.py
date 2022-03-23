from django.urls import path
from .views import index, index_second, about

urlpatterns = [
    path('', index, name='home'),
    path('second/<int:secid>/', index_second),
    path('about/', about),
]

