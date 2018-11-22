#Maria Alvarez Hernandez ID: 4-0239-0850
#Luis Alonso Calderon Achio ID: 1-1702-0626
#Enrique Diaz Delgado ID: 1-1725-0124
#Derian Sibaja Chavarria ID 4-0232-0842


from django.shortcuts import render , get_object_or_404
from django.http import HttpResponseRedirect
from django.core.mail import send_mail, get_connection
# Create your views here.
from django.http import HttpResponse
from .models import Page
from .forms import AfirmacionForm
from django.http import Http404
import requests

PAGES = [
    {
        "title": "Home",
        "bodytext": "Demostrador de teoremas de lógica proposicional utilizando el algoritmo de Wang clásico (Top Down). Este es un proyecto realizado para el curso de Paradigmas de Programación de la Universidad Nacional de Costa Rica",
        "permalink": '/'
    },
    {
        "title": "About us",
        "bodytext": "Somos estudianes de la carrera de Ingeniería en Sistemas de la Universidad Nacional de Costa Rica",
        "permalink": '/about'
    },
    {
        "title": "Probar",
        "bodytext": "Probar",
        "permalink": '/probar'
    },
    {
        "title": "Historial de pruebas",
        "bodytext": "Historial",
        "permalink": '/historial'
    },
]

def index(request,pagename):
    #return HttpResponse("<h1>My index page</h1>")
    #return render(request, "base.html")
    # return render(request, "pages/page.html")
    pagename = "/" + pagename
    the_page = next((x for x in PAGES if pagename == x['permalink']), None)
    if (not the_page):
        raise Http404()
    context = {
        "title": the_page["title"],
        "content": the_page["bodytext"],
        "page_list": PAGES
    }
    if the_page["bodytext"] == 'Probar' :
        return render(request, "pages/pageForm.html",context)
    elif the_page["bodytext"] == "Historial":
        context['pruebas'] = requests.get('https://servidordjango.herokuapp.com/api/pruebas').json
        return render(request, "pages/historial.html", context)
    else:
        return render(request, "pages/page.html",context)


	

# def afirmacion(request):
    # submitted = False
    # if request.method == 'POST':
       # afirmacion = request.POST.get('afirmacion')
       # r = requests.post('http://127.0.0.1:8081/api/pruebas', data={'afirmacion': afirmacion})
       # if r.status_code == 200:
           # response = r.json()
       # else:
           # return HttpResponseRedirect('/afirmacion?submitted=False')
    # else:
        # form = AfirmacionForm()
        # if 'submitted' in request.GET:
            # submitted = True

    # return render(request,
                  # 'pages/afirmacion.html',
                  # {'form': form,
                   # 'page_list': Page.objects.all(),
                   # 'submitted': submitted})
