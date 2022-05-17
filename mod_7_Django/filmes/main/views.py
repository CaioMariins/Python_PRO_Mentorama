from django.shortcuts import render
from .models import ProjetoDjango

# Create your views here.
def homepage(request):
    return render(
        request = request,
        template_name = "home.html",
        context = {"filmes": ProjetoDjango.objects.all}
    )