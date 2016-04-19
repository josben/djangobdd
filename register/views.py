from django.shortcuts import render
from register.forms import PersonForm
from register.models import Person
from django.http import HttpResponseRedirect

def register(request):
    person_list = Person.objects.all()
    return render(request, 'register/register.html', {'list': person_list})

def form_register(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/register/')
        else:
            form = PersonForm()
            return render(request, 'form_register.html', {'form': form})
    else:
        form = PersonForm()
        return render(request, 'register/form_register.html', {'form': form})

