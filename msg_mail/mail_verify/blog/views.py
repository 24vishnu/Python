import jwt
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from .forms import SignupForm


def reset(request):
    form = PasswordResetForm
    return render(request=request, template_name="blog/password_reset.html",
                  context={"form": form})


def home(request):
    return render(request, 'blog/home.html')


@csrf_exempt
def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            try:
                login(request, user)
            except (TypeError, ValueError, OverflowError, User.DoesNotExist):
                return render(request, 'blog/login.html')
            return render(request, 'blog/home.html')
        else:
            return redirect('login')
            # return render(request, 'blog/login.html')

    else:
        return render(request, "blog/login.html")


def logout_user(request):
    logout(request)
    return render(request, template_name="blog/home.html")


@csrf_exempt
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()

            current_site = get_current_site(request)

            mail_subject = 'Activate your blog account.'

            jwt_token = jwt.encode({user.username: user.email}, 'private_key', algorithm='HS256').decode("utf-8")

            to_email = form.cleaned_data.get('email')

            email = EmailMessage(
                mail_subject,
                'http://' + str(current_site.domain) + '/blog/activate/' + jwt_token + '/',
                to=[to_email]
            )
            email.send()
            return HttpResponse('Please active your account before login')
    else:
        form = SignupForm()
    return render(request, 'blog/signup.html', {'form': form})


def activate(request, token):
    decoded_token = jwt.decode(token, 'private_key', algorithms='HS256')

    try:
        user = User.objects.get(username=list(decoded_token.keys())[0])
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        return HttpResponse('you are not registered yet, please sign up first')
        user = None
    if user is not None and not user.is_active:
        user.is_active = True
        user.save()
        login(request, user)
        HttpResponse('Thank you for your email confirmation. Now you can login your account.')
        return render(request, 'blog/login.html')
    else:
        # form = AuthenticationForm
        return render(request, template_name='blog/home.html')
