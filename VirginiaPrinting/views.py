from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import NewspaperCitation


# Create your views here.
def index(request):
    return HttpResponse("Hello, Virginia")


def news_cite_detail(request, obj_id):
    newspaper_citation = get_object_or_404(NewspaperCitation, pk=obj_id)
    return render(request, 'VirginiaPrinting/newspaper_citation.html', {'newspaper_citation': newspaper_citation})