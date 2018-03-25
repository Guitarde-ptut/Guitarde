from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import AuthenticationForm

from .models import Tutoriel
from .models import Commentaire

def liste_tutos(request):
    liste_tutos = Tutoriel.objects.all()
    template = loader.get_template('guitutos/liste_tutos.html')
    context = {
        'liste_tutos': liste_tutos,
        }
    return HttpResponse(template.render(context, request))

def index(request):
    template = loader.get_template('guitutos/index.html')
    return HttpResponse(template.render(None, request))

class CommentaireForm(forms.Form):
    texte = forms.CharField(label="Description",
                                  max_length=200,
                                  widget=forms.Textarea)


def tuto(request, id_tuto):
    tutoriel = get_object_or_404(Tutoriel, pk=id_tuto)
    template = loader.get_template('guitutos/tuto.html')
    liste_commentaires = Commentaire.objects.all().filter(com_tuto=id_tuto)
    form = CommentaireForm(request.POST)
    context = {
        'liste_commentaires': liste_commentaires,
        'tutoriel': tutoriel,
        'form' : form
    }
    commentaire = request.POST.get("commentaire")

#ici
    if form.is_valid() and request.user.is_authenticated:
        d = form.cleaned_data
        Commentaire.objects.create(auteur=User.objects.get(pk=request.user.id),
                                   com_tuto=tutoriel,
                                   texte=d['texte'])
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
            return redirect('connexion')
    else:
        form = UserCreationForm()
    return HttpResponse(template.render({'form':form}, request))

def connexion(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
    return render(request, 'guitutos/connexion.html', {'form': AuthenticationForm()}) 

    

def deconnexion(request):
    logout(request)
    return redirect('index')

class AjouterForm(forms.Form):
    nom = forms.CharField(label="Nom", max_length=50)
    description = forms.CharField(label="Description",
                                  max_length=350,
                                  widget=forms.Textarea)
    video = forms.URLField(label="URL")

def ajouter (request):
    template = loader.get_template("guitutos/ajouter.html")
    form = AjouterForm(request.POST)
    if form.is_valid() and request.user.is_authenticated:
        d = form.cleaned_data
        print(request.user)
        Tutoriel.objects.create(createur=User.objects.get(pk=request.user.id),
                                description=d['description'],
                                video=d['video'],
                                nom=d['nom'])
        return redirect('liste_tutos')
    else:
        print(form.errors)
        return HttpResponse(template.render({'form' : form },request))


# Create your views here.
