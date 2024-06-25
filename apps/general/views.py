from django.shortcuts import redirect
from django.views.generic import TemplateView


class HomeTemplateView(TemplateView):
    template_name = 'index.html'


class MapTemplateView(TemplateView):
    template_name = 'map.html'


def set_language(request):
    language_code = request.POST.get('language', 'uz')
    return redirect(request.META["HTTP_ORIGIN"] + f'/{language_code}/')
