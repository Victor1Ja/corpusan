from django.shortcuts import render,redirect
from .models import Transcrip
from .forms import TranscripForm
from django.core.paginator import Paginator
from django.forms.utils import ErrorList
from django.views.generic.edit import FormView
from .strings import strings
from django.contrib import messages
# Create your views here.
def handle_uploaded_file(**kargs):  
    for f in kargs:
        with open('geeks / upload/'+f.name, 'wb+') as destination:  
            for chunk in f.chunks():
                destination.write(chunk)


def index(request):
    """
    view de index muestra una lista de todas las transcripciones
    """

    transcrip = Transcrip.objects.all()
    transcrip = transcrip.filter(code__icontains = '_')
#    print(transcrip)
    code  = request.GET.get('code')
    city  = request.GET.get('city')
    country  = request.GET.get('country')
    #search
    if code != '' and code is not None:
        transcrip = transcrip.filter(code__icontains = code)
    if city != '' and city is not None:
        transcrip = transcrip.filter(city__icontains = city)
    if country != '' and country is not None:
        transcrip = transcrip.filter(country__icontains = country)

    #paginator
    paginator = Paginator(transcrip,5)
    page = request.GET.get('page')
    transcrip = paginator.get_page(page)

    return render(request,'transcrip/index.html', {'transcrips':transcrip, 'get':request.GET, 'strings':strings} )


def addItem(request):

    if request.method == 'POST':
        form = TranscripForm(request.POST,request.FILES)
        print(request.FILES)
        
        print(form.is_valid(), form.errors)
        if form.is_valid():
            print("salvo")
            form.save()
            messages.success(request, f'Grabación agregada correctamente')
            return redirect('transcrip:add') 
        else:
        #return redirect('index')
            print("post pero no salvo")
            messages.error(request, f'Grabación agregada correctamente')
    else:
        form = TranscripForm()
        print("no salvo")
        #print(request.POST)
        print(form.errors)
        print(form.is_valid() , form.has_error(field='code'), form.has_error(field='descrip'), form.has_error(field='transcrip'), form.has_error(field='audio'))
        
    return render(request,'transcrip/transcripForm.html', {'form': form , 'strings':strings} )
    