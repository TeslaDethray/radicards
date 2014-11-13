from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render
from cards.models import Card, Template
from constance import config
from django.views import generic

class IndexView(generic.ListView):
    model = Template
    template_name = config.TEMPLATE + '/index.html'

    def get_queryset(self):
        return Template.objects.order_by('order')[:config.NUM_CARDS]

def create(request, template_id):
    try:
        template = Template.objects.get(pk = template_id)
    except Template.DoesNotExist:
        raise Http404
    return render(request, config.TEMPLATE + '/create.html', {'template': template, 'config': config})

class ResultsView(generic.DetailView): #Share
    model = Card
    template_name = config.TEMPLATE + '/share.html'


class DetailView(generic.DetailView): #View
    model = Card
    template_name = config.TEMPLATE + '/view.html'
