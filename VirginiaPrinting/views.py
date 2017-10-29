from django.http import HttpResponse
from django.views import generic

from .models import NewspaperCitation, NewspaperHistory


# Create your views here.
def index(request):
    return HttpResponse("Hello, Virginia")


class NewsCiteDetailView(generic.DetailView):
    model = NewspaperCitation
    context_object_name = 'newspaper_citation'
    template_name = 'VirginiaPrinting/newspaper_citation.html'


class NewsHistDetailView(generic.DetailView):
    model = NewspaperHistory
    context_object_name = 'newspaper_history'
    template_name = 'VirginiaPrinting/newspaper_history.html'
