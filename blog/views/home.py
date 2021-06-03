from django.shortcuts import render
from django.core.paginator import Paginator
from django.db.models import Q


def home(request):
    context={
    'key' : 'value',
    'key1' : 'value1',
    'key2' : 'value2',
    }
    return render(request, 'home.html', context)
