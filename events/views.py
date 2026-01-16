
from django.shortcuts import render,redirect
from django.db.models import Count
from datetime import date
from .models import Event
from .forms import EventForm

def dashboard(request):
    events = Event.objects.select_related('category').prefetch_related('participants')
    stats = {
        'total_events': events.count(),
        'upcoming': events.filter(date__gte=date.today()).count(),
        'past': events.filter(date__lt=date.today()).count(),
        'participants': events.aggregate(total=Count('participants'))['total']
    }
    today_events = events.filter(date=date.today())
    return render(request,'events/dashboard.html',{'stats':stats,'today_events':today_events})

def event_list(request):
    q = request.GET.get('q','')
    events = Event.objects.filter(name__icontains=q) if q else Event.objects.all()
    return render(request,'events/event_list.html',{'events':events})

def event_create(request):
    form = EventForm(request.POST or None)
    if form.is_valid():
        form.save(); return redirect('event_list')
    return render(request,'events/event_form.html',{'form':form})
