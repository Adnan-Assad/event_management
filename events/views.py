from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from django.http import HttpResponse
from events.models import Category, Participant, Event
from events.forms import CategoryModelForm, EventModelForm, ParticipantModelForm
from django.db.models import Count, Q, Sum , Avg 
from datetime import date
from django.utils.timezone import now

# Create your views here.

def event_list(request):
    query =request.GET.get('q')
    category_id = request.GET.get('category')
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    events = Event.objects.select_related('category').prefetch_related('participants')
    if query:
        events = events.filter(Q(name__icontains=query) | Q(location__icontains=query))
    if category_id and category_id.isdigit():
        events = events.filter(category_id=category_id)
    if start_date and end_date:
        events = events.filter(date__range=[start_date, end_date])
    categories = Category.objects.all()

    context = {
        'events':events,
        'categories':categories,
        'query': query,
        'start_date': start_date,
        'end_date': end_date
    }
    return render(request, 'events/event_list.html', context)
def event_detail(request, id):
    event = get_object_or_404(Event.objects.select_related('category').prefetch_related('participants'), id=id)
    return render(request, 'events/event_detail.html', {'event': event})

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'events/category_list.html', {'categories': categories})
def category_create(request):
    if request.method =='POST':
        form = CategoryModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryModelForm()
    return render(request, 'events/category_form.html', {'form': form})
def category_update(request,id):
    category = get_object_or_404(Category, id = id)
    if request.method == 'POST':
        form = CategoryModelForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryModelForm(instance=category)
    return render(request,'events/category_form.html', {'form':form})

def category_delete(request, id):
    category = get_object_or_404(Category, id = id)
    if request.method == 'POST':
        category.delete()
        return redirect('category_list')
    return render(request, 'events/category_confirm_delete.html', {'category':category})

def event_create(request):
    if request.method == 'POST':
        form =EventModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('event_list')
    else:
        form = EventModelForm()
    return render(request, 'events/event_form.html', {'form': form})


def event_update(request, id):
    event = get_object_or_404(Event, id=id)
    if request.method == 'POST':
        form = EventModelForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('event_list')
    else:
        form = EventModelForm(instance=event)
    return render(request, 'events/event_form.html', {'form': form})
def event_delete(request, id):
    event = get_object_or_404(Event, id = id)
    if request.method == 'POST':
        event.delete()
        messages.success(request,"Event deleted successfully")
        return redirect('event_list')
        
    return render(request, 'events/event_confirm_delete.html', {'event':event})
def participant_list(request):
    participants =Participant.objects.prefetch_related('events').all()
    return render(request,'events/participant_list.html', {'participants':participants})

def participant_create(request):
    if request.method =='POST':
        form = ParticipantModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('participant_list')
    else:
        form = ParticipantModelForm()
    return render(request, 'events/participant_form.html', {'form':form})
def participant_update(request, id):
    participant = get_object_or_404(Participant, id = id)
    if request.method =='POST':
        form = ParticipantModelForm(request.POST, instance=participant)
        if form.is_valid():
            form.save()
            return redirect('participant_list')
    else:
        form = ParticipantModelForm(instance=participant)
    return render(request, 'events/participant_form.html', {'form':form})
def participant_delete(request, id):
    participant = get_object_or_404(Participant, id = id)
    if request.method =='POST':
        participant.delete()
        return redirect('participant_list')
    return render(request, 'events/participant_confirm_delete.html', {'participant':participant})


def dashboard(request):
    total_participants = Participant.objects.aggregate(total=Count('id'))['total']
    total_events = Event.objects.count()
    today = date.today()
    upcoming_events = Event.objects.filter(date__gte=today).count()
    past_events = Event.objects.filter(date__lt=today).count()
    todays_events = Event.objects.filter(date=today).select_related('category').prefetch_related('participants')
    filter_type =request.GET.get('filter', 'all')
    if filter_type == 'upcoming':
        filtered_events = Event.objects.filter(date__gte=today).select_related('category').prefetch_related('participants')
    elif filter_type =='past':
        filtered_events = Event.objects.filter(date__lt=today).select_related('category').prefetch_related('participants')
    else:
        filtered_events = Event.objects.all().select_related('category').prefetch_related('participants')
    context ={
        'total_participants': total_participants,
        'total_events':total_events,
        'upcoming_events':upcoming_events,
        'past_events': past_events,
        'todays_events': todays_events,
        'filtered_events': filtered_events,
        'filter_type': filter_type,
    }
    return render(request, 'events/dashboard.html', context)






        
