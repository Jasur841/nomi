from django.contrib import messages
from django.contrib.admin import models
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.
from home.models import FAQ, Setting, License, Post, ContactForm, ContactMessage


def index(request):
    setting = Setting.objects.all()
    lic = License.objects.all().order_by('?')[:4]
    post = Post.objects.all().order_by('?')[:4]
    post_slider = Post.objects.all().order_by('?')[:6]
    page = 'home'
    context = {
        'lic':lic,
        'post':post,
        'setting':setting,
        'page':page,
        'psot_slider':post_slider
            }
    return render(request, 'index.html',context)


def faq(request):
    faq = FAQ.objects.filter(status = 'True').order_by('ordernumber')
    context= {'faq':faq}
    return render(request,'faq.html',context)


def about(request):
    setting = Setting.objects.all()
    return render(request,'about.html',{'setting':setting})


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            data = ContactMessage()
            data.name = form.cleaned_data['name']
            data.email  = form.cleaned_data['email']
            data.subject= form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request,'Siz habaringiz yuborildi:')
            return HttpResponseRedirect('/contact')
    setting = Setting.objects.all()
    form = ContactForm
    context =  {
        'setting':setting,
        'form': form
        }
    return render(request,'contact.html',context)


