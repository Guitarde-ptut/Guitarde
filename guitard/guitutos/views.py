from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, render

from .models import Tutoriel
from .models import Commentaire

def liste_tutos(request):
    liste_tutos = Tutoriel.objects.all()[:5]
    template = loader.get_template('guitutos/liste_tutos.html')
    context = {
        'liste_tutos': liste_tutos,
        }
    return HttpResponse(template.render(context, request))

def index(request):
    return render_to_response(template.render("guitutos/index.html", request))

def tuto(request, id_tuto):
    tutoriel = get_object_or_404(Tutoriel, pk=id_tuto)
    template = loader.get_template('guitutos/tuto.html')
    liste_commentaires = Commentaire.objects.all().filter(com_tuto=id_tuto)
    context = {
        'liste_commentaires': liste_commentaires,
        'tutoriel': tutoriel,
    }
    return HttpResponse(template.render(context, request))

# Create your views here.
