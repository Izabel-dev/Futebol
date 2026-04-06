from django.shortcuts import render

def lista_times(request):
    return render(request, 'lista_times.html')
