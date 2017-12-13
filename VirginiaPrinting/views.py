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

def aboutView(request):
    return render(request, 'VirginiaPrinting/about.html')

def chronologyView(request):
    imprints = ImprintRecord.objects.all().order_by('year')
    context = {'imprints': imprints}
    return render(request, 'VirginiaPrinting/chronology_imprints.html', context)

def searchView(request):
    query_text = request.GET.get('search_term')

    bios = Biography.objects.filter(Q(name__icontains=query_text) | Q(notes__icontains=query_text))

    context = {'search_term': query_text,
               'biographies': bios,
               'biography_name': True,
               'biography_note': True}

    return render(request, 'VirginiaPrinting/search_results.html', context)

def searchFieldsView(request):
    query_text = request.GET.get('search_term')
    biography_name = request.GET.get('bio_name')
    biography_func = request.GET.get('bio_function')
    biography_note = request.GET.get('bio_notes')

    qName = Q(name__icontains=query_text)
    qFunc = Q(function__icontains=query_text)
    qNotes = Q(notes__icontains=query_text)

    if biography_name:
        if biography_func:
            if biography_note:
                bio = Biography.objects.filter(qName | qFunc | qNotes)
            else:
                bio = Biography.objects.filter(qName | qFunc)
        else:
            if biography_note:
                bio = Biography.objects.filter(qName | qNotes)
            else:
                bio = Biography.objects.filter(qName)
    else:
        if biography_func:
            if biography_note:
                bio = Biography.objects.filter(qFunc | qNotes)
            else:
                bio = Biography.objects.filter(qFunc)
        else:
            if biography_note:
                bio = Biography.objects.filter(qNotes)
            else:
                bio = None

    context = {'search_term': query_text,
               'biographies': bio,
               'biography_name': biography_name,
               'biography_func': biography_func,
               'biography_note': biography_note}

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
