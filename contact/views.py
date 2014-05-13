from django.shortcuts import render
from contact.forms import ContactForm
from django.http import HttpResponseRedirect
from django.core.mail import send_mail

# Create your views here.
def contact(request):
    errors = []
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email'),
                ['sanke93@gmail.com'], #email address where message is sent.
            )
            return HttpResponseRedirect('thanks/')
    else:
        form = ContactForm()
    context = {'form':form, }
    return render(request, 'contact.html', context)


def thanks(request):
    return render(request, 'thanks.html')
