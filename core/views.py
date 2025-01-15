from django.shortcuts import render, get_object_or_404
from .models import Store

def store_list(request):
    stores = Store.objects.all()
    return render(request, 'core/store_list.html', {'stores': stores})

def store_detail(request,pk):
    store = get_object_or_404(Store, pk=pk)
    return render(request, 'core/store_detail.html', {'store': store})


