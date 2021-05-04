from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import Context, loader
 
def post_list(request):
    template = loader.get_template('post_list.html')
    context = {}
    return HttpResponse(template.render(context, request))

def conv(request):
    return render(request, 'blog/conv.html')
 
def info(request):
    return render(request, 'blog/info.html')


def news(request):
    return render(request, 'blog/news.html')
 
def topic(request):
    return render(request, 'blog/topic.html')
