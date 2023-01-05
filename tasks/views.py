from django.http import HttpResponse
from django.shortcuts import render, redirect
from tasks.models import Collection
from django.utils.html import escape

# Create your views here.
def index(request):
    context = {}
    context['collections'] = Collection.objects.order_by("name")
    return render(request, 'tasks/index.html', context=context)

def add_collection(request):
    collection_name = escape(request.POST.get("collection-name"))
    Collection.objects.create(name=collection_name)
    return redirect('home')