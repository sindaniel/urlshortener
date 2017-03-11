from django.shortcuts import render

from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

from django.contrib.auth import(
    authenticate,
    login,
    logout
)


from .forms import UserLoginForm, UserRegisterForm

def login_view (request):
    title = 'Ingresar'
    form  = UserLoginForm(request.POST or None)

    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        return HttpResponseRedirect(reverse('pages:index'))
    return render(request, "accounts/home.html", {'form':form, 'title':title})



def register_view (request):

    if(request.user.is_authenticated()):
        return HttpResponseRedirect(reverse('pages:index'))

    form = UserRegisterForm(request.POST or None)

    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        name = form.cleaned_data.get('name')
        user.set_password(password)
        user.save()


        new_user = authenticate(username=username, password=password)
        if new_user is not None:
            login(request, new_user)
            return HttpResponseRedirect(reverse('pages:index'))

    context = {
        'form': form,
        'title': 'Register'
    }

    return render(request, "accounts/home.html", context)


def logout_view (request):
    logout(request)
    return HttpResponseRedirect(reverse('pages:index'))
