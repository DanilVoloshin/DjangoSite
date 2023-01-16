from django.shortcuts import render
from .forms import AddPostForm
from django.http import HttpResponse
from .models import Table, Reservation

from datetime import datetime

def order_table(request):
    tables = Table.objects.all() 
    reservation = Reservation.objects.all()
    currentDate = datetime.now().date()
    strCurrentDate = currentDate.strftime("%Y-%m-%d")
    form = AddPostForm()

    if request.method == 'POST':
        strCurrentDate = request.POST.get("date")
        currentDate = datetime.strptime(strCurrentDate, "%Y-%m-%d").date()
        if request.POST.get("name"):
            form = AddPostForm(request.POST)
            form.save()
            return render(request, 'success.html', {'table':request.POST.get('num_table'),'name':request.POST.get('name'),'date':request.POST.get('date')})

    return render(request, 'tables.html', {'tables': tables,'booking': reservation, 'newdate': currentDate, 'strNewDate': strCurrentDate, 'form': form })

