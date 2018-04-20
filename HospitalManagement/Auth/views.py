from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect, render


def register(request):
    ''' handles the registeration process '''

    context = {}
    if request.method == 'POST':
        # get the data
        first_name = request.POST.get("firstName", "")
        last_name = request.POST.get("lastName", "")
        email = request.POST.get("email", "")
        password = request.POST.get("password", "")

        try:
            # create user object
            user = User.objects.create_user(
                username=email,
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name)

        except:
            context[
                'reg_error'] = "Something went wrong, we are trying to figure it out. Give us a min!"
            return HttpResponse(render(request, 'Auth/register.html', context))

        # try to sign the user in
        user = authenticate(username=email, password=password)
        if user is not None:
            return redirect('/Patient/home')

        # couldn't sign in
        context[
            'reg_error'] = "Couldn't create that account. Try again, please!"

        return HttpResponse(render(request, 'Auth/register.html', context))

    # it is not a post
    else:
        return HttpResponse(render(request, 'Auth/register.html', context))


def signin(request):
    ''' signs people in into our application '''

    # handle a post
    if request.method == 'POST':
        context = {}
        email = request.POST.get("email", "")
        password = request.POST.get("password", "")

        user = authenticate(username=email, password=password)
        if user is not None:
            return redirect('/Patient/home')

            # bad creds
            context['reg_error'] = "Wrong email and/or password. Try again!"
            return HttpResponse(render(request, 'Auth/signin.html', context))

        try:
            pass
        except:
            context[
                'reg_error'] = "Doesn't seem like we have seen you before. Try registering first!"
            return HttpResponse(render(request, 'Auth/signin.html', context))

    # not a post request, just send the page
    else:
        return HttpResponse(render(request, 'Auth/signin.html'))
