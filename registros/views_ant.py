from django.shortcuts import render_to_response
from registros.models import Registro
from registros.forms import RegistroForm
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf



def home(request):
   entradas = Registro.objects.all()[:10]
   return render_to_response('index.html', {'resgistros' : entradas})

def one_post(request, id_registro):
    registro = Registro.objects.get(id=id_registro)
    
    return render_to_response(
        "registro.html",
        {
            "registro":registro,
        },
    )


def crear(request):
    if request.POST:
        form = RegistroForm(request.POST)
        if form.is_valid():
            nuevo = form.save()
            return HttpResponseRedirect('/registros/' + str(nuevo.id))
    else:
        form = RegistroForm()

    args = {}
    args.update(csrf(request))

    args['form'] = form

    return render_to_response('crear_registro.html', args)

#manage.py runserver --noreload