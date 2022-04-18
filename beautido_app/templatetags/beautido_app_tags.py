from django import template
from beautido_app.models import *

register = template.Library()
menu = [
    {'title': 'О сайте', 'url_name': 'about'},
    {'title': 'Добавить девушку', 'url_name': 'add_girl'},
    {'title': 'Фото', 'url_name': 'show_photos'},
    {'title': 'Login', 'url_name': 'login'},
]

@register.simple_tag()
def get_categories():
    return Category.objects.all()


@register.inclusion_tag('beautido_app/list_categories.html')
def show_categories(sort=None, cat_selected=0):
    if not sort:
        categories = Category.objects.all()
    else:
        categories = Category.objects.order_by(sort)
    return {'categories': categories, 'cat_selected': cat_selected}


# @register.inclusion_tag('beautido_app/list_menu.html')
# def show_menu():
#     return {'menu': menu}
