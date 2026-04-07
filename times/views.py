from django.shortcuts import render
from .models import Time

def lista_times(request):
    times = Time.objects.all() .order_by('fundacao')
    return render(request, 'lista_times.html', {'times': times})  
