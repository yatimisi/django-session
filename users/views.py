from django.http import HttpResponse
from django.shortcuts import render, redirect

def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        
        ## Use cookies
        # res = redirect(index)
        # res.set_cookie('name', name)
        # return res

        request.session['name'] = name
        return redirect(index)

    # name = request.COOKIES.get('name')
    name = request.session.get('name')

    if name:
        return HttpResponse('Hello, {} welcome back!'.format(name))

    return render(request, 'index.html')
