# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Partido, Agrupacion, Militante

# Register your models here.

admin.site.register(Partido)
admin.site.register(Agrupacion)
admin.site.register(Militante)
