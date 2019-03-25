from django.shortcuts import render
from .models import Murr


def index(request):
    queryset = Murr.objects.filter(featured=True)
    context = {
        'object_list': queryset
    }
    return render(request, 'card_murr/index.html', context)
