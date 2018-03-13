from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login
from .forms import UserForm
from django.views.generic import View

# Create your views here.
def index(request):


    context = {
        'test': '123'
    }
    return render(request, 'main/index.html', context)


def login(request):


    context = {

    }
    return render(request,'main/login.html', context)




def news(request):
    context = {
        'test': '123'
    }
    return render(request, 'main/news.html', context)



def profile(request):
    context = {
        'test': '123'
    }
    return render(request, 'main/profile.html', context)

class UserFormView(View):
    form_class = UserForm
    template_name = 'main/registrationForm.html'

    def get(self, request):
        form  =self.form_class(None)
        return render(request, self.template_name, {'form' : form})


    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():

            user = form.save(commit=False)

            #cleaned and normalized data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.username = username
            user.save()

            # returns User object if credentials are correct
            user = authenticate(username=username, password=password)

            if user is not None:

                if user.is_active():
                    login(request, user)
                    return redirect('main:index')
        return render(request, self.template_name, {'form': form})