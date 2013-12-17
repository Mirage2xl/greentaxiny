from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponseRedirect

from forms import ContactForm


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(cd['name'],
                      cd['message'],
                      cd.get('email', 'noreply@greentaxiny.net'),
                      ['greentaxiny@gmail.com'])
        return HttpResponseRedirect('/about/')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})
