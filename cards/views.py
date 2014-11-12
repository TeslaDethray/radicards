from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render
from cards.models import Card, Template
#from settings.models import Settings

def index(request):
    return HttpResponse("Index page")

def create(request, template_id):
    try:
        template = Template.objects.get(pk = template_id)
    except Template.DoesNotExist:
        raise Http404
    return render(request, 'cards/create.html', {'template': template})

def share(request, hashed_id):
    try:
        card = Card.objects.get(hashed_id = hashed_id)
    except Card.DoesNotExist:
        raise Http404
    return render(request, 'cards/share.html', {'card': card})

def view(request, hashed_id):
    try:
        card = Card.objects.get(hashed_id = hashed_id)
    except Card.DoesNotExist:
        raise Http404
    return render(request, 'cards/view.html', {'card': card})
