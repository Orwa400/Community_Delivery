from django.shortcuts import render, get_object_or_404
from .models import Store
from django.http import  HttpResponseRedirect, HttpResponse
from .forms import StoreForm

def home(request):
    return render(request, 'home.html')
   
def store_list(request):
    stores = Store.objects.all()
    return render(request, 'core/store_list.html', {'stores': stores})

def store_detail(request,pk):
    store = get_object_or_404(Store, pk=pk)
    return render(request, 'core/store_detail.html', {'store': store})

def store_create(request):
    if request.method == 'POST':
        form = StoreForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpREsponseRedirect('/stores/')
    else:
        form = StoreForm()
    return render(request, 'core/store_form.html', {'form': form})

def store_update(request, pk):
    store = get_object_or_404(Store, pk=pk)
    if request.method == 'POST':
        form = StoreForm(request.POST, instance=store) # Bind form with current store data
        if form_is.valid():
            form.save
            return HttpResponseRedirect('/stores/')
        else:
            form = StoreForm(instance=store)  # Pre-fill the form with the current store data

        return render(request, 'core/store_form.html', {'form': form})

def store_delete(request, pk):
    store = get_object_or_404(Store, pk=pk)
    if request.method =='POST':
        store.delete()
        return HttpResponseRedirect('/stores/')
    
    return render(request, 'core/store_confirm_delete.html', context)

# API Views
def store_list_api(request):
    stores = Store.objects.values()
    return JsonResponse({'stores': list(stores)})

def store_detail_api(request, pk):
    store = get_object_or_404(Store, pk=pk)
    data = {
        'id': store.id,
        'name': store.name,
        'address': store.address,
    }
    return JsonResponse(data)