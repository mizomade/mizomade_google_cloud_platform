from django.shortcuts import render,get_object_or_404
from .models import *

# Create your views here.

def trip_single(request, slug):
        
        trag = get_object_or_404(BlogPage, slug=slug)
        related = trag.tags.similar_objects()
        return render(request, 'blog/trag.html', {'trag': trag, 'related': related})