from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import NewspaperCitation, NewspaperHistory, Biography, ImprintRecord, GenericSearchResult


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
    page = request.GET.get('page')
    query_text = request.GET.get('search_term')
    url_query_string = request.GET.urlencode()

    bios = Biography.objects.filter(Q(name__icontains=query_text) |
                                    Q(notes__icontains=query_text))
    imprints = ImprintRecord.objects.filter(Q(title__icontains=query_text) |
                                            Q(short_title__icontains=query_text) |
                                            Q(notes__icontains=query_text))
    news_cites = NewspaperCitation.objects.filter(Q(title__icontains=query_text) |
                                                  Q(notes__icontains=query_text))
    news_hists = NewspaperHistory.objects.filter(Q(group_title__icontains=query_text) |
                                                 Q(notes__icontains=query_text))

    results = []
    for bio in bios:
        results.append(GenericSearchResult(bio, 1))
    for imprint in imprints:
        results.append(GenericSearchResult(imprint, 1))
    for news_cite in news_cites:
        results.append(GenericSearchResult(news_cite, 1))
    for news_hist in news_hists:
        results.append(GenericSearchResult(news_hist, 1))

    paginator = Paginator(results, 15)
    try:
        results_page = paginator.page(page)
    except PageNotAnInteger:
        results_page = paginator.page(1)

    context = {'search_term': query_text,
               'results': results_page,
               'biography': True,
               'biography_name': True,
               'biography_note': True,
               'imprint': True,
               'imprint_title': True,
               'imprint_short_title': True,
               'imprint_notes': True,
               'news_cite': True,
               'news_cite_title': True,
               'news_cite_notes': True,
               'news_hist': True,
               'news_hist_group_title': True,
               'news_hist_notes': True,
               'url_query_string': url_query_string,
               'num_results': results.__len__
               }

    return render(request, 'VirginiaPrinting/search_results.html', context)

def searchFieldsView(request):
    page = request.GET.get('page')
    query_text = request.GET.get('search_term')
    biography = request.GET.get('bio')
    biography_name = request.GET.get('bio_name')
    biography_func = request.GET.get('bio_function')
    biography_note = request.GET.get('bio_notes')
    imprint = request.GET.get('imprint')
    imprint_title = request.GET.get('imprint_title')
    imprint_short_title = request.GET.get('imprint_short_title')
    imprint_notes = request.GET.get('imprint_notes')
    url_query_string = request.GET.urlencode()

    results = []

    if biography:
        qList_bios = []

        if biography_name:
            qList_bios.append(Q(name__icontains=query_text))
        if biography_note:
            qList_bios.append(Q(notes__icontains=query_text))
        if biography_func:
            qList_bios.append(Q(function__icontains=query_text))

        query = qList_bios.pop()

        for item in qList_bios:
            query |= item

        bios = Biography.objects.filter(query)

        for bio in bios:
            results.append(GenericSearchResult(bio, 1))
    if imprint:
        qList_imprints = []

        if imprint_title:
            qList_imprints.append(Q(title__icontains=query_text))
        if imprint_short_title:
            qList_imprints.append(Q(short_title__icontains=query_text))
        if imprint_notes:
            qList_imprints.append(Q(notes__icontains=query_text))

        query = qList_imprints.pop()

        for item in qList_imprints:
            query |= item

        imprints = ImprintRecord.objects.filter(query)

        for imprint in imprints:
            results.append(GenericSearchResult(imprint, 1))

    paginator = Paginator(results, 5)
    try:
        results_page = paginator.page(page)
    except PageNotAnInteger:
        results_page = paginator.page(1)

    context = {'search_term': query_text,
               'results': results_page,
               'biography': biography,
               'biography_name': biography_name,
               'biography_func': biography_func,
               'biography_note': biography_note,
               'url_query_string': url_query_string,
               'imprint': imprint,
               'imprint_title': imprint_title,
               'imprint_short_title': imprint_short_title,
               'imprint_notes': imprint_notes,
               'news_cite': True,
               'news_cite_title': True,
               'news_cite_notes': True,
               'news_hist': True,
               'news_hist_group_title': True,
               'news_hist_notes': True,
               'num_results': results.__len__}

    return render(request, 'VirginiaPrinting/search_results.html', context)


class NewsCitesListView(generic.ListView):
    model = NewspaperCitation
    template_name = 'VirginiaPrinting/newspaper_citation_index.html'
    context_object_name = 'news_cites'
    paginate_by = 10


class NewsHistsListView(generic.ListView):
    model = NewspaperHistory
    template_name = 'VirginiaPrinting/newspaper_history_index.html'
    context_object_name = 'news_hists'
    paginate_by = 10


class BiosListView(generic.ListView):
    model = Biography
    template_name = 'VirginiaPrinting/biography_index.html'
    context_object_name = 'bios'
    paginate_by = 10


class ImprintsListView(generic.ListView):
    model = ImprintRecord
    template_name = 'VirginiaPrinting/imprint_record_index.html'
    context_object_name = 'imprints'
    paginate_by = 10


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
