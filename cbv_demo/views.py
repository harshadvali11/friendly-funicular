from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View,TemplateView,ListView,DetailView
from . import forms
from cbv_demo.models import School
# Create your views here.

def index(request):
    return HttpResponse("Function Based Views")

class IndexView(View):
    def get(self,request):
        return HttpResponse("Class Based Views")

def temp1(request):
    return render(request,'temp1.html',context={'data':"hello world"})

class TemplateDemoView(TemplateView):
    
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['data']="Data for CBV"
        return context

class Form_Demo(View):
    def get(self,request):
        return render(request,'temp2.html',context={'form':forms.Form_name()})
    
    def post(self,request):
        form=forms.Form_name(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
        return HttpResponse("Form Submission Successful")
        #return render(request,'temp2.html',context={'form':form})

class SchoolListView(ListView):
    model=School

class SchoolDetailView(DetailView):
    model=School
    template_name='app/school_detail.html'