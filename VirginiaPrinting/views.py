from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic

from .models import NewspaperCitation, NewspaperHistory, Biography, ImprintRecord


# Create your views here.
def index(request):
    news_cites = NewspaperCitation.objects.all()
    news_hists = NewspaperHistory.objects.all()
    bios = Biography.objects.all()
    imprints = ImprintRecord.objects.all()
    context = {'news_cites': news_cites,
               'news_hists': news_hists,
               'bios': bios,
               'imprints': imprints}
    return render(request, 'VirginiaPrinting/index.html', context)


def news_cites_index(request):
    return HttpResponse("Index of Newspaper Citations")


def news_hists_index(request):
    return HttpResponse("Index of Newspaper Histories")


def bios_index(request):
    return HttpResponse("Index of Biographies")


def imprints_index(request):
    return HttpResponse("Index of Imprint Records")


class NewsCiteDetailView(generic.DetailView):
    model = NewspaperCitation
    context_object_name = 'newspaper_citation'
    template_name = 'VirginiaPrinting/newspaper_citation.html'


class NewsHistDetailView(generic.DetailView):
    model = NewspaperHistory
    context_object_name = 'newspaper_history'
    template_name = 'VirginiaPrinting/newspaper_history.html'


class BioDetailView(generic.DetailView):
    model = Biography
    context_object_name = 'biography'
    template_name = 'VirginiaPrinting/biography.html'


class ImprintDetailView(generic.DetailView):
    model = ImprintRecord
    context_object_name = 'imprint_record'
    template_name = 'VirginiaPrinting/imprint_record.html'
