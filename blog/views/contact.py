from django.shortcuts import render
from django.core.paginator import Paginator
from django.db.models import Q

def contact(request):
    context={
    'key' : 'value',
    'key1' : 'value1',
    'key2' : 'value2',
    }
    return render(request, 'contact.html', context)
