from django.shortcuts import render
# Create your views here.
from .models import Post

def home(request):
    data = Post.objects.all()
    return render(request, "index.html", {'posts':data})