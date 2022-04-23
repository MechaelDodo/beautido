
menu = [
   {'title': 'О сайте', 'url_name': 'about'},
   {'title': 'Добавить девушку', 'url_name': 'add_girl'},
   {'title': 'Фотографии', 'url_name': 'show_photos'},
   # {'title': 'Login', 'url_name': 'login'},
]


class DataMixin:
    paginate_by = 3

    def get_user_context(self, **kwargs):
        context = kwargs
        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(1)
        context['menu'] = user_menu
        if 'cat_selected' not in context:
            context['cat_selected'] = 0
        return context
