from django.http import HttpResponseRedirect
from django.shortcuts import render

from contact_forms.forms import ContactForm


def home(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # process form
            pass
            return HttpResponseRedirect('/')
    return render(request, 'index.html', context={'form': form})
