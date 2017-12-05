from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic
from django.db.models import Q
from .models import NewspaperCitation, NewspaperHistory, Biography, ImprintRecord


# Create your views here.
def index(request):
    news_cites = NewspaperCitation.objects.count()
    news_hists = NewspaperHistory.objects.count()
    bios = Biography.objects.count()
    imprints = ImprintRecord.objects.count()
    context = {'num_news_cites': news_cites,
               'num_news_hists': news_hists,
               'num_bios': bios,
               'num_imprints': imprints}
    return render(request, 'VirginiaPrinting/index.html', context)

def chronologyView(request):
    imprints = ImprintRecord.objects.all().order_by('year')
    context = {'imprints': imprints}
    return render(request, 'VirginiaPrinting/chronology_imprints.html', context)

def searchView(request):
    query_text = request.GET.get('search_term')

    bios = Biography.objects.filter(Q(name__icontains=query_text) | Q(notes__icontains=query_text))

    context = {'search_term': query_text,
               'biographies': bios}

    return render(request, 'VirginiaPrinting/search_results.html', context)

def searchFieldsView(request):
    query_text = request.GET.get('search_term')
    biography_name = request.GET.get('bio_name')
    biography_func = request.GET.get('bio_function')

    print(biography_name)
    print(biography_func)

    bios = Biography.objects.filter(name__icontains=query_text)

    context = {'search_term': query_text,
               'biographies': bios}

    return render(request, 'VirginiaPrinting/search_results.html', context)


class NewsCitesListView(generic.ListView):
    model = NewspaperCitation
    template_name = 'VirginiaPrinting/newspaper_citation_index.html'
    context_object_name = 'news_cites'


class NewsHistsListView(generic.ListView):
    model = NewspaperHistory
    template_name = 'VirginiaPrinting/newspaper_history_index.html'
    context_object_name = 'news_hists'


class BiosListView(generic.ListView):
    model = Biography
    template_name = 'VirginiaPrinting/biography_index.html'
    context_object_name = 'bios'


class ImprintsListView(generic.ListView):
    model = ImprintRecord
    template_name = 'VirginiaPrinting/imprint_record_index.html'
    context_object_name = 'imprints'


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
