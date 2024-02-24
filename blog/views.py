from django.shortcuts import render

# Create your views here.
def render_articles(request):
    return render(request, 'articles.html')