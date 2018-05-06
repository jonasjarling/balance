from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, get_object_or_404, redirect, resolve_url
from django.contrib.auth import authenticate, login, logout
from .forms import UserForm
from django.views.generic import View
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):


    context = {
        'test': '123'
    }
    return render(request, 'main/index.html', context)


def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        # Redirect to a success page.
        return redirect('%s?next=%s' % (profile(request), request.path))
    else:
        # Return an 'invalid login' error message.
        return redirect('%s?next=%s' % (login(request), request.path))


    #context = {

    #}
    #return render(request,'main/login.html', context)

def logout_view(request):
    logout(request)
    # Redirect to a success page.
    return render(request, 'main/index.html')


def news(request):
    context = {
        'test': '123'
    }
    return render(request, 'main/news.html', context)


@login_required(login_url='/login/')
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