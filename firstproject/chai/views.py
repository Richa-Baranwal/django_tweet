from django.shortcuts import render
from .models import ChaiVarity, ChaiStore
from django.shortcuts import get_object_or_404
from .forms import ChaiVarityForm

# Create your views here.
def myapp(request):
    chais = ChaiVarity.objects.all()
    return render(request, 'chai/myapp.html', {'chais': chais})

def order(request):
    chais = ChaiVarity.objects.all()
    return render(request, 'chai/order.html', {'chais': chais})

def chai_detail(request, chai_id):
    chai = get_object_or_404(ChaiVarity, pk=chai_id)
    return render(request, 'chai/chai_detail.html', {'chai': chai})

def chai_store_view(request):
    stores = None
    if request.method == 'POST':
        form = ChaiVarityForm(request.POST)
        if form.is_valid():
            selected_chai = form.cleaned_data['chai_varity']
            stores = ChaiStore.objects.filter(chai_varieties=selected_chai)
    else:
        form = ChaiVarityForm()

    return render(request, 'chai/chai_stores.html', {'stores': stores, 'form': form})