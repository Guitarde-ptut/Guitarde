from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

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
    template = loader.get_template('guitutos/index.html')
    return HttpResponse(template.render(None, request))

def tuto(request, id_tuto):
    tutoriel = get_object_or_404(Tutoriel, pk=id_tuto)
    template = loader.get_template('guitutos/tuto.html')
    liste_commentaires = Commentaire.objects.all().filter(com_tuto=id_tuto)
    context = {
        'liste_commentaires': liste_commentaires,
        'tutoriel': tutoriel,
    }
    commentaire = request.POST.get("commentaire")
    if request.method == 'POST' \
       and len(commentaire)>0 \
       and User.objects.filter(username=request.user).exists():          
        Commentaire.objects.create(auteur=request.user,
                                   com_tuto=tutoriel,
                                   texte=commentaire)
    return HttpResponse(template.render(context, request))

def inscription(request):
    template = loader.get_template('guitutos/inscription.html')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return HttpResponse(template.render({'form':form}, request))

def connexion(request):
    template = loader.get_template('guitutos/connexion.html')
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
    return HttpResponse(template.render(None, request))
    

def deconnexion(request):
    logout(request)
    return redirect('index')

def ajouter (request):
    template = loader.get_template("guitutos/ajouter.html")
    nom = request.POST.get("nom")
    description = request.POST.get("description")
    video = request.POST.get("video")
    if request.method == 'POST' \
       and len(video)>0 \
       and len(nom)>0 \
       and User.objects.filter(username=request.user).exists():          
        Tutoriel.objects.create(createur=request.user,
                                description=description,
                                video=video,
                                nom=nom)
        return redirect('liste_tutos')
    return HttpResponse(template.render(None, request))


# Create your views here.
