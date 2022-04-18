from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy

from .models import *
from .forms import *
from django.views.generic import ListView, DetailView, CreateView

# Create your views here.

#menu = ['About', 'Add girl', 'Hot girls', 'Sign']

#menu = [
#    {'title': 'About', 'url_name': 'about'},
#    {'title': 'Add girl', 'url_name': 'add_girl'},
#    {'title': 'Photos', 'url_name': 'show_photos'},
#    {'title': 'Login', 'url_name': 'login'},
#]


class GirlsHome(ListView):
    model = Girl
    template_name = 'beautido_app/index.html'
    context_object_name = 'girls'
    extra_context = {'title': 'Главная страница',
                     'cat_selected': 0, }

    def get_queryset(self):
        return Girl.objects.filter(is_published=True)

# def index(request):
#     girls = Girl.objects.all()
#     #categories = Category.objects.all()
#     context = {
#         'title': 'Start page',
#         #'menu': menu,
#         'girls': girls,
#         #'categories': categories,
#         'cat_selected': 0,
#     }
#     return render(request, 'beautido_app/index.html', context)


def about(request):
    context = {
        'title': 'About',
        #'menu': menu,
    }
    return render(request, 'beautido_app/about.html', context)


class AddGirl(CreateView):
    form_class = AddGirlForm
    template_name = 'beautido_app/add_girl.html'
    extra_context = {'title': 'Добавить девушку'}
    success_url = reverse_lazy('home')

def add_girl(request):
    if request.method == 'POST':
        form = AddGirlForm(request.POST, request.FILES)
        if form.is_valid():

                #Girl.objects.create(**form.cleaned_data)
            form.save()
            return redirect('home')

    else:
        form = AddGirlForm()
    context = {
        'title': 'Add girl',
        'form': form,
    }
    return render(request, 'beautido_app/add_girl.html', context)


def show_photos(request):
    return HttpResponse('Photos')


def login(request):
    return HttpResponse('Login')


class ShowGirl(DetailView):
    model = Girl
    template_name = 'beautido_app/girl.html'
    context_object_name = 'girl'
    slug_url_kwarg = 'girl_slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['girl'].title
        return context


# def show_girl(request, girl_slug):
#     girl = get_object_or_404(Girl, slug=girl_slug)
#     context = {
#         'title': girl.title,
#         'girl': girl,
#         'cat_selected': girl.category_id,
#     }
#
#     return render(request, 'beautido_app/girl.html', context)


class ShowCategory(ListView):
    model = Girl
    template_name = 'beautido_app/index.html'
    context_object_name = 'girls'
    allow_empty = False
    #extra_context = {'title': 'Главная страница'}

    def get_queryset(self):
        return Girl.objects.filter(category__slug=self.kwargs['category_slug'], is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Категория - ' + str(context['girls'][0].category)
        context['cat_selected'] = context['girls'][0].category.slug
        return context



# def show_the_category(request, category_slug):
#     category_id = Category.objects.get(slug=category_slug).pk
#     girls = Girl.objects.filter(category_id=category_id)
#     #categories = Category.objects.all()
#     context = {
#         'title': 'Start page',
#         #'menu': menu,
#         'girls': girls,
#         #'categories': categories,
#         'cat_selected': category_slug,
#     }
#     return render(request, 'beautido_app/index.html', context)

#def index_second(request, secid):
#    if request.GET:
#        print(request.GET['name'])
#    smth = "This is second page! %s " % secid
#    return HttpResponse(smth)
