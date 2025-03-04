from django.shortcuts import render, get_object_or_404, redirect
from .models import Store, FavoriteStore
from django.http import  HttpResponseRedirect, HttpResponse, JsonResponse
from .forms import StoreForm
from django.contrib.auth import login, logout, authenticate 
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'home.html')
   
def store_list(request):
    stores = Store.objects.all()
    favorite_stores = []
    if request.user.is_authenticated:
        favorite_stores = Store.objects.filter(favoritestore__user=request.user)

    return render(request, 'store_list.html', {'stores': stores, 'favorite_stores': favorite_stores})

def store_detail(request,pk):
    store = get_object_or_404(Store, pk=pk)
    return render(request, 'core/store_detail.html', {'store': store})

def store_create(request):
    if request.method == 'POST':
        form = StoreForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/stores/')
    else:
        form = StoreForm()

    return render(request, 'core/store_form.html', {'form': form})

def store_update(request, pk):
    store = get_object_or_404(Store, pk=pk)
    if request.method == 'POST':
        form = StoreForm(request.POST, instance=store) # Bind form with current store data
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/stores/')
        else:
            form = StoreForm(instance=store)  # Pre-fill the form with the current store data

    return render(request, 'core/store_form.html', {'form': form})

def store_delete(request, pk):
    store = get_object_or_404(Store, pk=pk)
    if request.method =='POST':
        store.delete()
        return HttpResponseRedirect('/stores/')
    
    return render(request, 'core/store_confirm_delete.html', {'store': store})

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

def signup_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) # log in user automatically
            return redirect('/')
    else:
        form = UserCreationForm()
        
    return render(request, 'core/templates/signup.html', {'form': form})

def about_view(request):
    return render(request, 'core/templates/about.html')

def contact_view(request):
    return render(request, 'core/templates/contact.html')


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')
    else:
        form = AuthenticationForm()
    return render(request, 'core/templates/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('/')

@login_required
def add_favorite(request, store_id):
    store = get_object_or_404(Store, id=store_id),
    FavoriteStore.objects.get_or_create(user=request.user, store=store)
    return JsonResponse({'status': 'added'})

@login_required
def remove_favorite(request, store_id):
    store = get_object_or_404(Store, id=store_id)
    FavoriteStore.objects.filter(user=request.user, store=store).delete()
    return JsonResponse({'status': 'removed'})