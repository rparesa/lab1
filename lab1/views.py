from django.shortcuts import redirect
from .models import URL
from .forms import URLForm
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from bs4 import BeautifulSoup
import requests

def url_list(request):
    urls = URL.objects.all()
    if request.method == "POST":
        form = URLForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            try: 
                response = requests.get(post)
                temp = BeautifulSoup(response.content,"lxml")
                post.title = temp.title.string
                post.finalDestination = response.url
                post.statusCode = response.status_code
            except:
                post.statusCode = "None"
                post.finalDestination = "Does not exit"
                post.title = "No title"
                pass
            finally:           
                post.save()
                return redirect('url_detail', pk=post.pk)
    else:
        form = URLForm
    return render(request, 'lab1/url_list.html',{'urls':urls,'form':URLForm})

def url_detail(request, pk):
    url = get_object_or_404(URL, pk=pk)
    return render(request, 'lab1/url_detail.html', {'url': url})

def url_delete(request, pk):
    url = get_object_or_404(URL,pk=pk)
    url.delete() 
    return HttpResponseRedirect('../')
