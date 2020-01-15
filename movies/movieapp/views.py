from django.shortcuts import render
from django.views.generic import ListView
from movieapp.models import Movielist

# Create your views here.
# def index(request):
#     return render(request, 'movieapp/index.html')


class MovieListView(ListView):
    model = Movielist
    queryset= Movielist.objects.all()
