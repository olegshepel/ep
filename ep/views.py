from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponseRedirect
from .forms import Form


def create_form(request):
    if request.method == 'POST':
        form = Form(request.POST or None)
        if form.is_valid():
            url = request.POST.get('url')
            hash = request.POST.get('hash')
            path = f'/link/{url}/{hash}/'
            return redirect(path)
    else:
        form = Form()
    return render(request, 'shortener.html', {
        'form': form,
    })


def url_hash(request, url, hash):
    return render(request, 'shortened.html', {
        'url': f'/link/{url}/',
        'new_url': f'/link/{url}/{hash}/'
    })


def url_path(request, url):
    return render(request, 'linked.html', {
        'url': url
    })
