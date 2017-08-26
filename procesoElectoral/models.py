# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Partido(models.Model):
    
    nombre = models.CharField(max_length=100)
    
    def __unicode__(self):
    
    	return self.nombre
    	

class Agrupacion(models.Model):
    
    nombre = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=50)
    partido = models.ForeignKey('Partido', on_delete=models.CASCADE)
    
    def __unicode__(self):
    
    	return self.nombre
    	

class Militante(models.Model):
    
    nombre = models.CharField(max_length=50)
    edad = models.IntegerField(default=18)
    dni = models.CharField(max_length=20)
    agrupacion = models.ForeignKey('Agrupacion', on_delete=models.CASCADE)
    
    def __unicode__(self):
    
    	return self.nombre
