# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from .models import Partido, Agrupacion, Militante
from .forms import AuthenticationForm, PartidoForm, AgrupacionForm, MilitanteForm

# Create your views here.

def index(request):
    return render(request, 'procesoElectoral/index.html')
    
def userLogin(request):
    
    if request.method == 'POST':
    
        form = AuthenticationForm(request.POST)
        
        if form.is_valid:
        
            username = request.POST['username']
            password = request.POST['password']
            
            user = authenticate(username=username, password=password)
            
            if user is not None:
            
                if user.is_active:
            
                    login(request, user)
                    return redirect('/')
    else:
    
        form = AuthenticationForm()
        
    context = {'form':form}
    return render(request, 'procesoElectoral/login.html', context)
        

@login_required
def userLogout(request):

    logout(request)
    return redirect('/')      
      
            
def listPartidos(request):

    partidos = Partido.objects.all()
    return render(request, 'procesoElectoral/partido.html', {'partidos':partidos})
    

@login_required
def addPartido(request):

    if request.method == 'POST':
    
        form = PartidoForm(request.POST)
        
        if form.is_valid:
        
            partido = form.save(commit=False)
            partido.save()
            return redirect('/partidos')
            
    else:
    
        form = PartidoForm()
        
    context = {'form':form}
    return render(request, 'procesoElectoral/add_partido.html', context)


@login_required
def editPartido(request, id_partido):

    partido = get_object_or_404(Partido, pk=id_partido)
	
    if request.method == 'POST':

        form = PartidoForm(request.POST, instance=partido)
	    
	if form.is_valid:
	    
	    partido = form.save(commit=False)
	    partido.save()
	    return redirect('/partidos')
	       
    else:
    
        form = PartidoForm()
        
    context = {'form':form}
    return render(request, 'procesoElectoral/edit_partido.html', context)
   

@login_required
def deletePartido(request, id_partido):

    partido = get_object_or_404(Partido, pk=id_partido)
    
    if request.method == 'POST':
        
        partido.delete()
        return redirect('/partidos')
        
    return render(request, 'procesoElectoral/delete_partido.html')
            

@method_decorator(login_required, name='dispatch')
class ListAgrupaciones(ListView):
    
    model = Agrupacion
    
    def get(self, request, *args, **kwargs):
    
        agrupaciones = Agrupacion.objects.all()
        context = {'agrupaciones':agrupaciones,'titulo':"Lista de Agrupaciones"}
        return render(request, 'procesoElectoral/agrupacion.html', context)
        
        
@method_decorator(login_required, name='dispatch')
class DetailAgrupacion(DetailView):
    
    model = Agrupacion
        

@method_decorator(login_required, name='dispatch')
class AddAgrupacion(CreateView):

    model = Agrupacion
    form_class = AgrupacionForm
    
    def get(self, request, *args, **kwargs):
    
        if request.user.is_staff:
        
            form = self.form_class()
            context = {'form':form,'titulo':"Añadir nueva Agrupacion"}
            return render(request, 'procesoElectoral/add_agrupacion.html', context)
            
        else:
        
            return HttpResponseRedirect('/login')
            
    def post(self, request, *args, **kwargs):
    
        if request.user.is_staff:
        
            form = self.form_class(request.POST, request.FILES)
            
            if form.is_valid:
            
                militante = form.save()
                return HttpResponseRedirect('/agrupaciones')
                
            context = {'form':form,'titulo':"Añadir nueva Agrupacion"}
            return render(request, 'procesoElectoral/add_agrupacion.html', context)
    

@method_decorator(login_required, name='dispatch')
class EditAgrupacion(UpdateView):

    model = Agrupacion
    form_class = AgrupacionForm
        

@method_decorator(login_required, name='dispatch')
class DeleteAgrupacion(DeleteView):

    model = Agrupacion


@login_required
def listMilitantes(request):

    militantes = Militante.objects.all()
    return render(request, 'procesoElectoral/militante.html', {'militantes':militantes})
    
    
@login_required
def detailMilitante(request, id_militante):

    militante = get_object_or_404(Militante, pk=id_militante)
    return render(request, 'procesoElectoral/detail_militante.html', {'militante':militante})
    
    
@login_required
def addMilitante(request):
    
    if request.method == 'POST':
    
        form = MilitanteForm(request.POST)
        
        if form.is_valid:
        
            militante = form.save(commit=False)
            militante.save()
            return redirect('/militantes')
            
    else:
    
        form = MilitanteForm()
        
    context = {'form':form}
    return render(request, 'procesoElectoral/add_militante.html', context)
    
    
@login_required
def editMilitante(request, id_militante):

    militante = get_object_or_404(Militante, pk=id_militante)
     
    if request.method == "POST":
    
        form = MilitanteForm(request.POST, instance=militante)
        
        if form.is_valid:
        
            militante = form.save(commit=False)
            militante.save()
    	    return redirect('/militantes')
    	    
    else:
    
        form = MilitanteForm()
        
    context = {'form':form}
    return render(request, 'procesoElectoral/edit_militante.html', context)
   

@login_required
def deleteMilitante(request, id_militante):

    militante = get_object_or_404(Militante, pk=id_militante)
    
    if request.method == 'POST':
        
        militante.delete()
        return redirect('/militantes')
        
    return render(request, 'procesoElectoral/delete_militante.html')

@login_required
def addMilitante(request):
    
    if request.method == 'POST':
    
        form = MilitanteForm(request.POST)
        
        if form.is_valid:
        
            militante = form.save(commit=False)
            militante.save()
            return redirect('/militantes')
            
    else:
    
        form = MilitanteForm()
        
    context = {'form':form}
    return render(request, 'procesoElectoral/add_militante.html', context)
    

@login_required
def cuentaMilitantes(request, id_partido):

    partido = get_object_or_404(Partido, pk=id_partido)
    contador = 0
    
    query_agrupacion = partido.agrupacion_set.all()
    
    for agrupacion in query_agrupacion:
    
        query_militante = agrupacion.militante_set.all()
        contador = contador + len(query_militante)
        
    return contador
